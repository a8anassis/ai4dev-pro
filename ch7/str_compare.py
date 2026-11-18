"""Comparing strings in Python."""


str1 = "Andrew"
str2 = "andrew"

are_equal = str1 == str2    # False, because the comparison is case-sensitive

# Normalizing strings to uppercase for comparison
are_equal_normalized = str1.upper() == str2.upper()  # True, case is ignored


# inequality comparisons 'A' < 'a' because of ASCII ordinal values are 'A' = 65 and 'a' = 97
is_less_than = str1 < str2      # True, because "A" comes before "a" in ASCII values
is_greater_than = str1 > str2   # False