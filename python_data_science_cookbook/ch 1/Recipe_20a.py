import numpy as np
from StringIO import StringIO

# Define a data set
in_data = StringIO("30kg,inr2000,31.11,56.33,1\n52kg,inr8000.35,12,16.7,2")

# 1.Let us define two data pre-processing using lambda functions,
strip_func_1 = lambda x : float(x.rstrip("kg"))
strip_func_2 = lambda x : float(x.lstrip("inr"))

# 2.Let us now create a dictionary of these functions,
convert_funcs = {0:strip_func_1,1:strip_func_2}

# 3.Now provide this dictionary of functions to genfromtxt.
data = np.genfromtxt(in_data,delimiter=",", converters=convert_funcs)

# Using a lambda function to handle conversions
in_data = StringIO("10,20,30\n56,,90\n33,46,89")
mss_func = lambda x : float(x.strip() or -999)
data = np.genfromtxt(in_data,delimiter=",", converters={1:mss_func})
    