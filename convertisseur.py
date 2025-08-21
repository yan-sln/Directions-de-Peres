# -*- coding: utf-8 -*-
"""
Convert nested lists of floating-point approximations into exact symbolic values (SageMath).
"""

from sage.all import sqrt
from math import isclose

# Example list (triplets with rounded values)
liste = [
    [[1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
    [[1.0, 0.0, 1.0], [-0.7071067811865476, 1.0, 0.7071067811865476], [0.7071067811865476, 1.0, -0.7071067811865476]],
    [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 1.0, 0.0]],
    [[1.0, 1.0, 0.0], [0.7071067811865476, -0.7071067811865476, 1.0], [-0.7071067811865476, 0.7071067811865476, 1.0]],
    [[1.0, -0.7071067811865476, -0.7071067811865476], [1.0, 0.7071067811865476, 0.7071067811865476], [0.0, -1.0, 1.0]],
    [[1.0, 0.7071067811865476, -0.7071067811865476], [1.0, -0.7071067811865476, 0.7071067811865476], [0.0, 1.0, 1.0]],
    [[1.0, -0.7071067811865475, 0.0], [0.0, 0.0, 1.0], [0.7071067811865475, 1.0, 0.0]],
    [[1.0, 0.7071067811865475, 0.0], [0.0, 0.0, 1.0], [-0.7071067811865475, 1.0, 0.0]],
    [[1.0, 0.0, 0.0], [0.0, -1.0, 1.0], [0.0, 1.0, 1.0]],
    [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
    [[1.0, 0.0, 0.0], [0.0, -0.7071067811865475, 1.0], [0.0, 1.0, 0.7071067811865475]],
    [[1.0, 0.0, 0.0], [0.0, 0.7071067811865475, 1.0], [0.0, 1.0, -0.7071067811865475]],
    [[1.0, 0.0, -0.7071067811865475], [0.7071067811865475, 0.0, 1.0], [0.0, 1.0, 0.0]],
    [[1.0, 0.0, 0.7071067811865475], [-0.7071067811865475, 0.0, 1.0], [0.0, 1.0, 0.0]],
    [[-1.0, 0.0, 1.0], [-0.7071067811865476, 1.0, -0.7071067811865476], [0.7071067811865476, 1.0, 0.7071067811865476]],
    [[-0.7071067811865476, -0.7071067811865476, 1.0], [0.7071067811865476, 0.7071067811865476, 1.0], [-1.0, 1.0, 0.0]]
]

def convert_exact(element, tol=1e-12):
    """
    Recursively convert floats in nested lists into exact SageMath numbers.
    Handles sqrt(2)/2 approximations and simple rationals (-1, 0, 1).
    """
    if isinstance(element, list):
        return [convert_exact(e, tol) for e in element]

    # Handle common exact values
    if isclose(element, 0.0, abs_tol=tol):
        return 0
    if isclose(element, 1.0, abs_tol=tol):
        return 1
    if isclose(element, -1.0, abs_tol=tol):
        return -1
    if isclose(abs(element), 0.7071067811865476, abs_tol=tol):
        return (sqrt(2)/2) if element > 0 else -(sqrt(2)/2)

    # Fallback: keep as is (maybe a different float)
    return element

# Example usage
converted = convert_exact(liste)
print(converted)
