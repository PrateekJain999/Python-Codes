class Car:

    def __init__(self):
        self.__Speed = 30

    def sell(self):
        print("Selling Price: =",self.__Speed)

    def setMaxSpeed(self, price):
        self.__Speed = price

c = Car()
c.sell()

# change the price
c.__Speed = 40
c.sell()

# using setter function
c.setMaxSpeed(60)
c.sell()