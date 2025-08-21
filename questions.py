# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:50:06 2023

Author: yan-s

This script:
1. Computes orthogonal pairs and triplets among Peres' 33 directions.
2. Generates additional orthogonal triplets from pairs.
3. Builds a 3D graph representation of orthogonality relations.
"""

from itertools import combinations
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from numpy import cross, isclose
from orthogonalite import orthogonalite as ortho


# List of Peres' 33 directions (precomputed)
directionsPeres = [
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0],
    [1.0, -0.7071067811865476, -0.7071067811865476],
    [1.0, 0.7071067811865476, -0.7071067811865476],
    [1.0, -0.7071067811865476, 0.7071067811865476],
    [1.0, 0.7071067811865476, 0.7071067811865476],
    [1.0, -0.7071067811865475, 0.0],
    [1.0, 0.7071067811865475, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 0.0, -0.7071067811865475],
    [1.0, 0.0, 0.7071067811865475],
    [-1.0, 0.0, 1.0],
    [0.0, -1.0, 1.0],
    [0.0, 1.0, 1.0],
    [-0.7071067811865475, 0.0, 1.0],
    [0.7071067811865475, 0.0, 1.0],
    [0.0, 0.0, 1.0],
    [0.0, -0.7071067811865475, 1.0],
    [0.0, 0.7071067811865475, 1.0],
    [-0.7071067811865476, -0.7071067811865476, 1.0],
    [0.7071067811865476, -0.7071067811865476, 1.0],
    [-0.7071067811865476, 0.7071067811865476, 1.0],
    [0.7071067811865476, 0.7071067811865476, 1.0],
    [-1.0, 1.0, 0.0],
    [-0.7071067811865475, 1.0, 0.0],
    [0.7071067811865475, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [-0.7071067811865476, 1.0, 0.7071067811865476],
    [-0.7071067811865476, 1.0, -0.7071067811865476],
    [0.7071067811865476, 1.0, 0.7071067811865476],
    [0.7071067811865476, 1.0, -0.7071067811865476],
    [0.0, 1.0, -0.7071067811865475],
    [0.0, 1.0, 0.7071067811865475],
]


def pretty_print(lst: list) -> None:
    """Print list content with count."""
    print(f"The list contains {len(lst)} elements:")
    for el in lst:
        print(el, end=", \n")


# --- Q5: Find orthogonal triplets (16 expected) ---
triplets = []
for i, j, k in combinations(directionsPeres, 3):
    if ortho(i, j) and ortho(i, k) and ortho(j, k):
        triplets.append([i, j, k])

# --- Q6: Find orthogonal pairs (72 expected) ---
paires = []
for i, j in combinations(directionsPeres, 2):
    if ortho(i, j):
        paires.append([i, j])

# Q6bis: Keep only pairs not already in triplets (24 expected)
pairs_in_triplets = []
for t in triplets:
    pairs_in_triplets.extend([ [t[0],t[1]], [t[0],t[2]], [t[1],t[2]] ])

# Remove duplicates by using sets of tuples
pairs_in_triplets = {tuple(map(tuple, p)) for p in pairs_in_triplets}
paires = [p for p in paires if tuple(map(tuple, p)) not in pairs_in_triplets]

# --- Q7: Generate 24 additional triplets from pairs ---
def normalize_to_cube(point: list, d: int = 1) -> list:
    """
    Normalize a vector to lie on the cube faces of size d.
    λ = 1 / max(|x|, |y|, |z|)

    Parameters
    ----------
    point : list
        Input 3D vector
    d : int
        Cube half-size (default = 1)

    Returns
    -------
    list
        Normalized vector lying on cube faces
    """
    if all(isclose(c, 0.0) for c in point):
        raise ValueError("Cannot normalize zero vector.")
    lam = d / max(abs(point[0]), abs(point[1]), abs(point[2]))
    return [lam * point[0], lam * point[1], lam * point[2]]

tripletsSupp = []
for pair in paires:
    for i, j in combinations(pair, 2):  # always exactly 2 elements
        n = cross(i, j)
        tripletsSupp.append([normalize_to_cube(n, 1), i, j])

# --- Q8: Build edges for graph visualization ---
aretes = paires[:]
for t in triplets:
    for i, j in combinations(t, 2):
        aretes.append([i, j])


# --- Plot graph ---
rcParams['figure.dpi'] = 300
fig = plt.figure(figsize=(20, 15))
plt.title("Orthogonality graph in 3D")
ax = plt.axes(projection="3d")
ax.set_aspect("auto")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.view_init(20, 43)

ax.set_xlabel("X axis", fontweight="bold")
ax.set_ylabel("Y axis", fontweight="bold")
ax.set_zlabel("Z axis", fontweight="bold")

# Draw edges
for a, b in aretes:
    ax.plot3D([a[0], b[0]], [a[1], b[1]], [a[2], b[2]], marker="o")

plt.show()
