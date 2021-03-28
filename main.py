import numpy as np
from predictionAlgorithms import *


def generate_pred(lis, rep):
    rows = len(lis)
    cols = len(lis[0])
    temp_lis = []
    for ele in lis:
        if [str(i) for i in ele if i]:
            temp_lis.append([str(i) for i in ele if i])
    if not temp_lis:
        return lis
    # mat = np.array(temp_lis)
    mat = np.array([np.array(xi) for xi in temp_lis])
    out = [["" for col in range(cols)] for row in range(rows)]
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
