import numpy as np

original_list = [12.23, 13.32, 100, 36.32]

array_1d = np.array(original_list)

print("Original List:", original_list)
print("One-dimensional NumPy array:", array_1d)

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)

import numpy as np

vector = np.zeros(10)
print(vector)

vector[6] = 11
print("Update sixth value to 11", vector)

import numpy as np

array = np.arange(12, 38)

print(array)


import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)

print("Array converted to float:", float_arr)


import numpy as np

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
print("Values in Centigrade degrees:", celsius)

fahrenheit = (celsius * 9 / 5) + 32
print("Values in Fahrenheit degrees:", fahrenheit)

fahrenheit2 = np.array([0., 12., 45.21, 34., 99.91, 32.])
print("Values in Fahrenheit degrees:", fahrenheit2)

celsius2 = (fahrenheit2 - 32) * 5 / 9
print("Values in Centigrade degrees:", celsius2)


import numpy as np

arr = np.array([10, 20, 30])
print("Original array:", arr)

arr_appended = np.append(arr, [40, 50, 60, 70, 80, 90])

print("After append values to the end of the array:", arr_appended)


import numpy as np

arr = np.random.rand(10)
print("Random array:", arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)


import numpy as np

array = np.random.rand(10, 10)
print("10x10 Random Array:\n", array)

min_value = np.min(array)
max_value = np.max(array)

print("\nMinimum value:", min_value)
print("Maximum value:", max_value)


import numpy as np

array = np.random.rand(3, 3, 3)

print("3x3x3 Random Array:\n", array)
