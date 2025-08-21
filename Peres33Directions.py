# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:01:31 2023

@author: yan-s
"""

from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from numpy import array, radians, sin, cos, argsort, where, isclose
from numpy.linalg import norm
from scipy.spatial import distance
from itertools import product, combinations


# =====================
#  Rotation Utilities
# =====================

class MatricesRotations:
    """Static utility functions for 3D rotation matrices around X, Y, Z axes."""

    @staticmethod
    def axeX(n, theta):
        """3D rotation matrix around X axis:

        |1     0           0| |x|   |        x        |   |x'|
        |0   cos θ    −sin θ| |y| = |y cos θ − z sin θ| = |y'|
        |0   sin θ     cos θ| |z|   |y sin θ + z cos θ|   |z'|
        """
        return [
            n[0],
            n[1] * cos(theta) - n[2] * sin(theta),
            n[1] * sin(theta) + n[2] * cos(theta)
        ]

    @staticmethod
    def axeY(n, theta):
        """3D rotation matrix around Y axis:

        | cos θ    0   sin θ| |x|   | x cos θ + z sin θ|   |x'|
        |   0      1       0| |y| = |         y        | = |y'|
        |−sin θ    0   cos θ| |z|   |−x sin θ + z cos θ|   |z'|
        """
        return [
            n[0] * cos(theta) + n[2] * sin(theta),
            n[1],
            -n[0] * sin(theta) + n[2] * cos(theta)
        ]

    @staticmethod
    def axeZ(n, theta):
        """3D rotation matrix around Z axis:

        |cos θ   −sin θ   0| |x|   |x cos θ − y sin θ|   |x'|
        |sin θ    cos θ   0| |y| = |x sin θ + y cos θ| = |y'|
        |  0       0      1| |z|   |        z        |   |z'|
        """
        return [
            n[0] * cos(theta) - n[1] * sin(theta),
            n[0] * sin(theta) + n[1] * cos(theta),
            n[2]
        ]


def are_colinear(v1, v2, tol=1e-8):
    """Check if two vectors are colinear (parallel or anti-parallel)."""
    v1, v2 = array(v1) / norm(v1), array(v2) / norm(v2)
    return isclose(abs(v1.dot(v2)), 1.0, atol=tol)


# ======================
#  Peres 33 Directions
# ======================

class DirectionsPeres:
    """Compute the 33 Peres directions from cube rotations."""

    def __init__(self, d: float):
        self.d = d
        self.D = [-d, d]
        # Vertices of the original cube
        self._CONST_LST_ORIGINE = [list(tup) for tup in product(self.D, self.D, self.D)]
        # Copy of the base cube (will be modified with midpoints)
        self.cube = deepcopy(self._CONST_LST_ORIGINE)

    def main(self, theta: float):
        """Main entry point: generate the 33 Peres directions."""
        # Rotate the base cube around X, Y, Z
        cubeX = self.rotation(MatricesRotations.axeX, theta)
        cubeY = self.rotation(MatricesRotations.axeY, theta)
        cubeZ = self.rotation(MatricesRotations.axeZ, theta)

        # Add equidistant midpoints inside each cube
        for cube in (self.cube, cubeX, cubeY, cubeZ):
            self.add_midpoints(cube)

        # Gather all candidate points
        all_points = self.cube + cubeX + cubeY + cubeZ

        # Rescale them to lie on the faces of the cube of dimension d
        self.rescale_to_faces(all_points)

        # Extract the 33 unique Peres directions
        peres33 = self.compute_peres33(all_points)

        # Safety check
        assert len(peres33) == 33, f"Error: found {len(peres33)} directions instead of 33"

        return peres33

    def rotation(self, axe, theta: float):
        """Apply a given rotation to the original cube vertices."""
        pts = [axe(pt, theta) for pt in self._CONST_LST_ORIGINE]
        # Round to avoid floating-point artifacts and deduplicate
        pts = [tuple(round(x, 12) for x in p) for p in pts]
        return [list(p) for p in set(pts)]

    def equidistant(self, l1, l2):
        """Compute the midpoint between two points."""
        return [(l1[i] + l2[i]) / 2 for i in range(len(l1))]

    def add_midpoints(self, sommetsCube):
        """Add equidistant midpoints to a cube's vertices."""
        pointsCube = deepcopy(sommetsCube)
        dist = distance.squareform(distance.pdist(pointsCube))
        nearest = argsort(dist, axis=1)

        k = 3  # 3 closest neighbors
        for idx, i in enumerate(nearest):
            for ii in i[1:k + 1]:
                pointsCube[idx].append(sommetsCube[ii])

        for i in pointsCube:
            sommet = [i[0], i[1], i[2]]
            for ii in i[3:]:
                mid = self.equidistant(sommet, ii)
                if mid not in sommetsCube:
                    sommetsCube.append(mid)

    def indexPointsPlan(self, pts, plan):
        """Return indices of points lying on a given plane Ax + By + Cz + D = 0."""
        return where(abs(pts.dot(plan[:3]) + plan[3]) <= 1e-6)

    def rescale_to_faces(self, points):
        """Rescale points so that they lie on the cube faces |x|=d, |y|=d or |z|=d."""
        for idx, pt in enumerate(points):
            scale = self.d / max(abs(pt[0]), abs(pt[1]), abs(pt[2]))
            points[idx] = [scale * pt[0], scale * pt[1], scale * pt[2]]

    def compute_peres33(self, points):
        """Keep only the points lying on three positive faces (x=d, y=d, z=d)
        and remove colinear duplicates to obtain exactly 33 directions.
        """
        Peres = []
        pts = array(points)

        # Three positive faces of the cube
        faces = [
            array([1, 0, 0, -self.d]),  # x = d
            array([0, 1, 0, -self.d]),  # y = d
            array([0, 0, 1, -self.d])   # z = d
        ]

        # Collect points lying on these faces
        for plan in faces:
            idxs = self.indexPointsPlan(pts, plan)
            for pt in pts[idxs]:
                pt = list(pt)
                if pt not in Peres:
                    Peres.append(pt)

        # Remove the original cube vertices
        Peres = [i for i in Peres if i not in self._CONST_LST_ORIGINE]

        # Remove colinear duplicates
        final = []
        for v in Peres:
            if not any(are_colinear(v, u) for u in final):
                final.append(v)

        return final

    def affiche(self, directions):
        """Print the list of directions with their coordinates."""
        print(f"There are {len(directions)} directions:")
        for v in directions:
            print(v)


# ======================
#  3D Visualization
# ======================

class TraceDirectionsPeres:
    """Display cubes and the 33 Peres directions in 3D."""

    def __init__(self, directions, title="Peres Directions"):
        self.lst = directions
        rcParams['figure.dpi'] = 300
        plt.figure(figsize=(20, 15))
        plt.title(title)

        self.ax = plt.axes(projection="3d")
        self.ax.set_aspect("auto")
        self.ax.set_autoscale_on(True)
        self.ax.view_init(20, 43)

        self.ax.set_xlabel('X axis', fontweight='bold')
        self.ax.set_ylabel('Y axis', fontweight='bold')
        self.ax.set_zlabel('Z axis', fontweight='bold')

    def traceCubes(self, d, theta, alpha=0.4, allCubes=False):
        """Draw the base cube and optionally its 3 rotated versions."""
        v = [1, 0, 0]  # colors basis
        D = [-d, d]
        axe = {0: MatricesRotations.axeX,
               1: MatricesRotations.axeY,
               2: MatricesRotations.axeZ}

        for s, e in combinations(array(list(product(D, D, D))), 2):
            if sum(abs(s - e)) == D[1] - D[0]:
                self.ax.plot3D(*zip(s, e), color="black")
                if allCubes:
                    for i in range(3):
                        s_rot, e_rot = axe[i](s, theta), axe[i](e, theta)
                        self.ax.plot3D(
                            *zip(s_rot, e_rot),
                            color=[v[i % 3], v[(i + 1) % 3], v[(i + 2) % 3], alpha]
                        )

    def traceFleches(self):
        """Draw arrows representing the Peres directions."""
        pts = array(self.lst)
        x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        u, v, w = sin(x), sin(y), sin(z)
        self.ax.quiver(x, y, z, u, v, w, length=0.25, normalize=True)

    def tracePoints(self):
        """Draw points at the base of arrows."""
        for x, y, z in self.lst:
            self.ax.scatter3D(x, y, z, alpha=0.8,
                              c=(x + y + z),
                              cmap=plt.get_cmap('hsv'),
                              marker='.')

    def traceTextes(self):
        """Annotate each point with its coordinates."""
        for x, y, z in self.lst:
            self.ax.text(x, y, z + 0.01,
                         f"{x:.2f}, {y:.2f}, {z:.2f}",
                         fontsize="x-small")

    def affiche(self):
        """Show the final plot."""
        plt.show()


# ======================
#  Main program
# ======================

if __name__ == '__main__':
    d = 1        # Cube dimension
    theta = radians(45)  # Rotation angle

    # Generate the 33 Peres directions
    Peres33 = DirectionsPeres(d)
    directions = Peres33.main(theta)
    Peres33.affiche(directions)

    # Plot cubes and directions (arrows)
    fig1 = TraceDirectionsPeres(directions)
    fig1.traceCubes(d, theta, allCubes=True)
    fig1.traceFleches()
    fig1.tracePoints()
    fig1.affiche()

    # Plot with text annotations
    fig2 = TraceDirectionsPeres(directions, title="Peres Directions (with coordinates)")
    fig2.traceCubes(d, theta)
    fig2.tracePoints()
    fig2.traceTextes()
    fig2.affiche()
