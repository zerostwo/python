names = ['duansongqi','taoxinyu','lijinwen']
insert_name = input('请输入你的名字：')
num = 0
for i in names:
    if i == insert_name:
        num = 1
if num == 1:
    print ('找到了')
else:
    print('没找到')

    names.append(insert_name)
print(names)

