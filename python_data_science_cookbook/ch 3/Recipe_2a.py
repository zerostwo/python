# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from collections import OrderedDict
from matplotlib.pylab import frange

# 1.Load the data and handle missing values.
fill_data = lambda x : int(x.strip() or 0)
data = np.genfromtxt('president.txt',dtype=(int,int),converters={1:fill_data},delimiter=",")
x = data[:,0]
y = data[:,1]

# 2.Group data using frequency (count of individual data points).
# Given a set of points, Counter() returns a dictionary, where key is a data point,
# and value is the frequency of data point in the dataset.
x_freq = Counter(y)
x_ = np.array(x_freq.keys())
y_ = np.array(x_freq.values())
