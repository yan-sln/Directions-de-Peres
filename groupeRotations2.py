# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:30:44 2023

@author: yan-s
"""
# %% On importe les fonctions nécessaires
from copy import deepcopy
from itertools import product
from numpy import radians, isclose, sqrt
from Directions_de_Peres3 import MatricesRotations as mr
from Directions_de_Peres3 import TraceDirectionsPeres as tdp

# %% On récupère la liste des 33 directions de Peres déterminée précédemment
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
    [0.0, 1.0, 0.7071067811865475]]

# %% Fonction et méthode utile
def affiche(l):
    """Méthode qui affiche la longueur d'une liste et chacun de ses éléments"""
    print(f'Il y a {len(l)} éléments qui sont : ')
    for i in l:
        print(i, end=',\n')

def miniSim(n, lst, idx, i):
    # Si nombre près de n
    if isclose(i, n, rtol=1e-05, atol=1e-08, equal_nan=False):
        # Devient n
        lst[idx] = n
        
def symetrique(l):
    """Renvoie le vecteur inverse et lisse les coordonnées"""
    lst = [-l[0],-l[1],-l[2]]
    # Permet de "lisser" les coordonnées
    for idx, i in enumerate(lst):
        # Si nombre près de 0
        miniSim(0, lst, idx, i)
        # Si nombre près de 1
        miniSim(1, lst, idx, i)
        # Si nombre près de -1
        miniSim(-1, lst, idx, i)
        # Si nombre près de sqrt(2)/2
        miniSim(sqrt(2)/2, lst, idx, i)
        # Si nombre près de -sqrt(2)/2
        miniSim(-sqrt(2)/2, lst, idx, i)
    # Renvoie la liste
    return lst

def write(l: list, file:str, mode:str) -> 'Write list in file':
    with open(file, mode) as txt:
        for i in l:
            txt.write(i, end=',\n')
            
# %% Créer une fonction qui effectue une rotation des 33 points sur un axe
def rotation(lstPoints: list, theta: float, axe: str) -> 'pt rotate':
    """ """    
    # Vérifie que bon axe entré
    try:   
        # Créer la liste des points tournés
        lstRotaPts = deepcopy(lstPoints)
        # Pour tous les points en entré
        for idx, pt in enumerate(lstRotaPts):
            # Applique la rotation
            pt = axe(pt, radians(theta))
            # Vérifie que points sur bonne face
            if pt not in lstPoints:
                # Renvoie son symétrique
                pt = symetrique(pt)
            # Ajoute à la liste
            lstRotaPts[idx] = pt
        # Renvoie la liste
        return lstRotaPts
    # Sinon renvoie erreur        
    except Exception:
        raise Exception('Invalide axe') 
        
# %%
def quitEgal(la:list, lb:list) -> bool:
    """Compare deux liste de liste de même dimension"""
    for ia, ib in zip(la, lb):
        for iia, iib in zip(ia, ib):
            if not isclose(iia, iib, rtol=1e-05, atol=1e-08, equal_nan=False):
                return False
    return True

def trace(rota, title= None):
    # Trace Cubes, vecteurs et flêches
    figure = tdp(rota, title)
    figure.traceCubes(1, None, allCubes=False)
    figure.traceFleches()
    figure.tracePoints()
    figure.affiche()

def rotaPoint(angle, nbRotaSuite, boolTrace=False):
    """ """
    # Défini les 3 rotations d'axes
    axe = [mr.axeX, mr.axeY, mr.axeZ]
    # Liste de liste des rotations
    lstRota = []
    # Créer la liste initiale à partir de la rotation nulle
    rota = rotation(directionsPeres, 0, axe[1])
    #
    for i in product(axe, repeat=nbRotaSuite):
        # Applique les 3 rotations successives
        for ii in i:
            # Créer une rotation
            rota = rotation(rota, angle, ii)
        # On ajoute les rotations à la liste
        lstRota.append(rota)
        # Puis on vérifie si elle n'existe pas déjà
        for iii in lstRota[:-1]:
            # Si elle existe déjà
            if quitEgal(rota, iii):
                # La supprime de la liste
                lstRota.remove(rota)    
        if boolTrace:
            trace(rota) # nbRotaSuite**nbRotaSuite figures
    # Renvoie la liste des rotations
    return lstRota[1:]    

# %% If main
if __name__ == '__main__':    
    # pi/4
    angle = 90    
    # Le nombre de rotations sur les 3 axes à la suite (produit cartésien)
    nbRotaSuite = 3
    
    # Forme la liste des coordonnées crées (sans rotation)
    lstRota = rotaPoint(angle, nbRotaSuite, False)
    print(f'Il y a {len(lstRota)} graphes.')
    
