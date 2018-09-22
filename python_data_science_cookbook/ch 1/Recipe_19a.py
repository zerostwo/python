# 1.	Let us simulate a small tablular input using StringIO
import numpy as np
from StringIO import StringIO
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")

# 2.Read the input using numpy’s genfromtext to create a nummpy array.
data = np.genfromtxt(in_data,dtype=int,delimiter=",")

# cases where we may not need to use some columns.
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data,dtype=int,delimiter=",",usecols=(0,1))

# providing column names
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data,dtype=int,delimiter=",",names="a,b,c")

# using column names from data
in_data = StringIO("a,b,c\n10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data,dtype=int,delimiter=",",names=True)


