# %% On importe les fonctions nécessaires
from itertools import combinations
from numpy import cross, isclose, radians
from Peres33Directions import MatricesRotations as mr

# %% On récupère la liste des 33 directions de Peres déterminées précédemment
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
        
def symetrique(l):
    """Renvoie le vecteur inverse"""
    return [[-l[0],-l[1],-l[2]]]

# %% Créer une fonction qui effectue une rotation des 33 points sur un axe
def rotaPoint(lstPoints: list, theta: float, axe: str) -> 'pt rotate':
    """ """      
    # Créer la liste des points tournés
    lstRotaPts = []
    # Pour tous les points en entré
    for pt in lstPoints:
        # Applique la rotation
        pt = axe(pt, radians(theta))
        # Vérifie que points sur bonne face
        if pt not in lstPoints:
            print(pt)
            # Renvoie son symétrique
            pt = symetrique(pt)
        # Ajoute à la liste
        lstRotaPts.append(pt)
    # Renvoie la liste
    return lstRotaPts
    

# %% If main
if __name__ == '__main__':
    rotaPoint(directionsPeres, 90, mr.axeX)
    
