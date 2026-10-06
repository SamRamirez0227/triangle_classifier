from math import isclose


def is_valid_triangle(a, b, c) -> bool:
    """Return whether three side lengths form a non-degenerate triangle."""
    return (
        a > 0
        and b > 0
        and c > 0
        and a + b > c
        and a + c > b
        and b + c > a
    )


def classify_triangle(a, b, c) -> str:
    """Classify valid triangle side lengths, or return "Invalid"."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        classification = "Equilateral"
    elif a == b or a == c or b == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    first_leg, second_leg, hypotenuse = sorted((a, b, c))
    if isclose(
        first_leg**2 + second_leg**2,
        hypotenuse**2,
        rel_tol=1e-9,
        abs_tol=1e-9,
    ):
        return f"Right {classification}"
    return classification
