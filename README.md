# triangle_classifier

An equilateral triangle has three equal angles, each measuring 60 degrees. Since a right triangle has a 90-degree angle, an equilateral triangle cannot also be right.

| Test | Copilot-suggested? | Kept/edited/rejected | Why |
|---|---|---|---|
| test_equilateral_triangle | Yes | Kept | Correctly tests three equal sides returning Equilateral. |
| test_isosceles_triangle | Yes | Kept | Correctly tests exactly two equal sides in all three input positions. |
| test_scalene_triangle | Yes | Kept | Correctly tests both right and non-right scalene triangles. |
| test_invalid_triangles | Yes | Kept | Correctly tests non-positive sides, triangle inequality failures, and the degenerate boundary case. |
| test_right_triangle_non_integer | Yes | Edited | Copilot generated a different right triangle; changed it to 5, 5, 5*sqrt(2) to cover the required non-integer right isosceles case. |

## Acceptance Criteria

1. When a customer enters three side lengths that form a valid triangle, the system returns the correct triangle classification.

2. When the entered side lengths do not form a valid triangle, the system returns "Invalid" without crashing.

3. When the entered sides form a right triangle, the returned classification begins with "Right" so the piece can be identified as requiring reinforced corners.

## Running the Tests

Install the required dependency:

pip install -r requirements.txt

Run all tests with:

pytest -v

## Equivalence Classes and Boundaries

The equivalence classes identified for the triangle classifier are:
- Invalid triangles
- Equilateral triangles
- Isosceles triangles
- Scalene triangles
- Right triangles

The main boundaries tested are side lengths less than or equal to zero and the triangle inequality. The degenerate boundary occurs when the sum of two sides equals the third side, such as (1, 2, 3), which must return "Invalid".

## AI-Use Disclosure

I used GitHub Copilot to assist with drafting the unit tests in `test_triangle.py`. I reviewed each suggestion against the assignment requirements and kept or edited the generated tests when necessary. In particular, I edited the non-integer right-triangle test to cover the required `5, 5, 5*sqrt(2)` case.

I also used ChatGPT to review my implementation and Copilot-generated tests, organize the README, and develop the acceptance criteria and acceptance test. I manually reviewed the code and ran the complete pytest test suite to verify that the implementation and tests worked correctly.