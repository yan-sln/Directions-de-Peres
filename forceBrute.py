# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:20:01 2023

@author: yan-s
"""
from tqdm import tqdm

def forceBrute(n: int) -> str:
    """Parcourt les applications ϒ : Ρ → {0;1}"""
    for i in tqdm(range(100)):
        for i in range(1, (2**n)+1):
            with open('forceBrute.txt', 'a') as ap:
                    ap.write(f'{bin(i).replace("0b", "")}\n')
forceBrute(33)
