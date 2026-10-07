import math
import pytest

from triangle import classify_triangle

# Test that a triangle with all sides equal is classified as Equilateral


def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"


# Test a triangle with exactly 2 sides equal is classified as Isosceles
def test_isosceles_triangle():
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(3, 4, 3) == "Isosceles"
    assert classify_triangle(4, 3, 3) == "Isosceles"

# Test that a triangle with all sides different is classified as Scalene


def test_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 4, 3) == "Right Scalene"
    assert classify_triangle(4, 5, 3) == "Right Scalene"
    assert classify_triangle(2, 3, 4) == "Scalene"

# Test invalid triangles, including non positive side lengths and violations of the triangle inequality


def test_invalid_triangles():
    assert classify_triangle(0, 1, 1) == "Invalid"
    assert classify_triangle(-1, 1, 1) == "Invalid"
    assert classify_triangle(1, -1, 1) == "Invalid"
    assert classify_triangle(1, 1, -1) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(2, 3, 5) == "Invalid"
    assert classify_triangle(3, 5, 2) == "Invalid"

# Test a right triangle with non integer side lengths


def test_right_triangle_non_integer():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
