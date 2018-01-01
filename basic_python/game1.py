#提示输入剪刀石头布
while True:
    import random
    me = input('请输入剪刀(y)、石头(o)或者布(b):')
    com = random.randint(1,3)
    if com == 1:
        com = 'y'
        if com == me:
            print('平局')
        elif me == 'o':
            print('你输了')
        else:
            print('你赢了')
    elif com == 2:
        com = 'o'
        if com == me:
            print('平局')
        if me == 'b':
            print('你赢了')
        else:
            print('你输了')
    else:
        com = 'b'
        if com == me:
            print('平局')
        elif me == 'o':
            print('你赢了')
        else:
            print('你输了')
