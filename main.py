import numpy as np
from predictionAlgorithms import *

# Python program to take in a pattern
# and return a prediction of the next n elements
if __name__ == '__main__':
    mat = np.array([["1A-a", "2A-a"], ["3B-b", "4B-b"]])
    print(predict_at_pos(mat, 2, 0))
    # print(len(mat) == 1)
    # print(all([len(ele) == 1 for ele in mat]))

