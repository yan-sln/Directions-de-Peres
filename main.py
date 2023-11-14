# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:01:31 2023

@author: yan-s
"""

## Ajout des bibliothèques nécessaires
from copy import deepcopy
import matplotlib.pyplot as plt
from numpy import array, radians, sin, cos, argsort, where
from scipy.spatial import distance
from itertools import product, combinations


## Fonctions de rotation des coordonnées d'un cube

# Fonction qui effectue une rotation theta sur l'axe X
def axeX(e, theta):
    """Matrice de rotation en 3D sur l'axe X :

|1     0           0| |x|   |        x        |   |x'|
|0   cos θ    −sin θ| |y| = |y cos θ − z sin θ| = |y'|
|0   sin θ     cos θ| |z|   |y sin θ + z cos θ|   |z'|"""
    vect = [e[0],
            e[1] * cos(theta) - e[2] * sin(theta),
            e[1] * sin(theta) + e[2] * cos(theta)]
    return (vect)

# Fonction qui effectue une rotation theta sur l'axe Y
def axeY(e, theta):
    """Matrice de rotation en 3D sur l'axe Y :

| cos θ    0   sin θ| |x|   | x cos θ + z sin θ|   |x'|
|   0      1       0| |y| = |         y        | = |y'|
|−sin θ    0   cos θ| |z|   |−x sin θ + z cos θ|   |z'|"""
    vect = [e[0] * cos(theta) + e[2] * sin(theta),
            e[1],
            -e[0] * sin(theta) + e[2] * cos(theta)]
    return (vect)

# Fonction qui effectue une rotation theta sur l'axe Z
def axeZ(e, theta):
    """Matrice de rotation en 3D sur l'axe Z :
        
|cos θ   −sin θ   0| |x|   |x cos θ − y sin θ|   |x'|
|sin θ    cos θ   0| |y| = |x sin θ + y cos θ| = |y'|
|  0       0      1| |z|   |        z        |   |z'|"""
    vect = [e[0] * cos(theta) - e[1] * sin(theta),
            e[0] * sin(theta) + e[1] * cos(theta),
            e[2]]
    return (vect)

# Fonction pour créer une nouvelle liste des coordonnées du cube tourner
def rotation(axe, theta, CONST_LST_ORIGINE):    
    # Créer une liste à but de contenir les sommets tourné
    cubeTourner = []    
    # Pour chaque sommet, applique une rotations et le rajoute à la liste
    for i in CONST_LST_ORIGINE:
        # Appel d'une fonction axeX, AxeY ou AxeZ
        rotationPoint = axe(i,theta)    
        # Évite les redondances
        if rotationPoint not in cubeTourner:
            cubeTourner.append(rotationPoint)    
    return cubeTourner


## Trouve les 3 points "voisins" de chaque sommet du cube, et pour chaque rajoute un point équidistant

# Petite fonction qui renvoie les coordonnées d'un point équidistant à 2 autres (utilisé par voisins())
def equidistant(l1, l2):
    l1 = [(l1[i] + l2[i])/2 for i in range(len(l1))]
    return l1

# Méthode qui pour chaque cube, ajoute les points équidistants aux sommets
def voisins(sommetsCube):    
    # Créer une copie de travail des sommets du cube
    pointsCube = deepcopy(sommetsCube)
    
    # On calcule pour chaque sommet sa distance aux autres
    dist = distance.squareform(distance.pdist(pointsCube))    
    #Pour chaque sommet, créer une liste arrangée des sommets les plus proches
    lProches = argsort(dist, axis=1)    
    
    k = 3  # Pour chaque point, créer une liste des 3 plus proches
    for idx, i in enumerate(lProches):
        for ii in i[1:k+1]:
            pointsCube[idx].append(sommetsCube[ii])
            # Structure dans pointsCube: [pointsCube[0],[sommetsCube[ii0], sommetsCube[ii1], sommetsCube[ii2]]],
    
    # Pour chaque point, on créer un point équidistant à l'un de ses voisins, et ce pour chaques voisins
    for i in pointsCube:
        # On recréer le point de base
        sommet = [i[0], i[1], i[2]]
        # Pour chaque voisin
        for ii in i[3:]:
            # Créer un point équidistant
            pointEquidistant = equidistant(sommet, ii)
            # Pour éviter de rajouter des doublons, rajoute ssi n'existe pas
            if pointEquidistant not in sommetsCube:
                # On ajoute les points équidistants à la liste des sommets
                sommetsCube.append(pointEquidistant)


## Ramène tous les points sur les faces du cube de base

# Renvoie les coefficients d'une équation de plan
def inPlane(points, d, i):
    # Vecteur pour créer le vecteur normal au plan
    v = [d, 0, 0]
    # Créer un vecteur normal au plan
    vNormal = [v[i % len(v)], v[(i+1) % len(v)], v[(i+2) % len(v)]]
    # Créer l'équation du plan à l'aide du vecteur normal et de la distance d de l'origine
    plan = array([-vNormal[0], -vNormal[1], -vNormal[2], d])
    return plan

# Renvoie la liste des index des points présent sur le plan
def get_planer_indexes(pts, plan):
    # Calcule A*vNormal[0] + B*vNormal[1] + C*vNormal[3] + D pour chaque point du plan dans pts
    # Vérifie que abs(...) est en-dessous du treshold (1e-6) pour autoriser les erreurs de calcul flottant
    return where(abs(pts.dot(plan[:3]) + plan[3]) <= 1e-6)

# S'assure de ne pas changer de face
def face(v):
    v = v[0] + v[1] + v[2]
    if v >= 0: return True
    else: return False

# Fonction qui ramène tous les points sur les faces du cube de base
def Peres(tousPoints):
    # Pour chaque point, prend plus grande valeur; λ = ± (1/(max(abs(x), abs(y), abs(z))))
    for idx, point in enumerate(tousPoints):
        # On définit un coefficient lambda à appliquer le point pour...
        lbda = d/(max(abs(point[0]), abs(point[1]), abs(point[2])))    
        # ...le ramener sur le cube de base
        tousPoints[idx] = [lbda*point[0], lbda*point[1], lbda*point[2]]
    
        # Liste des directions de Peres
        Peres = []
        # Liste temporaire pour le calcul
        lTemp = array(tousPoints)
        for i in range(3):
            indexes = get_planer_indexes(array(lTemp), inPlane(CONST_LST_ORIGINE, d, i))
            for ii in lTemp[indexes]:
                ii = list(ii)
                if (ii not in Peres) and face(ii):    # N'ajoute pas si 2 coordonnées du vecteur négatives => pas sur faces recherchées; #!!!!!!!!!!!!! si pas activé, 40 vecteurs !!!!!!!!!!!!!!!
                    Peres.append(ii)
    return Peres


## Enlève colinéaires + affiche

# Colinéaire ssi xyz = x'y'z' ssi xyz - x'y'z' = 0
def colineaire(v1, v2):
    return (v1[0]*v1[1]*v1[2] - v2[0]*v2[1]*v2[2]) == 0

# Méthode pour supprimer des vecteurs colinéaires
def removeColineaires(L):
    toRemove=[]
    # On place un des vecteurs colinéaires dans une liste
    for i, ii in combinations(L,2):
            if colineaire(i, ii):
                if ii not in toRemove:
                    toRemove.append(ii)
    # On le supprime de la liste originale
    for i in L:
        if i not in toRemove:
            L.remove(i)
            
# Méthode qui affiche chaque élément d'une liste
def affiche(l):
    print(f'Il y a {len(l)} éléments qui sont : ')
    for i in l:
        print(i, end=',\n')
        

# Méthode
def plotCubesPeres(D, theta, alpha, Peres):
    """Affiche une figure contenant 4 cubes de Peres, avec les 33 directions"""

    # Créer la figure
    plt.figure(figsize = (16, 9))
    # Propriétés des axes
    ax = plt.axes(projection="3d")
    ax.set_aspect("auto")
    ax.set_autoscale_on(True)
    plt.title("Directions de Peres")
    ax.set_xlabel('Axe-X', fontweight ='bold') 
    ax.set_ylabel('Axe-Y', fontweight ='bold') 
    ax.set_zlabel('Axe-Z', fontweight ='bold')
    # Inverse le sens de Axe-Y pour avoir les vecteurs face à soit
    plt.gca().invert_yaxis()
    
    ## Trace les cubes
    v = [1, 0, 0]
    axe = {0: axeX, 1: axeY, 2: axeZ}
    for s, e in combinations(array(list(product(D, D, D))), 2):
        if sum(abs(s-e)) == D[1]-D[0]:
            # Créer un cube de Base (noir)
            ax.plot3D(*zip(s, e), color="black")            
            # Créer les 3 autres cubes de rotation
            for i in range(3):
                # Rotation sur l'axe X du cube de Base
                s_rotated, e_rotated = axe[i](e, theta), axe[i](s, theta)
                # Créer un cube rouge, puis bleu, puis vert
                ax.plot3D(*zip(s_rotated, e_rotated), color=[v[i % len(v)], v[(i+1) % len(v)], v[(i+2) % len(v)], alpha])
                
    ## Trace les flêches représentant les directions de Peres
    # Remanie la liste des coordonnées de vecteurs
    l = [[], [], []]    # Définit stucture : [[x, ..., xn], [y, ..., yn], [z, ..., zn]]
    for idx, i in enumerate(Peres):
        for iidx in range(len(i)):
            l[iidx].append(Peres[idx][iidx])
    # Coordonnées (x,y,z)        
    x, y, z = l[0], l[1], l[2]
    # Direction des flêches/vecteur
    u, v, w = sin(x), sin(y), sin(z)
    # Trace toutes les flêches
    ax.quiver(x, y, z, u, v, w, length=0.25, normalize=True)

    ## Trace les points à la base des flêches
    for i in Peres:
        # Récupère les coordonnées de chaque point, un à un
        x = i[0]; y = i[1]; z = i[2]
        # Trace le point
        ax.scatter3D(x, y, z, alpha = 0.8, c = (x + y + z), cmap = plt.get_cmap('hsv'), marker ='.')

    # Affiche la figure
    plt.show()
    


# Si exécuté en tant que programe principal
if __name__ == '__main__':
    ## 1. On définit les variables  
    
    # Définit la dimension du cube
    d = 1; D = [-d, d]
    
    # Liste constante des sommets du cube origine
    CONST_LST_ORIGINE = [list(tup) for tup in product(D, D, D)]
    
    # Créer une liste des sommets du cube de base
    cube = deepcopy(CONST_LST_ORIGINE)
    
    
    ## 2. On effectue les rotations du cube sur les axes X, Y, Z   
    
    # On définit l'angle de rotaion
    theta = radians(45)    
    
    # On calcul les coordonnées des cubes de rotations
    cubeX = rotation(axeX, theta, CONST_LST_ORIGINE)
    cubeY = rotation(axeY, theta, CONST_LST_ORIGINE)
    cubeZ = rotation(axeZ, theta, CONST_LST_ORIGINE)
    
    
    ## 3. Créer une liste contenant tous les sommets et tous les points équidistants
    
    # Trouve les points équidistants de chaque sommets et les ajoutes à la liste des sommets de chaques cubes
    voisins(cube); voisins(cubeX); voisins(cubeY); voisins(cubeZ)
    # Créer une liste contenant tous les sommets et tous les points équidistants
    tousPoints = cube + cubeX + cubeY + cubeZ   #len(tousPoints) = 80 (si enlève doublon, 74)
    # Supprime les variables inutilisées
    del cube, cubeX, cubeY, cubeZ
    
    
    ## 4. Ramène tous les points sur les 3 faces positives du cube de base, supprime les doublons et affiche les 33 directions de Peres
    
    # Ramène tous les points sur les 3 faces positives du cube de base
    Peres = Peres(tousPoints)
    # Supprime les variables inutilisées
    del tousPoints
    # Exécute la méthode pour supprimer les vecteurs colinéaires
    removeColineaires(Peres)    
    # Affiche les directions de Peres
    affiche(Peres)
    
    ## 5 Créer la figure et l'affiche
    
    # Programme dans programme
    plotCubesPeres(D, theta, 0.3, Peres)
