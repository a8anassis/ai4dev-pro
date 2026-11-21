"""Προκλήσεις και αλγόριθμοι στην Python για την επίλυση προβλημάτων."""


# Armstrong Number Challenge. Ένας Armstrong αριθμός είναι ένας αριθμός που ισούται με το άθροισμα των ψηφίων του,
# καθένα υψωμένο στη δύναμη του αριθμού των ψηφίων.
# Για παράδειγμα, 153 είναι ένας Armstrong αριθμός, επειδή 1^3 + 5^3 + 3^3 = 153.

def is_armstrong_number(num: int) -> bool:
    """Ελέγχει αν ένας αριθμός είναι Armstrong αριθμός."""
    num_str = str(num)
    num_digits = len(num_str)
    return num == sum(int(digit) ** num_digits for digit in num_str)


# Εναλλάσσει το case των χαρακτήρων σε μια συμβολοσειρά.
# Για παράδειγμα, "Hello World" γίνεται "hELLO wORLD".
def swap_case(s: str) -> str:
    """Εναλλάσσει το case των χαρακτήρων σε μια συμβολοσειρά."""
    # return s.swapcase()
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

# Επαναλαμβάνει μια συμβολοσειρά n φορές.
def repeat_text(text: str, n: int) -> str:
    """Επαναλαμβάνει μια συμβολοσειρά n φορές."""
    return text * n