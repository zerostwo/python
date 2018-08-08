# Load libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import scale
import numpy as np
import matplotlib.pyplot as plt

# 1. Load iris dataset
data = load_iris()
x = data['data']
y = data['target']
col_names = data['feature_names']

# 2. Scale the variables, with mean value
x = scale(x,with_std=False)
x_ = x[1:26,]
y_labels = range(1,26)