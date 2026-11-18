"""Χειρίζεται την εξαίρεση ZeroDivisionError."""

import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)

def div(a: int, b: int) -> int | None:
    """Διαιρεί τον αριθμό a με τον αριθμό b.

    Args:
        a (int): Ο αριθμός που θα διαιρεθεί.
        b (int): Ο αριθμός με τον οποίο θα διαιρεθεί ο αριθμός a.

    Returns:
        int | None: Το αποτέλεσμα της διαίρεσης a / b ή None σε περίπτωση σφάλματος.
    """
    try:
        result = a // b
    except ZeroDivisionError:
        logger.error("Σφάλμα: Προσπάθεια διαίρεσης με το μηδέν.")
        raise # rethrow the exception to the caller


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    try:
        a = int(input("Εισάγετε τον αριθμό a: "))
        b = int(input("Εισάγετε τον αριθμό b: "))

        result = div(a, b)
    except ZeroDivisionError:
        print("Η διαίρεση απέτυχε λόγω μηδενικού διαιρέτη.")

    if result is not None:
        print(f"Το αποτέλεσμα της διαίρεσης {a} / {b} είναι: {result}")
