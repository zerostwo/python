# -*- coding: utf-8 -*-
"""
Chapter 6 : Machine Learning - 1
Recipe    : Preparing data for model building

@author: gsubramanian
"""

# Load the necesssary Library
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
import numpy as np

def get_iris_data():
    """
    Returns Iris dataset
    """
    # Load iris dataset
    data = load_iris()
    
    # Extract the dependend and independent variables
    # y is our class label
    # x is our instances/records
    x    = data['data']
    y    = data['target']
    
    # For ease we merge them
    # column merge
    input_dataset = np.column_stack([x,y])

    # Let us shuffle the dataset
    # We want records distributed randomly
    # between our test and train set
    
    np.random.shuffle(input_dataset)

    return input_dataset

# We need  80/20 split.
# 80% of our records for Training
# 20% Remaining for our Test set
train_size = 0.8
test_size  = 1-train_size

# get the data
input_dataset = get_iris_data()
# Split the data
train,test = train_test_split(input_dataset,test_size=test_size)

# Print the size of original dataset
print "Dataset size ",input_dataset.shape
# Print the train/test split
print "Train size ",train.shape
print "Test  size",test.shape

