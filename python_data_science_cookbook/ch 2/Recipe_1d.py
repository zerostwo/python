# Create a matrix will all elements as 1
ones_matrix = np.ones((3,3))
display_shape(ones_matrix)

# Create a matrix with all elements as 0
zeros_matrix = np.zeros((3,3))
display_shape(zeros_matrix)

# Identity matrix
# k parameter  controls the index of 1
# if k =0, (0,0),(1,1,),(2,2) cell values
# are set to 1 in a 3 x 3 matrix
identity_matrix = np.eye(N=3,M=3,k=0)
display_shape(identity_matrix)
identity_matrix = np.eye(N=3,k=1)
display_shape(identity_matrix)
