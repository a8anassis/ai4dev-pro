"""Υπολογισμός της δύναμης ενός αριθμού σε Python.

Για παράδειγμα, 2^10 = 1024
"""


def power(base: int, exponent: int) -> int:
    """Υπολογίζει τη δύναμη ενός αριθμού.

    Args:
        base (int): Η βάση.
        exponent (int): Ο εκθέτης.

    Returns:
        int: Το αποτέλεσμα της δύναμης.
    """
    # return base ** exponent  # base raised to the power of exponent:

    result = 1

    for _ in range(exponent):
        result *= base  # result = result * base

    return result


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""

    base = int(input("Εισάγετε τη βάση (base): "))
    exponent = int(input("Εισάγετε τον εκθέτη (exponent): "))

    result = power(base, exponent)

    print(f"{base}^{exponent} = {result}")


if __name__ == "__main__":
    main()