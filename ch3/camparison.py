"""Τελεστές σύγκρισης και λογικοί τελεστές σε Python."""

MIN_GRADE = 50
MAX_GRADE = 100


def is_passing(grade: int) -> bool:
    """Επιστρέφει True αν η βαθμολογία είναι μεταξύ 50-100, αλλιώς επιστρέφει False."""
    return MIN_GRADE <= grade <= MAX_GRADE  # grade >= MIN_GRADE and grade <= MAX_GRADE