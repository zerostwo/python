# reversing elements
display_shape(f_matrix[::-1])

# Like python all elements are used by reference
# if copy is needed copy() command is used
f_copy = f_matrix.copy()

# Grid commands
xx,yy,zz = np.mgrid[0:3,0:3,0:3]
xx = xx.flatten()
yy = yy.flatten()
zz = zz.flatten()
