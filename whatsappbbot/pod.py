import requests
from bs4 import BeautifulSoup

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

poem_of_the_day =f"""
*{title}* 

{text}

By _{author}_
""" 
