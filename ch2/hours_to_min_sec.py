"""Μετατροπή ωρών σε λεπτά."""

MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60


def main() -> None:
    """Μετατροπή ωρών σε λεπτά και δευτερόλεπτα."""

    # Data input
    hours = int(input("Εισάγετε τον αριθμό των ωρών: "))

    # Data Processing
    minutes = hours * MINUTES_PER_HOUR
    seconds = minutes * SECONDS_PER_MINUTE

    # Εκτύπωση αποτελεσμάτων
    # print(hours, "ώρες ισούνται με", minutes, "λεπτά ή", seconds, "δευτερόλεπτα.")
    # print(str(hours) + " ώρες ισούνται με " + str(minutes) + " λεπτά ή " + str(seconds) + " δευτερόλεπτα.")
    print(f"{hours} ώρες ισούνται με {minutes} λεπτά ή {seconds} δευτερόλεπτα.")


if __name__ == "__main__":
    main()