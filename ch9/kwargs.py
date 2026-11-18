"""Demo για χρήση των kwargs. varkwargs."""


def build_profile(firstname: str, lastname: str, **kwargs) -> dict:
    """Δημιουργεί ένα λεξικό με τα στοιχεία του προφίλ."""
    profile = {"firstname": firstname, "lastname": lastname}

    for key, value in kwargs.items():
        profile[key] = value

    return profile

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""

    user_profile = build_profile("Alice", "Smith", age=30, city="Athens", profession="Engineer")

    profile = build_profile(**user_profile)

    print(profile)


if __name__ == "__main__":
    main()

