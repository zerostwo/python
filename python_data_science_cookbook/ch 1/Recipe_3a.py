# 1.Ways of creating a tuple
a_tuple = (1,2,'a')
b_tuple =1,2,'c'

# 2.Accessing elements of a tuple through index
print b_tuple[0]
print b_tuple[-1]

# 3.It is not possible to change the value of an item in a tuple,
# for example the next statement will result in an error.
try:
    b_tuple[0] = 20
except:
    print "Cannot change value of tuple by index"    

# 4.Though tuples are immutable
# But elements of a tuple can be mutable objects,
# for instance a list, as in the following line of code
c_tuple =(1,2,[10,20,30])
c_tuple[2][0] = 100

# 5.Tuples once created cannot be extended like list, 
# however two tuples can be concatenated.

print a_tuple + b_tuple

# 6 Slicing of uples
a =(1,2,3,4,5,6,7,8,9,10)
print a[1:]
print a[1:3]
print a[1:6:2]
print a[:-1]

# 7.Tuple min max
print min(a),max(a)

# 8.in and not in
if 1 in a:
    print "Element 1 is available in tuple a"
else:
    print "Element 1 is available in tuple a"
