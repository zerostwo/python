# Load Libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import Imputer
import numpy as np
import numpy.ma as ma

# 1. Load Iris Data Set
data = load_iris()
x = data['data']
y = data['target']

# Make a copy of hte original x value
x_t = x.copy()

# 2.	Introduce missing values into second row
x_t[2,:] = np.repeat(0,x.shape[1])
