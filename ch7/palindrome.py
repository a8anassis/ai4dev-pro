"""Check if a string is a palindrome.

Για παράδειγμα το abcba είναι palindrome, ενώ το abcd δεν είναι.
"""

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == s[::-1]     # Check if the string is equal to its reverse