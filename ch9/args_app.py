"""Demo για χρήση των args. varargs.

Oveloading functions in Python is not supported,
but we can use *args and **kwargs to achieve similar functionality.
"""

def total(*nums):
    """Υπολογίζει το άθροισμα όλων των αριθμών που δίνονται ως args."""
    return sum(nums)    # tuple


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του demo."""
    result1 = total(1, 2, 3, 4, 5)
    result2 = total(10, 20, 30)
    result3 = total(100, 200, 300, 400, 500)
    print(f"Τα αθροίσματα είναι: {result1}, {result2}, {result3}")

