from math import sqrt

# --- Input data ---

# List of 33 exact Peres directions
D = [
    [1, 0, 1], [1, 1, 0],
    [1, -sqrt(2)/2, -sqrt(2)/2], [1, sqrt(2)/2, -sqrt(2)/2],
    [1, -sqrt(2)/2,  sqrt(2)/2], [1, sqrt(2)/2,  sqrt(2)/2],
    [1, -sqrt(2)/2, 0], [1, sqrt(2)/2, 0], [1, 0, 0],
    [1, 0, -sqrt(2)/2], [1, 0, sqrt(2)/2],
    [-1, 0, 1], [0, -1, 1], [0, 1, 1],
    [-sqrt(2)/2, 0, 1], [sqrt(2)/2, 0, 1],
    [0, 0, 1], [0, -sqrt(2)/2, 1], [0, sqrt(2)/2, 1],
    [-sqrt(2)/2, -sqrt(2)/2, 1], [sqrt(2)/2, -sqrt(2)/2, 1],
    [-sqrt(2)/2,  sqrt(2)/2, 1], [sqrt(2)/2,  sqrt(2)/2, 1],
    [-1, 1, 0], [-sqrt(2)/2, 1, 0], [sqrt(2)/2, 1, 0], [0, 1, 0],
    [-sqrt(2)/2, 1,  sqrt(2)/2], [-sqrt(2)/2, 1, -sqrt(2)/2],
    [ sqrt(2)/2, 1,  sqrt(2)/2], [ sqrt(2)/2, 1, -sqrt(2)/2],
    [0, 1, -sqrt(2)/2], [0, 1, sqrt(2)/2]
]

# List of 16 exact orthogonal triplets
T = [
    [[1, 0, 1], [-1, 0, 1], [0, 1, 0]],
    [[1, 0, 1], [-sqrt(2)/2, 1,  sqrt(2)/2], [ sqrt(2)/2, 1, -sqrt(2)/2]],
    [[1, 1, 0], [0, 0, 1], [-1, 1, 0]],
    [[1, 1, 0], [ sqrt(2)/2, -sqrt(2)/2, 1], [-sqrt(2)/2,  sqrt(2)/2, 1]],
    [[1, -sqrt(2)/2, -sqrt(2)/2], [1,  sqrt(2)/2,  sqrt(2)/2], [0, -1, 1]],
    [[1,  sqrt(2)/2, -sqrt(2)/2], [1, -sqrt(2)/2,  sqrt(2)/2], [0, 1, 1]],
    [[1, -sqrt(2)/2, 0], [0, 0, 1], [ sqrt(2)/2, 1, 0]],
    [[1,  sqrt(2)/2, 0], [0, 0, 1], [-sqrt(2)/2, 1, 0]],
    [[1, 0, 0], [0, -1, 1], [0, 1, 1]],
    [[1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[1, 0, 0], [0, -sqrt(2)/2, 1], [0, 1,  sqrt(2)/2]],
    [[1, 0, 0], [0,  sqrt(2)/2, 1], [0, 1, -sqrt(2)/2]],
    [[1, 0, -sqrt(2)/2], [ sqrt(2)/2, 0, 1], [0, 1, 0]],
    [[1, 0,  sqrt(2)/2], [-sqrt(2)/2, 0, 1], [0, 1, 0]],
    [[-1, 0, 1], [-sqrt(2)/2, 1, -sqrt(2)/2], [ sqrt(2)/2, 1,  sqrt(2)/2]],
    [[-sqrt(2)/2, -sqrt(2)/2, 1], [ sqrt(2)/2,  sqrt(2)/2, 1], [-1, 1, 0]]
]

# List of 68 exact orthogonal pairs (commented out for now)
# P = [...]

# For now, only use the 16 triplets (can extend with pairs if needed)
U = T
# To include pairs too: U = T + P

# --- Functions ---

def sigma(direction):
    """
    Return the list of uplets in U (triplets or pairs) containing the given direction.
    """
    return [uplet for uplet in U if direction in uplet]

# --- Processing ---

# Count how many uplets contain each direction in D
listeCardSigma = [len(sigma(d)) for d in D]

print(listeCardSigma)
