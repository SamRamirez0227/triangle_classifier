from triangle import classify_triangle


def test_stained_glass_triangle_classification():
    # A valid triangle should return its shape.
    assert classify_triangle(4, 4, 6) == "Isosceles"

    # An invalid triangle should return Invalid without crashing.
    assert classify_triangle(1, 2, 3) == "Invalid"

    # A right-angle piece should be clearly flagged as Right.
    assert classify_triangle(3, 4, 5) == "Right Scalene"
