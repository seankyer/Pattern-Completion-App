import numpy as np


# Rotates a matrix A such that
#
# |1 2|  _  |1 3|
# |3 4|  -  |2 4|
#
def rotate_matrix(mat):
    rot_mat = [["" for col in range(len(mat))] for row in range(len(mat[0]))]
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            rot_mat[col][row] = mat[row][col]
    return np.array(rot_mat)


# Used for converting letters to an adjusted ASCII value
def to_base26(letter, offset):
    return ord(letter) - offset


# Used to process letters from adj ASCII to Characters
def letters_from_base26(val, offset):
    out = ""
    last_ele = False
    while not last_ele:
        out = chr(val % 26 + offset) + out
        last_ele = val <= 26
        val = int((val - (val % 26)) / 26)
    return out