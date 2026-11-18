"""Exceptions demo."""


try:
    num = int("abc")
except ValueError:
    print("Σφάλμα: Μη έγκυρη είσοδος.")


try:
    result = "aueb" / 7
except TypeError:
    print("Σφάλμα: Μη έγκυρος τύπος δεδομένων για διαίρεση.")


try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except OSError:
    print("Σφάλμα: Το αρχείο δεν βρέθηκε.")