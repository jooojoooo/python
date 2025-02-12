import datetime

def last_message_was_yesterday(contact_name, message):
    try:
        with open("log.txt", "r") as file:
            lines = file.readlines()

        for line in reversed(lines):
            parts = line.strip().split(',', 2)

            if len(parts) < 3:
                continue  # Skip lines that don't have enough values

            log_date, name, log_message = parts
            log_date = datetime.datetime.strptime(log_date, "%Y-%m-%d %H:%M:%S.%f")

            after10 = (datetime.datetime.now().hour >= 10) 

            if after10 and name == contact_name and log_message == message:
                return (datetime.datetime.now() - log_date).days >= 1
            
        return True
    except FileNotFoundError:
        return True
    
last_message_was_yesterday("Jonas","something else")
last_message_was_yesterday("Jonas","poem_of_the_day")