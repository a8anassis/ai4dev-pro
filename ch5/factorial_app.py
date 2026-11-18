"""Υπολογισμός παραγοντικού ενός αριθμού.

n! = 1 * 2 * 3 * ... * n
"""

def factorial(n: int) -> int:
    """Υπολογίζει το παραγοντικό ενός αριθμού n.

    Args:
        n (int): Ο αριθμός για τον οποίο θέλουμε να υπολογίσουμε το παραγοντικό.

    Returns:
        int: Το παραγοντικό του αριθμού n.
    """
    total_result = 1

    for i in range(1, n + 1):
        total_result *= i           # total_result = total_result * i

    return total_result


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""

    num = int(input("Εισάγετε έναν ακέραιο αριθμό για τον υπολογισμό του παραγοντικού: "))

    # Delegation design pattern
    total = factorial(num)

    print(f"Το παραγοντικό του {num} είναι: {total}")


if __name__ == "__main__":
    main()