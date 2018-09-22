from sklearn.datasets import make_classification
from sklearn.metrics import  classification_report
from sklearn.preprocessing import scale
import numpy as np

def get_data(batch_size):
    """
    Make a sample classification dataset
    Returns : Independent variable y, dependent variable x
    """
    b_size = 0
    no_features = 30
    redundant_features = int(0.1*no_features)
    informative_features = int(0.8*no_features)
    repeated_features = int(0.1*no_features)

    while b_size < batch_size:
        x,y = make_classification(n_samples=1000,n_features=no_features,flip_y=0.03,\
                n_informative = informative_features, n_redundant = redundant_features \
                ,n_repeated = repeated_features, random_state=51)
        y_indx = y < 1
        y[y_indx] = -1
        x = scale(x,with_mean=True,with_std=True)

        yield x,y
        b_size+=1
