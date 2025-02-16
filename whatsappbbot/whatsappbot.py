import datetime
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
#from poemoftheday import poems
#from pod import poem_of_the_day


# Error logging function
def log_error(error_message):
    with open("C:\\Users\\lecke\\.vscode\\python\\whatsappbbot\\error_log.txt", "a") as error_file:
        error_file.write(f"{datetime.datetime.now()} - {error_message}\n")


def allow_to_send(contact_name, message, send_time, repeat):
    try:
        with open("C:\\Users\\lecke\\.vscode\\python\\whatsappbbot\\log.txt", "r") as file:
            lines = file.readlines()

        if send_time: send_time = datetime.datetime.strptime(send_time, "%Y-%m-%d %H:%M:%S.%f")
        for line in reversed(lines):
            parts = line.strip().split(',', 2)

            if len(parts) < 3:
                continue  # Skip lines that don't have enough values

            log_date, name, log_message = parts
            log_date = datetime.datetime.strptime(log_date, "%Y-%m-%d %H:%M:%S.%f").replace(hour=0,minute=0,second=0,microsecond=0)


            if (name == contact_name and log_message == message):
                time_diff = datetime.datetime.now() - log_date
                if repeat == "day": return time_diff.days >= 1
                elif repeat == "week": return time_diff.days >= 7
                elif repeat == "month": 
                    return (log_date.day == send_time.day == datetime.datetime.now().day and  
                    log_date.month != send_time.month)
                elif repeat == "year": 
                    return (log_date.replace(year=1) == send_time.replace(year=1) and 
                    time_diff.days // 365 >= 1 and 
                    datetime.datetime.now().replace(year=1,hour=0,minute=0,second=0,microsecond=0) == send_time.replace(year=1))

        if send_time: 
            if repeat == "year": return datetime.datetime.now().replace(year=1,hour=0,minute=0,second=0,microsecond=0) == send_time.replace(year=1)
            if repeat == "month": return datetime.datetime.now().day == send_time.day
        return True
    except FileNotFoundError:
        return True


def get_pod():
    # URL of the Poem of the Day
    url = "https://www.poetryfoundation.org/poems/poem-of-the-day"

    response = requests.get(url)
    # Send a GET request to fetch the raw HTML content
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the title, author, and text
    title = soup.find('h4', class_='type-gamma').get_text(strip=True)
    author = soup.find('div', class_='type-kappa').get_text(strip=True)
    author = author.replace("By", "")
    text = soup.find('div', class_='rich-text col-span-full md:text-xl').get_text("\n", strip=True)

    poem_of_the_day =f"""*{title}* 

{text}

By _{author}_""" 
    return poem_of_the_day


def test():
    # Edge WebDriver Path
    edge_driver_path = "C:\\edgedriver\\msedgedriver.exe"

    # Edge options (keep WhatsApp logged in)
    edge_options = Options()
    edge_options.add_argument("user-data-dir=C:\\Users\\lecke\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")  # Replace with actual path
    edge_options.add_argument("--headless")  # No UI
    edge_options.add_argument("--disable-gpu")

    # Start Edge WebDriver
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Wait for WhatsApp Web to load
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")))

    def change_contact(contact_name):
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        search_box.click()
        search_box.send_keys(contact_name)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)

    def send_message(message):
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//footer//div[@contenteditable='true']")))
        for line in message.split("\n"):
            message_box.send_keys(line)
            message_box.send_keys(Keys.SHIFT, Keys.ENTER)
        message_box.send_keys(Keys.ENTER)
        print(f"✅ Message sent successfully! [{message.replace('\n', ' ')}]")

    planned_messages = [
        {"name": "Jonas", "message": "HAPPY YEAR", "send_time": "2006-03-05 00:00:00.0", "repeat": "year"},
        {"name": "Jonas", "message": "HAPPY MONTH", "send_time": "2006-02-15 00:00:00.0", "repeat": "month"},
        #{"name": "Jonas", "message": "HAPPY WEEK", "send_time": "2006-02-16 00:00:00.0", "repeat": "week"},
        {"name": "Miriam", "message": get_pod(), "send_time": "","repeat": "day"},

    ]

    def fun(planned_messages):
        for item in planned_messages:

            if allow_to_send(item["name"], item["message"].replace('\n', ' '), item["send_time"], item["repeat"]):
                change_contact(item["name"])
                with open("C:\\Users\\lecke\\.vscode\\python\\whatsappbbot\\log.txt", "a") as file:
                    file.write(f"{datetime.datetime.now()},{item['name']},{item['message'].replace('\n', ' ')}\n")
                print(f"Sending message to [{item["name"]}]")
                send_message(item["message"])

            else:
                print(f"No message sent to {item['name']}")

    fun(planned_messages)
    time.sleep(1)
    driver.quit()

if datetime.datetime.now().hour >= 1: test()
else: print("No message send, to early.")

#except Exception as e:
    #log_error(str(e))
