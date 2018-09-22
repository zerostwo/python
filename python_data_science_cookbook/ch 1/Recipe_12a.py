from math import log

def square_input(x):
    return x*x

# 1.	Define a generic function, which will take another function as input
# and will apply it on the given input sequence.
def apply_func(func_x,input_x):
    return map(func_x,input_x)
    
# Let us try to use the apply_func() and verify the results  
a = [2,3,4]

print apply_func(square_input,a)
print apply_func(log,a)    