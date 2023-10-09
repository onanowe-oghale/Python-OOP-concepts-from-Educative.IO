sneaker1 = [8, True, "Leather", 60]

#Here in the code above the list *sneaker1* contains the value for properties:
#Size, isonSale, Material and cost 
#This approach doesn't use OOP and can lead to several problems
#The problems in brings are :
# Due to fact that it's a list you would need to remember the index of each data type 
# It is not reusable you'll have to create a new list for each item 
# Difficult to create object-specific behavior as lists can't contain methods.


# With OOP we can do this

#sneaker1 = Shoe (8, True, "leather", 60)


#define a class in python, we use the python the keyword and we put the proprerty in it

class Myclass:
    x = 4 #this is the property........

#then we can use the class Myclass to create an object like this:

p1 = Myclass()
print(p1.x)    

#Python shoe class for shoe store

class shoe:
    #define the properties and assign none value
    size = None
    isonsale = None
    material = None
    price = None


#creating objects in python: To first create an object, we can have to first set our initliazer method. The initializer method is unique and has a predefined name __int__ it also does not return any value    

"""class Shoe:
    #defines the initializer method
    def __init__(self, size, isonsale, material, price):
        self.size = size
        self.isonsale = isonsale
        self.material = material
        self.price = material
"""
#creates an object of the shoe class and sets each property to an appropriate value

# sneaker3 = shoe(11, 'false', "leather", 81)        

#creating instance methods in python-------------------------------------
#--------------------- from our previous class above we use add instance methods-------------------------------------------------

class Shoe:
    #defines the initializer method
    def __init__(self, size, isOnSale, material, price):
        self.size = size
        self.isOnSale = isOnSale
        self.material = material
        self.price = price

    #Instance method
    def printInfo(self):
        return f"This pair of shoes are size {self.size}, are made of {self.material} and costs ${self.price}" 

    #Instance method
    def putOnSale(self):
        self.isOnSale = True

sneaker3 = Shoe(11, 'false', "leather", 81)

print(sneaker3.printInfo())

#Our first instance method is printInfo that lists all properties except isOnSale

# How to use inheritance in Python------------------------

#we will add the subcategory sandal of the shoe class using the inheritance
#Child classes the classes that inherit from a parent class. The child classes do not inherit all properties and methods but can also expand or overwrite them
# expand is the addition of properties and methods of the child class that are not present in the parent, overwrite is the ability to redefine a method in a child class that has already been defined in the parent class.


#the general syntax for single class inheritance is 

"""
class Baseclass:
    Base class body

class Derivedclass(Baseclass):
    Derived class body 

# class inheritance can also have multiple class inheritance:

class Baseclass1:
    Base class1 body

class Baseclass:
    Base class2 body

class DerivedClass(Baseclass1, BaseClass2):
    Derived class body

"""
#   Sandal is the child class to parent clas shoe

class Sandal(Shoe):
    def __init__(self, size, isOnSale, material, price, waterproof):
    #inherit self, size, isOnSale,  material, price properties
        Shoe.__init__(self, size , isOnSale, material, price)
    #expands sandal to contain additional property waterproof
        self.waterproof = waterproof

#overwrites printInfo to reference "pair of sandals" rather than shoes
    def printInfo(self):
        return f"This pair of sandals are size {self.size}, are made of {self.material}, and costs ${self.price} "
    

Sandal1 = Sandal(11, False, "Leather", 81, True)

print(Sandal1.printInfo())
