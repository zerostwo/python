def my_gen(low,high):
    for x in range(low,high):
        yield x**2

tot = 0     
   
for val in my_gen(1,10):
    tot+=val
print tot    
