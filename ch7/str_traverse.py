"""Traversing strings in Python."""


def main() -> None:
    """Main function to demonstrate string traversal."""
    firstname = input("Enter your first name: ")

    # Traverse the string using a for loop
    for char in firstname:
        print(char, end="")


    if __name__ == "__main__":
        main()
