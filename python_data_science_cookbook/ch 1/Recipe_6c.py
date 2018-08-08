def process(x):
    if isinstance(x,str):
        return x.lower()
    elif isinstance(x,int):
        return x*x
    else:
        return -9

a = (1,2,-1,-2,'D',3,4,-3,'A')
b = tuple(process(x) for x in a )

print b
