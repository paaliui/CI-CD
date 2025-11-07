import math

def _validate_triangle(a: float, b: float, c: float) -> None:
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError("sides must be numbers")
        if x <= 0:
            raise ValueError("sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("triangle inequality violated")

def triangle_perimeter(a: float, b: float, c: float) -> float:
    _validate_triangle(a, b, c)
    return a + b + c

def triangle_area(a: float, b: float, c: float) -> float:
    _validate_triangle(a, b, c)
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
