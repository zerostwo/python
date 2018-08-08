# -*- coding: utf-8 -*-
"""
Chapter 6 : Machine Learning - 1
Recipe    : Buildign decision trees for multi-class problems.

@author: gsubramanian
"""

from sklearn.datasets import load_iris
from sklearn.cross_validation import StratifiedShuffleSplit
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import pprint

def get_data():
    """
    Get Iris data
    """
    data = load_iris()
    x = data['data']
    y = data['target']
    label_names = data['target_names']
    
    return x,y,label_names.tolist()
    

def get_train_test(x,y):
    """
    Perpare a stratified train and test split
    """
    train_size = 0.8
    test_size = 1-train_size
    input_dataset = np.column_stack([x,y])
    stratified_split = StratifiedShuffleSplit(input_dataset[:,-1], \
            test_size=test_size,n_iter=1,random_state = 77)

    for train_indx,test_indx in stratified_split:
        train_x = input_dataset[train_indx,:-1]
        train_y = input_dataset[train_indx,-1]
        test_x =  input_dataset[test_indx,:-1]
        test_y = input_dataset[test_indx,-1]
    return train_x,train_y,test_x,test_y

