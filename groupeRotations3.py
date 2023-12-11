# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:15:16 2023

@author: yan-s
"""

# %% Partie 0
# On importe les fonctions nécessaires
from tqdm import tqdm
from itertools import product
from numpy import radians, dot, isclose, sqrt
from Directions_de_Peres3 import MatricesRotations as mr

# %% Partie 1 :
# On récupère la liste des 33 directions de Peres déterminée précédemment
directionsPeres = [[1.0, 0.0, 1.0],[1.0, 1.0, 0.0],[1.0, -0.7071067811865476, -0.7071067811865476],[1.0, 0.7071067811865476, -0.7071067811865476],[1.0, -0.7071067811865476, 0.7071067811865476],[1.0, 0.7071067811865476, 0.7071067811865476],[1.0, -0.7071067811865475, 0.0],[1.0, 0.7071067811865475, 0.0],[1.0, 0.0, 0.0],[1.0, 0.0, -0.7071067811865475],[1.0, 0.0, 0.7071067811865475],[-1.0, 0.0, 1.0],[0.0, -1.0, 1.0],[0.0, 1.0, 1.0],[-0.7071067811865475, 0.0, 1.0],[0.7071067811865475, 0.0, 1.0],[0.0, 0.0, 1.0],[0.0, -0.7071067811865475, 1.0],[0.0, 0.7071067811865475, 1.0],[-0.7071067811865476, -0.7071067811865476, 1.0],[0.7071067811865476, -0.7071067811865476, 1.0],[-0.7071067811865476, 0.7071067811865476, 1.0],[0.7071067811865476, 0.7071067811865476, 1.0],[-1.0, 1.0, 0.0],[-0.7071067811865475, 1.0, 0.0],[0.7071067811865475, 1.0, 0.0],[0.0, 1.0, 0.0],[-0.7071067811865476, 1.0, 0.7071067811865476],[-0.7071067811865476, 1.0, -0.7071067811865476],[0.7071067811865476, 1.0, 0.7071067811865476],[0.7071067811865476, 1.0, -0.7071067811865476],[0.0, 1.0, -0.7071067811865475],[0.0, 1.0, 0.7071067811865475]]

# %% Partie 2 : rotation

def rotation(pt: list, theta: float, axe: str) -> 'pt rotate':
    """Effectue la rotation d'un point sur un axe précisé"""    
    # Vérifie que bon axe entré
    try:   
        # Renvoie le point tourné
        return axe(pt, radians(theta))
    # Sinon renvoie erreur        
    except Exception:
        raise Exception('Invalide axe')        

# %% Partie 3 : plan et symétrique

def miniLisse(n, pt, idx, i):
    """Mini méthode pour éviter les répétitions"""
    # Si nombre près de n
    if isclose(i, n, rtol=1e-05, atol=1e-08, equal_nan=False):
        # Devient n
        pt[idx] = n
        
def lisse(pt):
    """Lisse les coordonnées"""
    for idx, i in enumerate(pt):
        # Si nombre près de 0
        miniLisse(0, pt, idx, i)
        # Si nombre près de 1
        miniLisse(1, pt, idx, i)
        # Si nombre près de -1
        miniLisse(-1, pt, idx, i)
        # Si nombre près de sqrt(2)/2
        miniLisse(sqrt(2)/2, pt, idx, i)
        # Si nombre près de -sqrt(2)/2
        miniLisse(-sqrt(2)/2, pt, idx, i)
        
def symetrique(pt: list):
    """Renvoie le vecteur inverse"""
    return [-pt[0],-pt[1],-pt[2]]

def sommeLst(l1:list, operand:str, l2:list):
    """return l3 : l1 operand l2"""
    l3 = []
    for i, ii in zip(l1,l2):
        l3.append(eval(f'{i} {operand} {ii}'))
    return l3

def inPlan(pt:list):
    """Vérifie si le point est sur les bons plans, sinon son symétrique"""
    # Défini les plans    
    plan = {0: [-1,0,0], 1: [0,-1,0], 2: [0,0,-1]}
    # Si dotproduct(pt-ptPlan, vNormal) = 0
    if (isclose(dot(sommeLst(pt, '-', plan[0]), plan[0]), 0, rtol=1e-05, atol=1e-08, equal_nan=False) or 
        isclose(dot(sommeLst(pt, '-', plan[1]), plan[1]), 0, rtol=1e-05, atol=1e-08, equal_nan=False) or 
        isclose(dot(sommeLst(pt, '-', plan[2]), plan[2]), 0, rtol=1e-05, atol=1e-08, equal_nan=False)):
        # Renvoie son symetrique
        pt = symetrique(pt)
    # Lisse les coordonnées
    lisse(pt)
    # Renvoie le point
    return pt
            
# %% Partie 4 : main

def lstRotation(lst:list, angle, axe):
    """Applique rotation et renvoie liste"""   
    # Liste de liste des rotations
    lstRota = []
    # Applique la rotation à tous les points
    for pt in lst:
        # Rotation
        lstRota.append(inPlan(rotation(pt, angle, axe)))   
    
    # Renvoie la liste des points tournés
    return lstRota

# %%
if __name__ == '__main__':
    # pi/4
    angle = 90    
    # Défini les 3 rotations d'axes (possibles)
    axe = [mr.axeX, mr.axeY, mr.axeZ]    
    # Groupe des compositions
    groupeG = []    
    # Initialise à cas sans rotation
    rota = lstRotation(directionsPeres, 0, axe[0])
    
    #for i in tqdm(range(100)):    # Permet de voir l'avancement, mais ralenti
    for nbRotaSuite in range(1,4):
        # Compose les rotations (produit cartésien)
        for i in product(axe, repeat=nbRotaSuite):
            # Applique des n rotations successives
            for ii in i:
                # Applique rotations succesives
                rota = lstRotation(rota, angle, axe=ii)
            # !!! Ici les tests de doublons
            # Tri les vecteurs
            rota.sort()    #!!! Change tt
            if rota not in groupeG:
                # On ajoute les rotations à la liste
                groupeG.append(rota)
    #
    print(f'{len(groupeG)} rotations.')
    
