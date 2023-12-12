# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:50:06 2023

@author: yan-s
"""
# %% Dépendances
# Récupère la fonction définit précédemment
from orthogonalite import orthogonalite as ortho

# On récupère la liste des directions de Peres déterminées précédemment
directionsPeres = [[1.0, 0.0, 1.0],
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
                   [0.0, 1.0, 0.7071067811865475]]

def affiche(l:list)-> str:
    """Affcihe lisiblement le nombre et les éléments d'une liste"""
    print(f'La liste contient {len(l)} éléments :')
    for i in l:
        print(i,end=', \n')

# %% Question 5: liste triplets directionsPeres 2 à 2 orthogonales (16)
from itertools import combinations

triplets = []
for i, ii, iii in combinations(directionsPeres, 3):
    if ortho(i, ii) and ortho(i, iii) and ortho(ii, iii):
        triplets.append([i, ii, iii])
        
# %% Question 6: liste paires de directionsPeres orthogonales (72)

paires = []
for i, ii in combinations(directionsPeres, 2):
    if ortho(i, ii):
        paires.append([i, ii])
      
## Question 6bis: 24 paires non déjà présentes dans triplets
p = []
# On ajoute à p 3 paires à partir de chaque triplets
for i in triplets:
    p.append([i[0],i[1]])
    p.append([i[0],i[2]])
    p.append([i[1],i[2]])

# On supprime les paires présentent dans p
for i in p:
    while i in paires:
        paires.remove(i)

# %% Question 7: les 24 triplets supplémentaires
from numpy import cross

def lbda(point:list, d:int)-> list:
    """Fonction qui ramène un point sur les faces du cube de base, tq. λ = ± (1/(max(abs(x), abs(y), abs(z))))"""
    # On définit un coefficient lambda à appliquer au point pour...
    lbda = 1/(max(abs(point[0]), abs(point[1]), abs(point[2])))
    # ...le ramener sur le cube de base
    return [lbda*point[0], lbda*point[1], lbda*point[2]]

tripletsSupp = []
for i in paires:
    for ii, iii in combinations(i,2):
        # On trouve un vecteur normal aux 2 autres, qu'on raméne sur le cube de dim 1
        tripletsSupp.append([lbda(list(cross(ii, iii)), 1), ii, iii])
        
# %% Question 8:
aretes = paires[:]
# dans arrete ssi app à paires ou app à triplets
for i in triplets:
    for ii, iii in combinations(i, 2):
        aretes.append([ii, iii])

from matplotlib import rcParams
import matplotlib.pyplot as plt

# Définit taille figure
rcParams['figure.dpi'] = 300
rcParams['figure.figsize'] = (100, 100)
# Créer la figure
fig = plt.figure(figsize=(20, 15))
plt.title('Graphe en 3D.')
# Propriétés des axes
ax = plt.axes(projection='3d')
ax.set_aspect("auto")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
# Orientation du point de vue
ax.view_init(20, 43)
# Définit les labels des axes
ax.set_xlabel('Axe-X', fontweight='bold')
ax.set_ylabel('Axe-Y', fontweight='bold')
ax.set_zlabel('Axe-Z', fontweight='bold')

for i in aretes:
    ax.plot3D([i[0][0], i[1][0]], [i[0][1], i[1][1]], [i[0][2], i[1][2]], marker = 'o')
    
plt.show()
