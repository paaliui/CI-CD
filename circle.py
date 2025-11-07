import math

def _validate_radius(r: float) -> None:
    if not isinstance(r, (int, float)):
        raise TypeError("radius must be a number")
    if r < 0:
        raise ValueError("radius must be non-negative")

def circle_area(r: float) -> float:
    """Площадь круга: π r^2."""
    _validate_radius(r)
    return math.pi * (r ** 2)

def circle_circumference(r: float) -> float:
    """Длина окружности: 2 π r."""
    _validate_radius(r)
    return 2 * math.pi * r
