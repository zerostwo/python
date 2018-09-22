a = input('Input_first_seq:')
b = input('Input_second_seq:')
r = []
for i in range(len(a)):
    if a[i] != b[i]:
        r.append(i)
    
if r == []:
    print("Good!")
else:
    for i in r:
        print(i+1)
        print(a[i])
        print(b[i])        

