"""Οι συναρτήσεις enumerate() και zip() σε Python."""


names = ["Άννα", "Βασίλης", "Γιώργος"]  # tuples ενός immutable τύπου δεδομένων
grades = [85, 92, 78]  # λίστα ενός mutable τύπου δεδομένων


def main() -> None:
    """Εκτυπώνει τα ονόματα και τις βαθμολογίες των μαθητών."""

    for index, name in enumerate(names, start=1):  # [(0, "Άννα"), (1, "Βασίλης"), (2, "Γιώργος")]
        print(f"{index}. {name}: {name}")


    for name, grade in zip(names, grades, strict=True):  # [("Άννα", 85), ("Βασίλης", 92), ("Γιώργος", 78)]
        print(f"{name}: {grade}")

if __name__ == "__main__":
    main()