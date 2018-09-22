# Load libraries
from itertools import chain,compress,combinations,count,izip,islice

# 1.Chain example, where different iterables can be combined together.
a = [1,2,3]
b = ['a','b','c']
print list(chain(a,b)) # prints [1, 2, 3, 'a', 'b', 'c']

# 2.Compress example, a data selector, where the data in the first iterator
#  is selected based on the second iterator.
a = [1,2,3]
b = [1,0,1]
print list(compress(a,b)) # prints [1, 3]

# 3.From a given list, return n length sub sequences.
a = [1,2,3,4]
print list(combinations(a,2)) # prints [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# 4.A counter which produces infinite consequent integers, given a start integer,
a = range(5)
b = izip(count(1),a)
for element in b:
    print element

# 5.	Extract an iterator from another iterator, 
# let us say we want an iterator which only returns every 
# alternate elements from the input iterator
a = range(100)
b = islice(a,0,100,2)
print list(b)
