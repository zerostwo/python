# A simple function to examine given numpy object 
def display_shape(a):
    print 
    print a
    print
    print "Nuber of elements in a = %d"%(a.size)
    print "Number of dimensions in a = %d"%(a.ndim)
    print "Rows and Columns in a ",a.shape
    print 

display_shape(a_matrix)
