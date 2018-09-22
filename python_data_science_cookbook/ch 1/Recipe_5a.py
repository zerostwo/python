# 1.Let us look at a quick example of list creation. 
a = range(1,10)
print a
b = ["a","b","c"]
print b

# 2.List can be accessed through indexing. Indexing starts at 0.
print a[0]

# 3.With negative indexing the elements of a list are accessed from backwards.
a[-1]

# 4.Slicing is accessing a subset of list by providing two indices.
print a[1:3]  # prints [2, 3]
print a[1:]   # prints [2, 3, 4, 5, 6, 7, 8, 9]
print a[-1:]  # prints [9]
print a[:-1]  # prints [1, 2, 3, 4, 5, 6, 7, 8]

#5.List concatenation
a = [1,2]
b = [3,4]
print a + b # prints [1, 2, 3, 4]

# 6.	List  min max
print min(a),max(a)

# 7.	in and not in
if 1 in a:
    print "Element 1 is available in list a"
else:
    print "Element 1 is available in tuple a"

# 8. Appending and extending list
a = range(1,10)
print a
a.append(10)
print a

# 9.List as a stack
a_stack = []

a_stack.append(1)
a_stack.append(2)
a_stack.append(3)

print a_stack.pop()
print a_stack.pop()
print a_stack.pop()

# 10.List as queue
a_queue = []

a_queue.append(1)
a_queue.append(2)
a_queue.append(3)

print a_queue.pop(0)
print a_queue.pop(0)
print a_queue.pop(0)


# 11.	List sort and reverse
from random import shuffle
a = range(1,20)
shuffle(a)
print a
a.sort()
print a

a.reverse()
print a