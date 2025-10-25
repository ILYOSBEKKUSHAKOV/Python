#1
fruits = ["apple", "banana", "strawberry", "grapes", "cherry"]
print(fruits[2])

#2
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
combined_list = list1 + list2
print(combined_list)

#3
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
middle_index = len(numbers) // 2
new_list = [numbers[0], numbers[middle_index], numbers[-1]]
print(new_list)

#4
favourite_movies = ["The Dark  Knight", "Aquaman", "The Game of Thrones", "The Originals", "Doctor who"]
movies_tuple = tuple(favourite_movies)
print(movies_tuple)

#5
cities = ["Paris", "London", "New York", "Tokyo", "Riga"]
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")
    
#6
numbers1 = [12, 13, 14, 15, 16]
duplucated_list = numbers1*2
print(duplucated_list)

#7
numbers2 = [123, 124, 125, 126, 127]
numbers2[0], numbers2[-1] = numbers2[-1], numbers2[0]
print(numbers2)

#8
numbers3 = tuple(range(1,11))
print(numbers3[3:8])

#9
colours = ["blue", "red", "yellow", "blue", "orange"]
count_blue = colours.count("blue")
print(f"The colour 'blue' appears {count_blue} times")

#10
animals = ["tiger", "rabbit", "elefant", "horse", "lion"]
lion_index = animals.index("lion")
print("The index of 'lion' is : ", lion_index)

#11
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

#12
my_list = (123, 12, 33, 45, 66, 77)
my_tuple = (12, 11, 22, 44, 55)
print("Length of the list", len(my_list))
print("Length of the tuple", len(my_tuple))

#13
numbers_tuple = (22, 44, 66, 88)
numbers_list = list(numbers_tuple)
print(numbers_list)

#14
number1 = (12, 32, 4, 44, 99)
min_value = min(number1)
max_value = max(number1)
print("Minimum value is: ", min_value)
print("Maximum value is: ", max_value)

#15
words = ("apple", "cherry", "pears", "peach", "grapes")
print(words[::-1])
