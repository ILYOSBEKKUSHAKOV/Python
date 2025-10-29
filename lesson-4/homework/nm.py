#1
my_dict = {'London': 3, 'Los Vegas': 10, 'Los Angeles': 7, 'New Yourk': 2}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original dictionary: ", my_dict)
print("Sorted in Ascending Order by Value: ", ascending)
print("Sorted in Descending Order by Value: ", descending)
#2
our_dict = {0: 10, 1: 20}
our_dict[2] = 30
print("Updated dictionary: ", our_dict)
#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dict = dic1 | dic2 | dic3 
print("Concatenated dictionary: ",concatenated_dict) 
#4
n = int(input("Enter a number: "))
result = {x: x*x for x in range(1, n+1)}
print (result)
#5
square_dict = {}
for x in range(1,16):
  square_dict[x] = x*x
print(square_dict)
#Set exercises
#1
my_set = {1, 2, 3, 4, 5}
print("Created set:", my_set)
#2 iterate (loop) over a set.
my_set = {1, 2, 3, 4, 5}
print("Elements in the set:")
for item in my_set:
    print(item)
#3
my_set = {11, 12, 13}
print("Original set:", my_set)
my_set.add(14)
print("After adding one ele,ent(14):", my_set)
my_set.update([15, 16, 17])
print("After adding multiple elements:", my_set)
#4
my_set1 = {1, 2, 3, 4, 5}
print("Original set:", my_set1)
my_set1.remove(3)
print("After removing (3) with remove:", my_set1)
my_set1.discard(4)
print("After discarding (4) with discatd:", my_set1)
my_set1.discard(10)
print("After discarding (10) with discatd:", my_set1)
removed_item = my_set1.pop()
print("Removed item using pop:", removed_item)
print("After pop operation:", my_set1)
my_set1.clear()
print("After using clear:", my_set1)
#5
my_set2 = {1, 2, 3, 4, 5}
print("Original set:", my_set2)
element = 4
if element in my_set2:
    my_set2.remove(element)
    print(f"Element {element} removed successfully.")
else:
    print(f"Element {element} not found in the set.")
    
print("Updated set: ", my_set2) 
