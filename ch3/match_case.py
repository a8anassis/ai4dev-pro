"""Χρήση της match-case σε Python για την επιλογή ενός είδους από ένα μενού."""

EXIT_CHOICE = "4"

def decide_on_choice(choice: str) -> str:
    """Επιστρέφει ένα μήνυμα ανάλογα με την επιλογή του χρήστη."""
    match choice:
        case "1":
            return "Κατάθεση."
        case "2":
            return "Ανάληψη."
        case "3":
            return "Υπόλοιπο."
        case "4":
            return "Έξοδος."
        case _:
            return "Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε 1, 2, 3 ή 4."

    # Alternative using if-elif-else:
    # if choice == "1":
    #     return "Κατάθεση."
    # elif choice == "2":
    #     return "Ανάληψη."
    # elif choice == "3":
    #     return "Υπόλοιπο."
    # elif choice == "4":
    #     return "Έξοδος."
    # else:
    #     return "Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε 1, 2, 3 ή 4."


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""

    while True:

        # Data input
        print("\nΠαρακαλώ επιλέξτε μία από τις παρακάτω επιλογές:")
        print("1. Κατάθεση")
        print("2. Ανάληψη")
        print("3. Υπόλοιπο")
        print("4. Έξοδος")

        user_choice = input("Εισάγετε τον αριθμό της επιλογής σας: ")

        # Validation
        if user_choice == EXIT_CHOICE:
            print("Έξοδος από το πρόγραμμα.")
            break

        # Processing
        result_message = decide_on_choice(user_choice)

        # Output
        print(result_message)


if  __name__ == "__main__":
    main()