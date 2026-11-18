"""Demo of Python lists."""

my_list = []
my_list2 = [0] * 3
my_list3 = [1, 2, 3, 4, 5, 3, 3]

list3_size = len(my_list3)

# traverse
for i in range(len(my_list3)):          # lazy evaluation of len(my_list3) in each iteration
    print(my_list3[i])                  # IndexError if i >= len(my_list3)


for el in my_list3:                        # for-each loop
    print(el)


for i, el in enumerate(my_list3):          # returns a tuple (index, element) for each iteration
    print(f"Index: {i}, Element: {el}")


# append
my_list3.append(6)                         # adds 6 to the end of the list

# insert
my_list3.insert(0, 5)                      # adds 5 at index 0

# remove
my_list3.remove(3)                         # removes the first occurrence of 3

# search
if 4 in my_list3:               # like equals operator (==) for each element in the list
    print("4 is in the list")

# pythonic way to check if an element is in the list
try:
    index = my_list3.index(4)                 # returns the index of the first occurrence of 4
except ValueError:
    index = -1

# update
my_list3[0] = 10                          # updates the element at index 0 to 10


# remove multiple elements from a list using list comprehension
# traverse in reverse order to avoid index shifting issues
for i in range(len(my_list3) - 1, -1, -1):  # iterate backwards to avoid index shifting issues
    if my_list3[i] == 3:
        del my_list3[i]

my_deleted_filtered_list = [el for el in my_list3 if el != 3]   # returns a new list with all elements except 3

# Slicing
lst = [10, 20, 30, 40, 50]
my_list4 = my_list3[1:3]                   # [20, 30]
my_list5 = my_list3[:2]                    # [10, 20]
my_list6 = my_list3[::2]                  # [10, 30, 50]
reversed_lst = my_list3[::-1]                 # [50, 40, 30, 20, 10]

