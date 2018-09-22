# 1.	Create a simple list and a function similar to the
# one in functions as parameter section.
a =[10,20,30]

def do_list(a_list,func):
    total = 0
    for element in a_list:
        total+=func(element)
    return total

print do_list(a,lambda x:x**2)   
print do_list(a,lambda x:x**3)   


b =[lambda x: x%3 ==0  for x in a  ]