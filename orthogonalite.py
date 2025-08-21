# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:48:52 2023

@author: yan-s
"""

import numpy as np

def is_orthogonal(*vectors, rtol=1e-5, atol=1e-8):
    """
    Check generalized orthogonality of two or more vectors.

    Definition:
        For vectors u, v, w, ... in R^n:
        sum = Σ (u_i * v_i * w_i * ...)
        If sum ≈ 0, return True.

    - For 2 vectors: reduces to standard dot product.
    - For 3+ vectors: generalized "n-orthogonality".

    Parameters
    ----------
    *vectors : list of lists or numpy arrays
        Input vectors, all must have the same dimension.
    rtol : float
        Relative tolerance for zero-check (default=1e-5).
    atol : float
        Absolute tolerance for zero-check (default=1e-8).

    Returns
    -------
    bool
        True if generalized inner product is close to 0, else False.

    Raises
    ------
    ValueError
        If vectors have different dimensions or fewer than 2.
    """
    if len(vectors) < 2:
        raise ValueError("At least two vectors are required.")

    arr = np.array(vectors, dtype=float)
    if arr.ndim != 2:
        raise ValueError("Invalid input: all vectors must have same dimension.")

    result = np.sum(np.prod(arr, axis=0))
    return np.isclose(result, 0.0, rtol=rtol, atol=atol)
