from datetime import datetime

birth_str = input("Tug'ilgan kuningizni kiriting (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d")

today = datetime.today()
age_days = (today - birth_date).days

years = age_days // 365
months = (age_days % 365) // 30
days = (age_days % 365) % 30

print(f"Yoshingiz: {years} yil, {months} oy, {days} kun")

from datetime import datetime

birth_str = input("Tug'ilgan kun (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d")

today = datetime.today()
next_birthday = datetime(today.year, birth_date.month, birth_date.day)

if next_birthday < today:
    next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)

days_left = (next_birthday - today).days

print(f"Keyingi tug'ilgan kungacha: {days_left} kun qoldi.")


from datetime import datetime, timedelta

current_str = input("Current time (YYYY-MM-DD HH:MM): ")
hours = int(input("Meeting duration (hours): "))
minutes = int(input("Meeting duration (munites): "))

current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
end_time = current_time + timedelta(hours=hours, minutes=minutes)

print("Meeting end time:", end_time)


from datetime import datetime
from zoneinfo import ZoneInfo

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
current_tz = input("Enter your current timezone (e.g., Asia/Tashkent): ")
target_tz = input("Enter the timezone to convert to (e.g., Europe/London): ")

dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
dt = dt.replace(tzinfo=ZoneInfo(current_tz))

converted = dt.astimezone(ZoneInfo(target_tz))

print("Converted time:", converted.strftime("%Y-%m-%d %H:%M %Z"))


from datetime import datetime
import time

target_str = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

print("\nCountdown started...\n")

while True:
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print("Time's up!")
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"\rTime remaining: {days}d {hours}h {minutes}m {seconds}s", end="")

    time.sleep(1)


import re

email = input("Enter an email address: ")

# Basic email pattern
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid email address ✔")
else:
    print("Invalid email address ✘")


phone = input("Enter a 10-digit phone number: ")

digits = "".join(filter(str.isdigit, phone))

if len(digits) == 10:
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    print("Formatted number:", formatted)
else:
    print("Invalid phone number. Please enter exactly 10 digits.")


import re

password = input("Enter your password: ")

min_length = 8
has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"\d", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Check all criteria
if len(password) < min_length:
    print("Weak: Password must be at least 8 characters long.")
elif not has_upper:
    print("Weak: Password must contain at least one uppercase letter.")
elif not has_lower:
    print("Weak: Password must contain at least one lowercase letter.")
elif not has_digit:
    print("Weak: Password must contain at least one digit.")
elif not has_special:
    print("Weak: Password should contain at least one special character (!@#$...).")
else:
    print("Strong password ✔")



text = """Python is a popular programming language. Many developers love Python because Python is versatile and easy to learn."""

word = input("Enter the word to find: ").strip()

text_lower = text.lower()
word_lower = word.lower()

positions = []
index = text_lower.find(word_lower)
while index != -1:
    positions.append(index)
    index = text_lower.find(word_lower, index + 1)

if positions:
    print(f"The word '{word}' was found {len(positions)} times at positions: {positions}")
else:
    print(f"The word '{word}' was not found in the text.")


import re

text = input("Enter a text containing dates: ")

date_patterns = [
    r"\b\d{2}/\d{2}/\d{4}\b",   
    r"\b\d{2}-\d{2}-\d{4}\b",   
    r"\b\d{4}-\d{2}-\d{2}\b"    
]

dates = []
for pattern in date_patterns:
    dates.extend(re.findall(pattern, text))

if dates:
    print("Dates found in the text:")
    for d in dates:
        print(d)
else:
    print("No dates found in the text.")


