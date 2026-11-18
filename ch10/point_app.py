"""Data classes για την αναπαράσταση σημείων σε 2D χώρο."""

class Point:
    """Αναπαριστά ένα σημείο σε 2D χώρο με συντεταγμένες x και y."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point(x={self.x!r}, y={self.y!r})"


def main() -> None:
    """Κύρια συνάρτηση για τη δημιουργία και εμφάνιση σημείων."""
    point1 = Point(1.0, 2.0)
    point2 = Point(3.5, 4.5)

    print(f"Σημείο 1: {point1}")
    print(f"Σημείο 2: {point2}")