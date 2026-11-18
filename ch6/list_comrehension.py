"""List comprehensions are a concise way to create lists in Python."""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["alice", "bob", "charlie", "david", "eve"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# map
squared_nums = [num ** 2 for num in nums]  # squares each number in nums
str_nums = [str(num) for num in nums]  # converts each number in nums to a string


# filtering
even_nums = [num for num in nums if num % 2 == 0]  # filters even numbers from nums
even_odd = ["even" if num % 2 == 0 else "odd" for num in nums]  # labels each number as even or odd


lazy = (num ** 2 for num in nums)  # generator expression, lazy evaluation