# 2.	Define a function, which can perform min max scaling given a list of numbers
def min_max(x):
    return [round((xx-min(x))/(1.0*(max(x)-min(x))),2) for xx in x]

# 3.	Perform scaling on the given input list.    
print x 
print min_max(x)    
