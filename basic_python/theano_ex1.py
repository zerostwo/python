import theano 
import theano.tensor as T 
import numpy as np

x=T.dmatrix('x')
y=T.dmatrix('y')
z=x+y
add=theano.function([x,y],z)
num=add(1,2)
print(num)

