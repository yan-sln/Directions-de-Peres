# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:48:52 2023

@author: yan-s
"""

from numpy import isclose

def orthogonalite(*arg):
    """ u​⃗​​.​v​⃗​​=xx​′​​x′′... + ... + nn​′n′′...​​ """
    # Vérifie s'il y a au moins 2 vecteurs, et qu'ils soient de même taille
    if all([True if len(i) == len(arg[0]) else False for i in arg]) and len(arg) >= 2:
        somme = 0    
        for i in range(len(arg[0])):
            facteur = 1
            for ii in arg:
                facteur *= ii[i]
            somme += facteur            
        if isclose(somme, 0, rtol=1e-05, atol=1e-08, equal_nan=False):return True
        else:return False
    else:return False
