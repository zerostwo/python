# 1.	Let us define a simple class with __iter__ method.
class SimpleIterable(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for x in range(self.start,self.end):
            yield x**2

#  Now let us invoke this class and iterate over its values two times.
c = SimpleIterable(1,10)

# First iteration
tot = 0
for val in iter(c):
    tot+=val

print tot

# Second iteration
tot =0
for val in iter(c):
    tot+=val

print tot
    
