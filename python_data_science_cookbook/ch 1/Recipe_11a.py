# 1.	Let us define a function of function to find the sum of squares of the given input
def sum_square(x):
    def square_input(x):
        return x*x
    return sum([square_input(x1) for x1 in x])

# Print the output to check for correctness
print sum_square([2,4,5])    
