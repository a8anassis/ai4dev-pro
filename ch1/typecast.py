"""Παραδείγματα μετατροπής τύπων δεδομένων σε Python."""
from os import truncate

num1 = int("32")
num2 = float("32.5")
str_num = str(32)
truncated_num = int(3.99)       # Ακέραιος αριθμός (αποκοπή δεκαδικών) - απώλεια πληροφορίας

# Παράδειγμα μετατροπής τύπων δεδομένων
result = "Coding" + 7       # TypeError: δεν μπορεί να προστεθεί συμβολοσειρά και ακέραιος αριθμός
result2 = 5 + 3.5           # int -> float, αποτέλεσμα: 8.5


# Μετατροπές με boolean τιμές
# 0 0.0 "", None, [], {} -> False
# Όλα τα υπόλοιπα -> True
bool1 = bool(0)          # False
bool2 = bool(1)          # True
bool3 = bool("")         # False
bool4 = bool("Hello")    # True
bool5 = bool(None)         # False