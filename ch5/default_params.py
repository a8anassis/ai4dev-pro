"""Παράδειγμα με default params"""


def say_hello(name = "World") -> None:
    """Λέει γεια"""
    print(f"Hello, {name}!")

def main() -> None:
    """Κύρια συνάρτηση"""
    say_hello()
    say_hello("Alice")

if __name__ == "__main__":
    main()