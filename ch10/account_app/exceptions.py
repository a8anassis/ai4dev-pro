"""Custom exceptions for the account app."""


class AccountError(Exception):
    """Base class for account-related exceptions."""

class NegativeAmountError(AccountError):
    """Raised when a negative amount is provided for a transaction."""

class InsufficientBalanceError(AccountError):
    """Raised when an account has insufficient balance for a transaction."""


class SsnMismatchError(AccountError):
    """Raised when the provided SSN does not match the account's SSN."""


