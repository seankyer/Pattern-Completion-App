import numpy as np
from predictionAlgorithms import *

# Python program to take in a pattern
# and return a prediction of the next n elements
if __name__ == '__main__':
    lr_mat = lin_reg_mat_builder(np.array([["1Aa", "2Aa"], ["3Bb", "4Bb"]]))
    print(predict_at_pos(lr_mat, 2, 0))

