import numpy as np
from scipy import stats
import re
from PredictionAlgorithms import *
from PatternProcessing import *


def is_valid_seq(seq_mat):
    seq_list = seq_mat.copy().flatten()
    seq_type = ""
    for pos in range(len(seq_list)):
        if seq_type == "":
            seq_type = build_type(seq_list[pos])
        elif seq_type != build_type(seq_list[pos]):
            return False
    return seq_type


# Rotates a matrix A such that
#
# |1 2|  _  |1 3|
# |3 4|  -  |2 4|
#
def rotated_matrix(A):
    rot_mat = [["" for col in range(len(A))] for row in range(len(A[0]))]
    for row in range(len(A)):
        for col in range(len(A[0])):
            rot_mat[col][row] = A[row][col]
    return np.array(rot_mat)


def pattern_growth(A):
    m = []
    for row in range(len(A)):
        m.append(lin_reg_nums(A[row]))
    if m.count(m[0].slope) == len(m) and m[0].slope != 0:
        return("Horizontal")
    B = rotated_matrix(A)
    m = []
    for row in range(len(B)):
        m.append(lin_reg_nums(B[row]))
    if m.count(m[0].slope) == len(m) and m[0].slope != 0:
        return("Vertical")
    return("None")


def has_valid_regs(A, s_t):
    for i in range(len(s_t)):
        reg = ""
        for row in range(len(A)):
            if s_t[i] == "C":
                if reg == "":
                    reg = lin_reg_letters([l[1:] for l in parse_pattern(s_t, A[row])][i], 65)
                else:
                    if reg.slope != lin_reg_letters([l[1:] for l in parse_pattern(s_t, A[row])][i], 65).slope:
                        return False
            elif s_t[i] == "L":
                if reg == "":
                    reg = lin_reg_letters([l[1:] for l in parse_pattern(s_t, A[row])][i], 97)
                else:
                    if reg.slope != lin_reg_letters([l[1:] for l in parse_pattern(s_t, A[row])][i], 97).slope:
                        return False
            elif s_t[i] == "N":
                if reg == "":
                    reg = lin_reg_nums([l[1:] for l in parse_pattern(s_t, A[row])][i])
                else:
                    if reg.slope != lin_reg_nums([l[1:] for l in parse_pattern(s_t, A[row])][i]).slope:
                        return False
    return True


def linreg_mat_builder(A):
    s_t = is_valid_seq(A)
    if not s_t:
        return False
    t = [[char]for char in s_t]
    B = rotated_matrix(A)
    if not (has_valid_regs(A, s_t) and has_valid_regs(B, s_t)):
        return False
    for pos in range(len(t)):
        if t[pos][0] == "C":
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, A[0])][pos], 65))
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, B[0])][pos], 65))
        elif t[pos][0] == "L":
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, A[0])][pos], 97))
            t[pos].append(lin_reg_letters([l[1:] for l in parse_pattern(s_t, B[0])][pos], 97))
        elif t[pos][0] == "N":
            t[pos].append(lin_reg_nums([l[1:] for l in parse_pattern(s_t, A[0])][pos]))
            t[pos].append(lin_reg_nums([l[1:] for l in parse_pattern(s_t, B[0])][pos]))
    return t


def predict_at_pos(A, r, c):
    out = ""
    for row in range(len(A)):
        val = int(A[row][1].slope * c + A[row][1].intercept + A[row][2].slope * r)
        if A[row][0] == "C":
            out += str(letters_from_base26(val, 65))
        elif A[row][0] == "L":
            out += str(letters_from_base26(val, 97))
        else:
            out += str(val)
    return out


lr_mat = linreg_mat_builder(np.array([["1Aa", "2Aa"], ["3Bb", "4Bb"]]))
print(predict_at_pos(lr_mat, 2, 0))
