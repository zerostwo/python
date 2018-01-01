#condtion user
names = []
while True:
    print('='*50)
    print('welcome to use XXXX v6.9')
    print('1:add new name')
    print('2:remove name')
    print('3:set name')
    print('4:search name')
    print('5:all name')
    print('0:exit')
    print('='*50)

    #get number
    key = input('please input your choose:')

    #def list, save all name

    #according to choose, do
    if key == 1:
        inser_name = input("please input your name:")
        names.append(inser_name)
    elif key == 2:
        remove_name = input('please input name you want to remove:')
        names.remove(remove_name)
    elif key == 3:
        print(name)


