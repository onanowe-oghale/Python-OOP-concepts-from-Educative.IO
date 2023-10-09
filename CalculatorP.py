#Building a calculator with the use of OOP

class Calculator:
    #the very first initializer for the two numbers

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print (self.num1 - self.num2)

    def multiply(self):
        print (self.num1 * self.num2)

    def divide(self):
        print (self.num1 / self.num2)     


solved = Calculator(23, 18)
solved.add()
solved.subtract()
solved.multiply()
solved.divide()        