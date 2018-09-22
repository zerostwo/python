# -*- coding: utf-8 -*-
"""
Chapter 6 : Machine Learning - 1
Recipe    : Using Naive Bayes Classifier

@author: gsubramanian
"""

from nltk.corpus import movie_reviews
from sklearn.cross_validation import StratifiedShuffleSplit
import nltk
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


def get_data():
    """
    Get movie review data
    """
    dataset = []
    y_labels = []
    # Extract categories
    for cat in movie_reviews.categories():
        # for files in each cateogry    
        for fileid in movie_reviews.fileids(cat):
            # Get the words in that category
            words = list(movie_reviews.words(fileid))
            dataset.append((words,cat))
            y_labels.append(cat)
    return dataset,y_labels


def get_train_test(input_dataset,ylabels):
    """
    Perpare a stratified train and test split
    """
    train_size = 0.7
    test_size = 1-train_size
    stratified_split = StratifiedShuffleSplit(ylabels,test_size=test_size,n_iter=1,random_state=77)

    for train_indx,test_indx in stratified_split:
        train   = [input_dataset[i] for i in train_indx]
        train_y = [ylabels[i] for i in train_indx]
        
        test    = [input_dataset[i] for i in test_indx]
        test_y  = [ylabels[i] for i in test_indx]
    return train,test,train_y,test_y

