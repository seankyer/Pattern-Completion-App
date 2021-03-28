import numpy as np
from predictionAlgorithms import *

# Python program to take in a pattern
# and return a prediction of the next n elements
if __name__ == '__main__':
    mat = np.array([["1A-a", "2A-a"], ["3B-b", "4B-b"]])
    lr_mat = lin_reg_mat_builder(mat)
    print(predict_at_pos(lr_mat, 2, 0))

