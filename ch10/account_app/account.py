"""Demo of Python account application."""

from decimal import Decimal

from ch10.account_app.exceptions import NegativeAmountError, SsnMismatchError, InsufficientBalanceError


class Account:
    """A simple bank account class."""

    def __init__(self, id: int, iban: str, firstname: str, lastname: str, ssn:str, balance: Decimal):
        """Initialize the account with an ID, IBAN, owner's name, and balance."""
        self.id = id
        self.iban = iban
        self.owner = f"{firstname} {lastname}"
        self.ssn = ssn
        self.balance = balance


    def deposit(self, amount: Decimal) -> None:
        """Deposit a specified amount into the account."""
        try:
            if amount <= 0:
                raise NegativeAmountError("Deposit amount must be positive.")
            self.balance += amount
        except NegativeAmountError as e:
            print(e)    # logging the error message
            raise


    def withdraw(self, amount: Decimal, ssn: str) -> None:
        """Withdraw a specified amount from the account."""
        try:
            if amount <= 0:
                raise NegativeAmountError("Withdrawal amount must be positive.")
            if ssn != self.ssn:
                raise SsnMismatchError("SSN does not match the account owner.")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient funds for this withdrawal.")
            self.balance -= amount
        except (NegativeAmountError, SsnMismatchError, InsufficientBalanceError) as e:
            print(e)  # logging the error message
            raise

def main() -> None:
    """Main function to demonstrate the Account class."""
    account = Account(id=1, iban="GR12345678901234567890", firstname="John", lastname="Doe", ssn="123-45-6789", balance=Decimal("1000.00"))

    print(f"Account created for {account.owner} with IBAN {account.iban} and initial balance {account.balance}.")

    # Demonstrate deposit
    try:
        account.deposit(Decimal("200.00"))
        print(f"Deposited 200.00. New balance: {account.balance}.")
    except NegativeAmountError:
        pass

    # Demonstrate withdrawal
    try:
        account.withdraw(Decimal("150.00"), "123-45-6789")
        print(f"Withdrew 150.00. New balance: {account.balance}.")
    except (NegativeAmountError, SsnMismatchError, InsufficientBalanceError):
        pass


if __name__ == "__main__":
    main()