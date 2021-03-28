import numpy as np
import itertools as it
from predictionAlgorithms import *


def generate_pred(lis, rep):
    rows = len(lis)
    cols = len(lis[0])
    temp_list = []
    for ele in lis:
        if [str(i) for i in ele if i]:
            temp_list.append([str(i) for i in ele if i])
    if not temp_list:
        return lis
    # mat = np.array([np.array(xi) for xi in temp_list])
    out = [["" for col in range(cols)] for row in range(rows)]
    # print(temp_list)
    # print(mat)
    mat = np.array(list(it.zip_longest(*temp_list))).T # https://sukhbinder.wordpress.com/2018/07/24/variable-length-list-to-numpy-array/
    for row in range(rows):
        for col in range(cols):
            if not predict_at_pos(mat, row, col):
                return False
            else:
                out[row][col] = predict_at_pos(mat, row, col)
    return out


# Python program to take in a pattern
# and return a prediction of the next n elements
# if __name__ == '__main__':
    # mat = np.array([["1A-a", "2A-a"], ["3B-b", "4B-b"]])
    # print(predict_at_pos(mat, 2, 0))
