#1
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(2000))

#2
def check_weirdness(n):
    if not (1 <= n <= 100):
        print("Number must be between 1 and 100.")
        return

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


n = int(input("Enter a number between 1 and 100: "))
check_weirdness(n)

#3
def even_numbers_with_if(a, b):
    if a > b:
        a, b = b, a  

    if a % 2 != 0:
        a += 1  

    return list(range(a, b + 1, 2))

print(even_numbers_with_if(3, 10))  
print(even_numbers_with_if(10, 3))  

def even_numbers_no_if(a, b):
    a, b = min(a, b), max(a, b)  
    start = a + (a % 2)         
    return list(range(start, b + 1, 2))
print(even_numbers_no_if(3, 10))  
print(even_numbers_no_if(10, 3)) 
