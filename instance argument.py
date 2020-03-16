# Creating a class name as demo
class demo:

    a = 0
    b = 0

    # Initialising or defining a function as init
    def __init__(self):
        self.a = 5
        self.b = 10

    # Initialising or defining a function
    def display(self):
        print("a = ", self.a)
        print("b = ", self.b)


# Creating a class name as demo1
class demo1:

    x = 0
    y = 0

    # Using setter for demo
    def data(self, demo):
        self.x = demo.a
        self.y = demo.b

    # It reads x & y from above function inti
    def display1(self):
        print("x = ", self.x)
        print("y = ", self.y)

# Calling an above function
d1 = demo()
d1.display()
d2 = demo1()
d2.data(d1)
d2.display1()
