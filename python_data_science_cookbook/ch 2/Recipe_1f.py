# Matrix operations
a_matrix = np.arange(9).reshape(3,3)
b_matrix = np.arange(9).reshape(3,3)

# Addition
c_matrix = a_matrix + b_matrix

# Element wise multiplication
d_matrix = a_matrix * b_matrix

# matrix multiplication
e_matrix = np.dot(a_matrix,b_matrix)

# matrix tranpsose
f_matrix = e_matrix.T

# min,max,sum
print
print "f_matrix,minimum = %d"%(f_matrix.min())
print "f_matrix,maximum = %d"%(f_matrix.max())
print "f_matrix, col sum",f_matrix.sum(axis=0)
print "f_matrix, row sum",f_matrix.sum(axis=1)
