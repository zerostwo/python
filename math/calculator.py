class Calculator:
    name = 'Good Calculator'
    price = 18
    
    def add(self,x,y):
        print(self.name)
        result = x+y
        print(result)

    def minus(self,x,y):
        print(self.name)
        result = x-y
        print(result)

    def times(self,x,y):
        print(self.name)
        result = x*y
        print(result)

    def divide(self,x,y):
        print(self.name)
        result = x/y
        print(result)

cal = Calculator()

cal.name
cal.add(1,1)
cal.minus(1,1)
cal.times(1,1)
cal.divide(1,1)

