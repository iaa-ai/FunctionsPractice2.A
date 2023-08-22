def triangle_area(a, b, c) -> float:
    """
    Calculate the area of a triangle using Heron's formula.

    Args:
        a : The length of side a of the triangle.
        b : The length of side b of the triangle.
        c : The length of side c of the triangle.

    Returns:
        result: The calculated area of the triangle.
    """
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    result = area ** 0.5

    return result

sideA = 12
sideB = 23
sideC = 34
compute = triangle_area(sideA, sideB, sideC)

print("Triangle area:", compute)
