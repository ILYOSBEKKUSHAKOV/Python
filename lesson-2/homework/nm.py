#1
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
from datetime import date 
current_year = date.today().year
age = current_year - year_of_birth
print(f"Hello, {name}! You are {age} years old in {current_year}")

#2
txt = 'LMaasleitbtui'
car_names = ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi', 'Mitsubishi', 'Tesla', 'Nissan', 'Kia', 'Hyundai',
             'Peugeot', 'Fiat', 'Chevrolet', 'Subaru']

found = [car for car in car_names if all(ch.lower() in txt.lower() for ch in car.lower())]
print(found)

#3
txt = 'MsaatmiazD'
car_names = ['Toyota','Honda', 'Ford', 'BMW', 'Audi', 'Mitsubishi', 'Tesla', 'Nissan', 'Kia', 'Hyundai',
              'Peugeot', 'Fiat', 'Chevrolet', 'Subaru','Mazda']

found = [car for car in car_names if all(ch.lower() in txt.lower() for ch in car.lower())]
print(found)

#4
import re

txt = "I'am John. I am from London"
match = re.search(r'from ([A-Za-z ]+)', txt)

if match:
    residence = match.group(1).strip()
    print("Residence area:", residence)
else:
    print("Residence area not found.")

#5
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

#6
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

#7
numbers = input("Enter numbers seperated by spaces: ")
num_list = [float(x) for x in numbers.split()]
max_value = max(num_list)
print("The maximum value is: ", max_value)

#8
word = input("Enter a word: ")
word = word.lower()
if word == word[::-1]:
   print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

#9
email = input("Enter an email address: ")

if "@" in email:
    domain = email.split('@')[1]
    print("Domain:", domain)
else:
    print("Invalid email address.Please include '@'.")

#10
import random
import string
length = int(input("Enter the desired password length: "))
character = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(character) for _ in range(length))
print("Generate password: ", password)

