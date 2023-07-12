import numpy as np


def normalization(list):
    print(np.max(list))
    print(np.min(list))
    newlist = []
    for i in list:
        newlist.append((i - np.min(list)) / (np.max(list) - np.min(list)))


list = [5, 13, 21, 0.2]
normalization(list)
