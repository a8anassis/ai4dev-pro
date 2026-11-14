"""Υπολογισμός παραγοντικού αριθμού με επαναληπτική μέθοδο.

n! = 1 * 2 * 3 * ... * n
"""
from pip._internal.req import req_uninstall

from ch1.data_types import result


def factorial(n: int) -> int:
    """Υπολογίζει το παραγοντικό ενός αριθμού n.

    Args:
        n (int): Ο αριθμός για τον οποίο θέλουμε να υπολογίσουμε το παραγοντικό.

    Returns:
        int: Το παραγοντικό του αριθμού n.
    """

    # Data input
    total_result = 1
    i = 1

    # Data Processing
    while i <= n:
        total_result *= i     # total_result = total_result * i
        i += 1

    return total_result

if __name__ == "__main__":
    num = int(input("Εισάγετε έναν ακέραιο αριθμό για τον υπολογισμό του παραγοντικού: "))

    total = factorial(num)

    print(f"Το παραγοντικό του {num} είναι: {total}")
