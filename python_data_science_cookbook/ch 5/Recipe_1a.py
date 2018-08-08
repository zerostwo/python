"""
Chapter 5 : Data Mining - Needle in a Haystack
Recipe    : Preparing data for model building

@author: gsubramanian
"""

import numpy as np

def euclidean_distance(x,y):
    if len(x) == len(y):
        return np.sqrt(np.sum(np.power((x-y),2)))
    else:
        print "Input should be of equal length"
    return None


def lrNorm_distance(x,y,power):
    if len(x) == len(y):
        return np.power(np.sum (np.power((x-y),power)),(1/(1.0*power)))
    else:
        print "Input should be of equal length"
    return None


def cosine_distance(x,y):
    if len(x) == len(y):
        return np.dot(x,y) / np.sqrt(np.dot(x,x) * np.dot(y,y))
    else:
        print "Input should be of equal length"
    return None


def jaccard_distance(x,y):
    set_x = set(x)
    set_y = set(y)
    return 1 - len(set_x.intersection(set_y)) / len(set_x.union(set_y))


def hamming_distance(x,y):
    diff = 0
    if len(x) == len(y):
        for char1,char2 in zip(x,y):
            if char1 != char2:
                diff+=1
        return diff
    else:
        print "Input should be of equal length"
    return None
