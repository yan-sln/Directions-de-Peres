# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:01:31 2023

@author: yan-s
"""

# Ajout des bibliothèques et fonctions nécessaires
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib import rcParams
from numpy import array, radians, sin, cos, argsort, where
from scipy.spatial import distance
from itertools import product, combinations


class MatricesRotations:
    """Class contenant des fonctions pour appliquer une matrice de rotation sur les 3 axes X, Y, Z"""

    # Fonction qui effectue une rotation theta sur l'axe X
    @staticmethod
    def axeX(n, theta):
        """Matrice de rotation en 3D sur l'axe X :
    |1     0           0| |x|   |        x        |   |x'|
    |0   cos θ    −sin θ| |y| = |y cos θ − z sin θ| = |y'|
    |0   sin θ     cos θ| |z|   |y sin θ + z cos θ|   |z'|"""
        vect = [n[0],
                n[1] * cos(theta) - n[2] * sin(theta),
                n[1] * sin(theta) + n[2] * cos(theta)]
        return (vect)

    # Fonction qui effectue une rotation theta sur l'axe Y
    @staticmethod
    def axeY(n, theta):
        """Matrice de rotation en 3D sur l'axe Y :
    | cos θ    0   sin θ| |x|   | x cos θ + z sin θ|   |x'|
    |   0      1       0| |y| = |         y        | = |y'|
    |−sin θ    0   cos θ| |z|   |−x sin θ + z cos θ|   |z'|"""
        vect = [n[0] * cos(theta) + n[2] * sin(theta),
                n[1],
                -n[0] * sin(theta) + n[2] * cos(theta)]
        return (vect)

    # Fonction qui effectue une rotation theta sur l'axe Z
    @staticmethod
    def axeZ(n, theta):
        """Matrice de rotation en 3D sur l'axe Z :
    |cos θ   −sin θ   0| |x|   |x cos θ − y sin θ|   |x'|
    |sin θ    cos θ   0| |y| = |x sin θ + y cos θ| = |y'|
    |  0       0      1| |z|   |        z        |   |z'|"""
        vect = [n[0] * cos(theta) - n[1] * sin(theta),
                n[0] * sin(theta) + n[1] * cos(theta),
                n[2]]
        return (vect)


class DirectionsPeres(MatricesRotations):
    def __init__(self, d):
        #
        self.D = [-d, d]
        # Liste constante des sommets du cube origine
        self._CONST_LST_ORIGINE = [list(tup)
                                   for tup in product(self.D, self.D, self.D)]
        # Créer une liste des sommets du cube de base
        self.cube = deepcopy(self._CONST_LST_ORIGINE)

    def main(self, d):
        # On calcul les coordonnées des cubes de rotations
        cubeX = self.rotation(self.axeX, theta)
        cubeY = self.rotation(self.axeY, theta)
        cubeZ = self.rotation(self.axeZ, theta)
        # Trouve les points équidistants de chaque sommets et les ajoutes à la liste des sommets de chaques cubes
        self.voisins(self.cube); self.voisins(cubeX); self.voisins(cubeY); self.voisins(cubeZ)
        # Créer une liste contenant tous les sommets et tous les points équidistants
        # len(tousPoints) = 80 (si enlève doublon, 74)
        tousPoints = self.cube + cubeX + cubeY + cubeZ
        # Ramène tous les points sur les 3 faces positives du cube de base
        self.lbda(tousPoints, d)
        return self.peres(tousPoints, d)

    def rotation(self, axe, theta):
        """Fonction pour créer une nouvelle liste des coordonnées du cube tourné"""
        # Créer une liste à but de contenir les sommets tourné
        cubeTourner = []
        # Pour chaque sommet, applique une rotations et le rajoute à la liste
        for i in self._CONST_LST_ORIGINE:
            # Appel d'une fonction axeX, AxeY ou AxeZ
            rotationPoint = axe(i, theta)
            # Évite les redondances
            if rotationPoint not in cubeTourner:
                cubeTourner.append(rotationPoint)
        return cubeTourner

    def equidistant(self, l1, l2):
        """Fonction qui renvoie les coordonnées d'un point équidistant à 2 autres (utilisé par voisins())"""
        l1 = [(l1[i] + l2[i])/2 for i in range(len(l1))]
        return l1

    def voisins(self, sommetsCube):
        """Méthode qui pour chaque cube, ajoute les points équidistants aux sommets"""
        # Créer une copie de travail des sommets du cube
        pointsCube = deepcopy(sommetsCube)

        # On calcule pour chaque sommet sa distance aux autres
        dist = distance.squareform(distance.pdist(pointsCube))
        # Pour chaque sommet, créer une liste arrangée des sommets les plus proches
        lProches = argsort(dist, axis=1)

        k = 3  # Pour chaque point, créer une liste des 3 plus proches
        for idx, i in enumerate(lProches):
            for ii in i[1:k+1]:
                # Structure dans pointsCube: [pointsCube[0],[sommetsCube[ii0], sommetsCube[ii1], sommetsCube[ii2]]],
                pointsCube[idx].append(sommetsCube[ii])

        # Pour chaque point, on créer un point équidistant à l'un de ses voisins, et ce pour chaques voisins
        for i in pointsCube:
            # On recréer le point de base
            sommet = [i[0], i[1], i[2]]
            # Pour chaque voisin
            for ii in i[3:]:
                # Créer un point équidistant
                pointEquidistant = self.equidistant(sommet, ii)
                # Pour éviter de rajouter des doublons, rajoute ssi n'existe pas
                if pointEquidistant not in sommetsCube:
                    # On ajoute les points équidistants à la liste des sommets
                    sommetsCube.append(pointEquidistant)

    def creerPlan(self, points, d, i):
        """Renvoie les coefficients d'une équation de plan"""
        # Vecteur pour créer le vecteur normal au plan
        v = [d, 0, 0]
        # Créer un vecteur normal au plan
        vNormal = [v[i % len(v)], v[(i+1) % len(v)], v[(i+2) % len(v)]]
        # Créer l'équation du plan à l'aide du vecteur normal et de la distance d de l'origine
        # Négatif pour avoir un bon graphe
        plan = array([-vNormal[0], -vNormal[1], -vNormal[2], d])
        return plan

    def indexPointsPlan(self, pts, plan):
        """Renvoie la liste des index des points présent sur le plan"""
        # Calcule A*vNormal[0] + B*vNormal[1] + C*vNormal[3] + D pour chaque point du plan dans pts
        # Vérifie que abs(...) est en-dessous du treshold (1e-6) pour autoriser les erreurs de calcul flottant
        return where(abs(pts.dot(plan[:3]) + plan[3]) <= 1e-6)

    def lbda(self, tousPoints, d):
        """Méthode qui ramène tous les points sur les faces du cube de base"""
        # Pour chaque point, prend plus grande valeur; λ = ± (1/(max(abs(x), abs(y), abs(z))))
        for idx, point in enumerate(tousPoints):
            # On définit un coefficient lambda à appliquer le point pour...
            lbda = d/(max(abs(point[0]), abs(point[1]), abs(point[2])))
            # ...le ramener sur le cube de base
            tousPoints[idx] = [lbda*point[0], lbda*point[1], lbda*point[2]]
    
    def peres(self, tousPoints, d):
        # Liste des directions de Peres
        Peres = []  # -> recréer liste
        # Liste temporaire pour le calcul
        lTemp = array(tousPoints)
        for i in range(3):
            # Récupère index des points sur plan
            indexes = self.indexPointsPlan(
                array(lTemp), self.creerPlan(self._CONST_LST_ORIGINE, d, i))
            # Pour tous les index, récupère point
            for ii in lTemp[indexes]:
                # Retransforme en list
                ii = list(ii)
                # Si pas déjà dans la list
                if (ii not in Peres):
                    # Le rajoute
                    Peres.append(ii)                    
        # Supprime les sommets du cube initial
        Peres = [i for i in Peres if i not in self._CONST_LST_ORIGINE]
        
        # '''Colinéaires
        # [1.0, -1.0, 0.0] [-1.0, 1.0, 0.0]

        # [1.0, 0.0, -1.0] [-1.0, 0.0, 1.0]

        # [0.0, -1.0, 1.0] [0.0, 1.0, -1.0]
        # '''
        
        #!!!
        # Supprime les points sur les arrêtes en trop
        for i in lTemp[self.indexPointsPlan(array(lTemp), [0, 0, 1, 1])]:
            # Retransforme en list
            i = list(i)
            # Si dans la liste, le supprime
            if i in Peres:
                # Le rajoute
                Peres.remove(i)
        # Supprime sur arrêtes en trop
        for i in Peres:
            if i[0] == 1 and i[1] == -1:
                Peres.remove(i)
                
        #!!!
        
        # #Permet la même chose que le plan et la droite
        # from numpy import cross, isclose
        # # Colinéaire
        # def colineaire(v1, v2):
        #     return isclose(sum(map(abs ,list(cross(v1, v2)))), 0, rtol=1e-05, atol=1e-08, equal_nan=False)

        # L = []
        # for i, ii in combinations(Peres, 2):
        #     if colineaire(i, ii):
        #         L.append(i)
        #         L.append(ii)
        # L.sort()
        # for i in L[3:]:
        #     Peres.remove(i)
        #!!!
        
        return Peres

    def affiche(self, l):
        """Méthode qui affiche le nombre et chaque élément d'une liste"""
        print(f'Il y a {len(l)} éléments qui sont : ')
        for i in l:
            print(i, end=',\n')


class TraceDirectionsPeres(MatricesRotations):
    """Affiche une figure contenant 4 cubes de Peres, avec les 33 directions"""

    def __init__(self, directions):
        # Copie locale des directions
        self.lst = directions
        # Définit taille figure
        rcParams['figure.dpi'] = 300
        rcParams['figure.figsize'] = (100, 100)
        # Créer la figure
        plt.figure(figsize=(20, 15))
        plt.title("Directions de Peres")

        # Propriétés des axes
        self.ax = plt.axes(projection="3d")
        self.ax.set_aspect("auto")
        self.ax.set_autoscale_on(True)
        # Orientation du point de vue
        self.ax.view_init(20, 43)
        # Définit les labels des axes
        self.ax.set_xlabel('Axe-X', fontweight='bold')
        self.ax.set_ylabel('Axe-Y', fontweight='bold')
        self.ax.set_zlabel('Axe-Z', fontweight='bold')

    def traceCubes(self, d, theta, alpha=0.4, allCubes=False):
        """Trace les cubes"""
        v = [1, 0, 0]
        D = [-d, d]
        axe = {0: MatricesRotations.axeX,
               1: MatricesRotations.axeY, 2: MatricesRotations.axeZ}
        for s, e in combinations(array(list(product(D, D, D))), 2):
            if sum(abs(s-e)) == D[1]-D[0]:
                # Créer un cube de Base (noir)
                self.ax.plot3D(*zip(s, e), color="black")
                # Créer les 3 autres cubes de rotation
                if allCubes:
                    for i in range(3):
                        # Rotation sur l'axe X du cube de Base
                        s_rotated, e_rotated = axe[i](
                            e, theta), axe[i](s, theta)
                        # Créer un cube rouge, puis bleu, puis vert
                        self.ax.plot3D(*zip(s_rotated, e_rotated), color=[
                                       v[i % len(v)], v[(i+1) % len(v)], v[(i+2) % len(v)], alpha])

    def traceFleches(self):
        """Trace les flêches représentant les directions de Peres"""
        # Définit stucture : [[x, ..., xn], [y, ..., yn], [z, ..., zn]]
        l = [[], [], []]
        for idx, i in enumerate(self.lst):
            for iidx in range(len(i)):
                l[iidx].append(self.lst[idx][iidx])
        # Coordonnées (x,y,z)
        x, y, z = l[0], l[1], l[2]
        # Direction des flêches/vecteur
        u, v, w = sin(x), sin(y), sin(z)
        # Trace toutes les flêches
        self.ax.quiver(x, y, z, u, v, w, length=0.25, normalize=True)

    def tracePoints(self):
        # Trace les points à la base des flêches
        for i in self.lst:
            # Récupère les coordonnées de chaque point, un à un
            x = i[0]; y = i[1]; z = i[2]
            # Trace le point
            self.ax.scatter3D(x, y, z, alpha=0.8, c=(
                x + y + z), cmap=plt.get_cmap('hsv'), marker='.')

    def traceTextes(self):
        for i in self.lst:
            # Récupère les coordonnées de chaque point, un à un
            x = i[0]; y = i[1]; z = i[2]
            self.ax.text(x, y, z+0.01,
                         f'{x:.2f}, {y:.2f}, {z:.2f}', fontsize='x-small')

    def affiche(self):
        # Affiche la figure
        plt.show()


# Si exécuté en tant que programe principal
if __name__ == '__main__':
    
    d = 1  # Dimention des cubes
    theta = radians(45)  # Angle de rotation entre les cubes

    # Créer les 33 directions de Peres
    Peres33 = DirectionsPeres(d)
    Peres = Peres33.main(d)
    Peres33.affiche(Peres)  # Affiche les directions de Peres

    # Trace 4 Cubes, vecteurs et flêches
    figure = TraceDirectionsPeres(Peres)
    figure.traceCubes(d, theta, allCubes=True)
    figure.traceFleches()
    figure.tracePoints()
    figure.affiche()

    # Trace les directions et leurs coordonnées
    figure2 = TraceDirectionsPeres(Peres)
    figure2.traceCubes(d, theta)
    figure2.tracePoints()
    figure2.traceTextes()
    figure2.affiche()
