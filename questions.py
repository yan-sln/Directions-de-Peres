# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:50:06 2023

@author: yan-s
"""

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

## Question 5: liste triplets directionsPeres 2 à 2 orthogonales (16)
from itertools import combinations

triplets = []
for i, ii, iii in combinations(directionsPeres, 3):
    if ortho(i, ii) and ortho(i, iii) and ortho(ii, iii):
        triplets.append([i, ii, iii])
        
## Question 6: liste paires de directionsPeres orthogonales (72)

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

## Question 7: 
from numpy import cross

tripletsSupp = []
for i in paires:
    for ii, iii in combinations(i,2):
        # Pour trouver vecteur normal au 2 autres, produit vectoriel
        tripletsSupp.append([list(cross(ii, iii)), ii, iii])
        
## Question 8:
arretes = []
# dans arrete ssi app à paires ou app à triplets
for i, ii in combinations(directionsPeres, 2):
    if ([i, ii] in paires) or ([i, ii] in combinations(triplets, 2)):
        arretes.append([i, ii])

from matplotlib import rcParams
import matplotlib.pyplot as plt

# Définit taille figure
rcParams['figure.dpi'] = 300
rcParams['figure.figsize'] = (100, 100)
# Créer la figure
fig = plt.figure(figsize=(20, 15))
plt.title("Graphe de Peres")
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

for i in arretes:
    ax.plot3D([i[0][0], i[1][0]], [i[0][1], i[1][1]], [i[0][2], i[1][2]], marker = 'o')
    
plt.show()
