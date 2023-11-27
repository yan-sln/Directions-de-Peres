# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:00:18 2023

@author: yan-s
"""

def intersection(A, B, C, D):    
    """Tel que [AB] et [CD] des segments"""
    u=((C[0]-A[0])*(C[1]-D[1])-(C[1]-A[1])*(C[0]-D[0]))/((C[1]-D[1])*(B[0]-A[0])-(C[0]-D[0])*(B[1]-A[1]))
    v=((B[1]-A[1])*(C[0]-A[0])-(B[0]-A[0])*(C[1]-A[1]))/((B[1]-A[1])*(C[0]-D[0])-(B[0]-A[0])*(C[1]-D[1]))
    # Vérifie 3e équation
    if ((u*(B[2]-A[2])+v*(C[2]-D[2]))==C[2]-A[2]):
        # Se croisent
        if(0<=u<=1 and 0<=v<=1):return True
        # Se croisent en leurs origines
        else:return False
    else:return False
