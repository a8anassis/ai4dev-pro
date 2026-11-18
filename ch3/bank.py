"""Ανάληψη από ATM.

Validation: Το ποσό πρέπει να είναι θετικός ακέραιος και πολλαπλάσιο του NOTE.
Business logic: Ελέγχει αν το ποσό είναι μικρότερο ή ίσο με το υπόλοιπο.

"""

EXIT_OPTION = 0
NOTE = 20
INITIAL_BALANCE = 1000


def main() -> None:
    """Εκτελεί ανάληψη από ATM και εμφανίζει το υπόλοιπο μετά την ανάληψη."""
    balance = INITIAL_BALANCE

    while True:
        print(f"Μπορείτε να κάνετε ανάληψη σε πολλαπλάσια των {NOTE}€.")
        print(f"Επιλέξτε {EXIT_OPTION} για έξοδο.")

        # Data input
        amount = int(input("Εισάγετε το ποσό που θέλετε να αναλάβετε: "))

        # Validation
        if amount == EXIT_OPTION:
            print("Έξοδος από το πρόγραμμα.")
            break

        if amount < 0:
            print(f"Παρακαλώ εισάγετε ένα θετικό ποσό.")
            continue

        if amount % NOTE != 0:
            print(f"Παρακαλώ εισάγετε ένα ποσό που είναι πολλαπλάσιο του {NOTE}\u20AC.")
            continue

        if amount > balance:
            print("Δεν έχετε αρκετό υπόλοιπο για αυτή την ανάληψη.")
            continue

        # Happy path: Update balance and print success message
        balance -= amount

        # Output
        print(f"Η ανάληψη των {amount}\u20AC ήταν επιτυχής. Το νέο υπόλοιπο είναι: {balance}\u20AC")


if __name__ == "__main__":
    main()