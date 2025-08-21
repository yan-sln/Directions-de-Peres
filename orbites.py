from math import sqrt

# --- Data ---

D=[[1, 0, 1], [1, 1, 0], [1, -1/2*sqrt(2), -1/2*sqrt(2)], [1, 1/2*sqrt(2), -1/2*sqrt(2)], [1, -1/2*sqrt(2), 1/2*sqrt(2)], [1, 1/2*sqrt(2), 1/2*sqrt(2)], [1, -1/2*sqrt(2), 0], [1, 1/2*sqrt(2), 0], [1, 0, 0], [1, 0, -1/2*sqrt(2)], [1, 0, 1/2*sqrt(2)], [-1, 0, 1], [0, -1, 1], [0, 1, 1], [-1/2*sqrt(2), 0, 1], [1/2*sqrt(2), 0, 1], [0, 0, 1], [0, -1/2*sqrt(2), 1], [0, 1/2*sqrt(2), 1], [-1/2*sqrt(2), -1/2*sqrt(2), 1], [1/2*sqrt(2), -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1/2*sqrt(2), 1], [1/2*sqrt(2), 1/2*sqrt(2), 1], [-1, 1, 0], [-1/2*sqrt(2), 1, 0], [1/2*sqrt(2), 1, 0], [0, 1, 0], [-1/2*sqrt(2), 1, 1/2*sqrt(2)], [-1/2*sqrt(2), 1, -1/2*sqrt(2)], [1/2*sqrt(2), 1, 1/2*sqrt(2)], [1/2*sqrt(2), 1, -1/2*sqrt(2)], [0, 1, -1/2*sqrt(2)], [0, 1, 1/2*sqrt(2)]]

T=[[[1, 0, 1], [-1, 0, 1], [0, 1, 0]], [[1, 0, 1], [-1/2*sqrt(2), 1, 1/2*sqrt(2)], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 1, 0], [0, 0, 1], [-1, 1, 0]], [[1, 1, 0], [1/2*sqrt(2), -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1, 1/2*sqrt(2), 1/2*sqrt(2)], [0, -1, 1]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [1, -1/2*sqrt(2), 1/2*sqrt(2)], [0, 1, 1]], [[1, -1/2*sqrt(2), 0], [0, 0, 1], [1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), 0], [0, 0, 1], [-1/2*sqrt(2), 1, 0]], [[1, 0, 0], [0, -1, 1], [0, 1, 1]], [[1, 0, 0], [0, 0, 1], [0, 1, 0]], [[1, 0, 0], [0, -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[1, 0, 0], [0, 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1], [0, 1, 0]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1], [0, 1, 0]], [[-1, 0, 1], [-1/2*sqrt(2), 1, -1/2*sqrt(2)], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [1/2*sqrt(2), 1/2*sqrt(2), 1], [-1, 1, 0]]]

P=[[[1, 0, 1], [-1, 0, 1]], [[1, 0, 1], [0, 1, 0]], [[1, 0, 1], [-1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[1, 0, 1], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1/2*sqrt(2), -1/2*sqrt(2), 1]], [[1, 1, 0], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, 1, 0], [-1, 1, 0]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1, 1/2*sqrt(2), 1/2*sqrt(2)]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [0, -1, 1]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [1, -1/2*sqrt(2), 1/2*sqrt(2)]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [0, 1, 1]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [-1/2*sqrt(2), 1, 0]], [[1, -1/2*sqrt(2), 1/2*sqrt(2)], [0, 1, 1]], [[1, -1/2*sqrt(2), 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1]], [[1, -1/2*sqrt(2), 1/2*sqrt(2)], [1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), 1/2*sqrt(2)], [0, -1, 1]], [[1, 1/2*sqrt(2), 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1]], [[1, 1/2*sqrt(2), 1/2*sqrt(2)], [-1/2*sqrt(2), 1, 0]], [[1, -1/2*sqrt(2), 0], [0, 0, 1]], [[1, -1/2*sqrt(2), 0], [1/2*sqrt(2), 1, 0]], [[1, -1/2*sqrt(2), 0], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[1, -1/2*sqrt(2), 0], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 1/2*sqrt(2), 0], [0, 0, 1]], [[1, 1/2*sqrt(2), 0], [-1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), 0], [-1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[1, 1/2*sqrt(2), 0], [-1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 0, 0], [0, -1, 1]], [[1, 0, 0], [0, 1, 1]], [[1, 0, 0], [0, 0, 1]], [[1, 0, 0], [0, -1/2*sqrt(2), 1]], [[1, 0, 0], [0, 1/2*sqrt(2), 1]], [[1, 0, 0], [0, 1, 0]], [[1, 0, 0], [0, 1, -1/2*sqrt(2)]], [[1, 0, 0], [0, 1, 1/2*sqrt(2)]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), -1/2*sqrt(2), 1]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, 0, -1/2*sqrt(2)], [0, 1, 0]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), -1/2*sqrt(2), 1]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, 0, 1/2*sqrt(2)], [0, 1, 0]], [[-1, 0, 1], [0, 1, 0]], [[-1, 0, 1], [-1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[-1, 0, 1], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[0, -1, 1], [0, 1, 1]], [[-1/2*sqrt(2), 0, 1], [0, 1, 0]], [[1/2*sqrt(2), 0, 1], [0, 1, 0]], [[0, 0, 1], [-1, 1, 0]], [[0, 0, 1], [-1/2*sqrt(2), 1, 0]], [[0, 0, 1], [1/2*sqrt(2), 1, 0]], [[0, 0, 1], [0, 1, 0]], [[0, -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[0, -1/2*sqrt(2), 1], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[0, -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[0, 1/2*sqrt(2), 1], [-1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[0, 1/2*sqrt(2), 1], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[0, 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [1/2*sqrt(2), 1/2*sqrt(2), 1]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [-1, 1, 0]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[1/2*sqrt(2), -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1/2*sqrt(2), -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[-1/2*sqrt(2), 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[1/2*sqrt(2), 1/2*sqrt(2), 1], [-1, 1, 0]], [[1/2*sqrt(2), 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[-1/2*sqrt(2), 1, 1/2*sqrt(2)], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[-1/2*sqrt(2), 1, -1/2*sqrt(2)], [1/2*sqrt(2), 1, 1/2*sqrt(2)]]]

# --- Build group of cube rotations ---

# Precompute symmetric pairs ±d
Ds = [[d, [-d[0], -d[1], -d[2]]] for d in D]

# Build generators DRx, DRy, DRz
def find_rotation_map(rot_formula):
    """
    Build rotation mapping {d -> rot(d)} using Ds for identification
    """
    mapping = []
    for d in D:
        rotated = rot_formula(d)
        for ds in Ds:
            if rotated in ds:  # identify with D or -D
                mapping.append([d, ds[0]])  # map to representative in D
    return mapping

# Rotation formulas
DRz = find_rotation_map(lambda d: [-d[1], d[0], d[2]])   # rotation pi/2 about z
DRy = find_rotation_map(lambda d: [d[2], d[1], -d[0]])   # rotation pi/2 about y
DRx = find_rotation_map(lambda d: [d[0], -d[2], d[1]])   # rotation pi/2 about x

def composition(ga, gb):
    """Compose two maps ga, gb (both lists of [point, image])"""
    result = []
    for d in D:
        img = [pair[1] for pair in gb if pair[0] == d][0]
        img2 = [pair[1] for pair in ga if pair[0] == img][0]
        result.append([d, img2])
    return result

def rot(rotation):
    """Return map corresponding to rotation [x,y,z] (quarter turns about x,y,z)"""
    imD = [[d, d] for d in D]  # identity
    for _ in range(rotation[0]): imD = composition(DRx, imD)
    for _ in range(rotation[1]): imD = composition(DRy, imD)
    for _ in range(rotation[2]): imD = composition(DRz, imD)
    return imD

# Generate group G
rotations = [(x,y,z) for x in range(4) for y in range(4) for z in range(4)]
G = []
for r in rotations:
    g = rot(r)
    if g not in G:
        G.append(g)

print("We found", len(G), "positive isometries (rotations).")  # Expect 24


# --- Generic orbit computation ---

def orbit_action(G, objects, action):
    """
    Compute orbits of `objects` under group action.
    action(g, obj) applies element g to object obj.
    """
    orbits = []
    seen = []
    for obj in objects:
        if obj not in seen:
            orbit = []
            for g in G:
                image = action(g, obj)
                if image not in orbit:
                    orbit.append(image)
            orbits.append(orbit)
            seen.extend(orbit)
    return orbits

# Actions on D, T, P
def act_on_point(g, d):
    return [pair[1] for pair in g if pair[0] == d][0]

def act_on_tuple(g, tup):
    return [act_on_point(g, d) for d in tup]

# Compute orbits
orbitsD = orbit_action(G, D, act_on_point)
orbitsT = orbit_action(G, T, act_on_tuple)
orbitsP = orbit_action(G, P, act_on_tuple)

print("Number of orbits on D:", len(orbitsD))
print("Number of orbits on T:", len(orbitsT))
print("Number of orbits on P:", len(orbitsP))
