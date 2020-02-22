names = ['duansongqi','']
inser_name = input('please input your name:')

if inser_name in names:
    print('yes')
else:
    print('no')
    names.append(inser_name)
print(names)

