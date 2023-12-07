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
        
