"""Demo of Python dictionaries."""

empty_dict = {}
grades = { "Alice": 90, "Bob": 45, "Charlie": 92 }

alice_grade = grades["Alice"]  # gets Alice's grade

# upsert
grades["Alice"] = 95  # updates Alice's grade
grades["David"] = 88  # inserts a new entry for David

# iterate over items
for name, grade in grades.items():      # returns [ (name, grade) ] for each iteration
    print(f"{name}: {grade}")

# iterate over keys
for name in grades.keys():              # returns [ name ] for each iteration
    print(f"{name}: {grades[name]}")

# iterate over values
for grade in grades.values():           # returns [ grade ] for each iteration
    print(f"Grade: {grade}")


passed = { name: grade for name, grade in grades.items() if grade >= 50 }  # returns a new dict with only passed students