"""Data classes για την αναπαράσταση σημείων σε 2D χώρο."""


from dataclasses import dataclass


@dataclass
class Point:
    """Αναπαριστά ένα σημείο σε 2D χώρο με συντεταγμένες x και y."""
    x: int
    y: int

if __name__ == "__main__":
    # Δημιουργία ενός σημείου
    point1 = Point(3, 4)
    print(f"Σημείο 1: {point1}")

    # Δημιουργία ενός άλλου σημείου
    point2 = Point(7, 1)
    print(f"Σημείο 2: {point2}")



