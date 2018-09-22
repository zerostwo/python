# -*- coding: utf-8 -*-
"""
Chapter 6 : Machine Learning - 1
Recipe    : Finding Nearest Neighbours

@author: gsubramanian
"""

from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

   

def get_train_test(x,y):
    """
    Perpare a stratified train and test split
    """
    train_size = 0.8
    test_size = 1-train_size
    input_dataset = np.column_stack([x,y])
    stratified_split = StratifiedShuffleSplit(input_dataset[:,-1],test_size=test_size,n_iter=1)

    for train_indx,test_indx in stratified_split:
        train_x = input_dataset[train_indx,:-1]
        train_y = input_dataset[train_indx,-1]
        test_x =  input_dataset[test_indx,:-1]
        test_y = input_dataset[test_indx,-1]
    return train_x,train_y,test_x,test_y
    

def build_model(x,y,k=2):
    """
    Fit a nearest neighbour model
    """
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x,y)
    return knn

def test_model(x,y,knn_model):
    y_predicted = knn_model.predict(x)
    print classification_report(y,y_predicted)
    
    
if __name__ == "__main__":

    # Load the data    
    x,y = get_data()
    
    # Scatter plot the data
    plot_data(x,y)
    
    # Split the data into train and test    
    train_x,train_y,test_x,test_y = get_train_test(x,y)
    
    # Build the model
    knn_model = build_model(train_x,train_y)
    
    # Test the model
    print "\nModel evaluation on training set"
    print "================================\n"
    test_model(train_x,train_y,knn_model)
    
    print "\nModel evaluation on test set"
    print "================================\n"
    test_model(test_x,test_y,knn_model)
    
    