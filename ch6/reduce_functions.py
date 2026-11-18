"""Demonstration of reduce functions in Python."""


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["alice", "bob", "charlie", "david", "eve"]


# sum
sum_all = sum(x for x in nums)  # sums all numbers in nums
sum_even = sum(x for x in nums if x % 2 == 0)  # sums only even numbers in nums, generator expression for lazy evaluation

# min and max
min_value = min(nums)  # finds the minimum number in nums
max_value = max(nums)  # finds the maximum number in nums
min_even = min(x for x in nums if x % 2 == 0)  # finds the minimum even number in nums
max_even = max(x for x in nums if x % 2 == 0)  # finds the maximum even number in nums


# avg
avg_value = sum(nums) / len(nums)  # calculates the average of numbers in nums


# all() function checks if all elements in an iterable are True
all_positive = all(x > 0 for x in nums)  # checks if all numbers are positive

# any() function checks if any element in an iterable is True
any_even = any(x % 2 == 0 for x in nums)  # checks if there is any even number in nums