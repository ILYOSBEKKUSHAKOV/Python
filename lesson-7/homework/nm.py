def is_prime(n):
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))   # Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi. 
print(is_prime(7))  # Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.


def sum_of_digits(number):
    """Return the sum of digits of any integer number."""
    number = abs(number)  
    total = 0
    while number > 0:
        total += number % 10  
        number //= 10          
    return total

print(sum_of_digits(23))     # 5 (2 + 3)
print(sum_of_digits(456))    # 15 (4 + 5 + 6)
print(sum_of_digits(7890))   # 24 (7 + 8 + 9 + 0)


def powers_of_two_less_than(n):
    """Return a list of all powers of 2 less than n."""
    k = 1
    result = []
    while 2**k < n:
        result.append(2**k)
        k += 1
    return result

# Example usage
n = 10
print(powers_of_two_less_than(n))
