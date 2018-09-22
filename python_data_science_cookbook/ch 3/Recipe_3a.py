# Load Librarires
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import itertools

# 1. Load Iris dataset
data = load_iris()
x = data['data']
y = data['target']
col_names = data['feature_names']