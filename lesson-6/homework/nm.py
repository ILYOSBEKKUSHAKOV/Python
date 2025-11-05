def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0

    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                if i + 1 < len(txt):
                    result.append(txt[i + 1])
                    result.append('_')
                    i += 1  
            else:
                if i != len(txt) - 1:
                    result.append('_')

            count = 0  
        i += 1

    if result and result[-1] == '_':
        result.pop()

    return ''.join(result)

text = "programmingisfun"
output = insert_underscores(text)
print(output)



n = int(input())
for i in range(n):
    print(i**2)



i=1
while i<=10:
    print(i)
    i+=1


n = 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print() 


n = int(input("Enter number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1

print("Sum is:", total)


num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num * i)
    i += 1


numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break  
    if num > 150:
        continue 
    if num % 5 == 0:
        print(num)

num = int(input("Enter a number: "))
count = len(str(num))
print("Number of digits:", count)


n = 5
for i in range(n, 0, -1):     
    for j in range(i, 0, -1): 
        print(j, end=' ')
    print() 


list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)


for i in range(-10,0):
    print(i)


for i in range(5):
        print(i)
print("Done!")


start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1: 
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


n = 10  
a, b = 0, 1  

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end='  ')
    a, b = b, a + b 

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! =", factorial)

list1 = [1, 1, 2]
list2 = [2, 3, 4]
result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(result)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(result)
