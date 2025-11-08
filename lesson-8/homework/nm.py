try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("Error: Division by Zero is now allowed!")
Error: Division by Zero is now allowed!
try:
    num = input("Enter an integer: ")
    if not num.isdigit() and not (num.startswith('-') and num[1:].isdigit()):
        raise ValueError("Invalid input! Not an integer.")
    print("You entered:", int(num))
except ValueError as e:
    print("Error:", e)
Error: Invalid input! Not an integer.
try:
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
Error: The file does not exist.
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Both inputs must be numbers.")
    result = float(a) + float(b)
    print("Sum:", result)
except TypeError as e:
    print("Error:", e)
Error: Both inputs must be numbers.
try:
    file_name = input("Enter file name to open: ")
    with open(file_name, 'w') as file:
        file.write("Testing permission handling.")
except PermissionError:
    print("Error: You don't have permission to access this file.")
try:
    numbers = [10, 20, 30]
    index = int(input("Enter index to access (0-2): "))
    print("Number at index:", numbers[index])
except IndexError:
    print("Enter: Index out of range.")
Enter: Index out of range.
try:
    num = input("Enter a number (Ctrl+c to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nError: Input cancelled by user.")
You entered: 123
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ArithmeticError:
    print("Error: An arithmetric error occured.")
Result: 0.0
try:
    file_name = input("Enter file name: ")
    with open(file_name, 'r', encoding='ascii') as file:
        print(file.read())
except UnicodeDecodeError:
    print("Error: Unable to decode file (encoding issue).")
try:
    my_list = [1, 2, 3]
    my_list.push()
except AttributeError:
    print("Error: The list object has no such attribute.")
Error: The list object has no such attribute.
with open("sample.txt", "r") as f:
    print(f.read())
n = int(input("Enter number of lines to read: "))
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")
text = input("Enter text to append: ")
with open("sample.txt", "a") as f:
    f.write("\n" + text)

with open("sample.txt", "r") as f:
    print(f.read())
asa
n = int(input("Enter number of lines to read from end: "))
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)
with open("sample.txt", "r") as f:
    content = f.read()
print(content)
with open("sample.txt", "r") as f:
    arr = [line.strip() for line in f]
print(arr)
with open("sample.txt", "r") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
with open("sample.txt", "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))
from collections import Counter

with open("sample.txt", "r") as f:
    words = f.read().split()
freq = Counter(words)
print(freq)
import os

file_path = "sample.txt"
print("File size:", os.path.getsize(file_path), "bytes")
data = ["Apple", "Banana", "Cherry"]
with open("fruits.txt", "w") as f:
    for item in data:
        f.write(item + "\n")
with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())
import random

with open("sample.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines))
f = open("sample.txt", "r")
print("File closed?", f.closed)
f.close()
print("File closed after closing?", f.closed)
f = open("sample.txt", "r")
print("File closed?", f.closed)
f.close()
print("File closed after closing?", f.closed)
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
with open("sample.txt", "r") as f:
    text = f.read().replace(",", " ")
    words = text.split()
print("Number of words:", len(words))
import glob

char_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as f:
        char_list.extend(list(f.read()))
print(char_list)
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")
import string

n = int(input("Enter number of letters per line: "))
letters = string.ascii_uppercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write(" ".join(letters[i:i+n]) + "\n")
