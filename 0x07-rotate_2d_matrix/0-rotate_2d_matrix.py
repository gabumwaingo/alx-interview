#!/usr/bin/python3
"""
Rotates a 2d matrix by 90deg clockwise
by iterating through layers and swaping the elements
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            """ save top """
            top = matrix[first][i]

            """ left -> top """
            matrix[first][i] = matrix[last - offset][first]

            """ bottom -> left """
            matrix[last - offset][first] = matrix[last][last - offset]

            """ right -> bottom """
            matrix[last][last - offset] = matrix[i][last]

            """ top -> right """
            matrix[i][last] = top
