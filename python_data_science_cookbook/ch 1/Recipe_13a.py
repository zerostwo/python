# 1.	Let us define a function which will explain our
#  concept of function returning a function.
def cylinder_vol(r):
    pi = 3.141
    def get_vol(h):
        return pi * r**2 * h
    return get_vol

# 2.	Let us define a radius and find get a volume function,
#  which can now find out the volume for the given radius and any height.
radius = 10
find_volume = cylinder_vol(radius)

# 3.	Let us try to find out the volume for different heights
height = 10
print "Volume of cylinder of radius %d and height %d = %.2f  cubic units" \
                %(radius,height,find_volume(height))        

height = 20
print "Volume of cylinder of radius %d and height %d = %.2f  cubic units" \
                %(radius,height,find_volume(height))        
    