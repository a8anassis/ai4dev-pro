"""Split and join strings and lists."""


line = "This is a sample line of text."
tokens = line.split()  # splits the string into a list of words using whitespace as the delimiter
print(tokens)  # ['This', 'is', 'a', 'sample', 'line', 'of', 'text.']


# join a list of strings into a single string with a space as the delimiter
joined_line = " ".join(tokens)
print(joined_line)  # This is a sample line of text.