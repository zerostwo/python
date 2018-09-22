# Load libraries
import numpy as np
from matplotlib.pylab import frange
import matplotlib.pyplot as plt

fill_data = lambda x : int(x.strip() or 0)
data = np.genfromtxt('president.txt',dtype=(int,int),converters={1:fill_data},\
            delimiter=",")
x = data[:,0]
y = data[:,1]


# 2.Plot the data to look for any trends or values
plt.close('all')
plt.figure(1)
plt.title("All data")
plt.plot(x,y,'ro')
plt.xlabel('year')
plt.ylabel('No Presedential Request')
