# What is OOP? What are the OOP concept for python? explain with programming.


'''1. Abstraction: Means keeping necessary while hiding unnecessary.
 For example, if you want to add two numbers. And also you want to hide the operation from whole program. We can just
make a class here Add, in it define a function named here as "addition". Write an operation. And now out of the class
try to pass values to your function directly like y = addition(2, 3). It will give you a NameError. Because the
addition function is defined under the class. That is why to access the addition function you have to give
access to it like y = add.addition(2,3). Which is called as Abstraction.'''

class Add():
    def addition(self, x, y):
        return x+y

add = Add()
y = add.addition(2, 3)
print(y)

print("---------------")

'''2. Encapsulation: To hide any object, in program. In an object oriented python program, you can restrict access
to methods and variables. This can prevent the data from being modified by accident and is known as encapsulation
In the program below, if someone want to change the tagname, they need to set it first and then they can print it
through get function.'''


class Honeywell():

    def __init__(self):
        self.__tagname = 1234

    def getTag(self):
        print("Tagname: {}".format(self.__tagname))

    def setTag(self, name):
        self.__tagname = name


CS = Honeywell()
CS.getTag()     # This will print the Initial tagname which we have defined in __init__
# print("----------------")

CS.__tagname = 5678
CS.getTag()     # Here we are trying to reassign a new tagname, but as CS.getTag() does not have privilege to take a
                # value, that is why it will print the initial value 1234.
# print("----------------")

CS.setTag(5678) # And over here we are setting the tagname as 5678 and then getting it through CD.getTag()
CS.getTag()
print("----------------")

'''3. Polymorphism: In object-oriented programming, polymorphism refers to a programming language's ability to process 
objects differently depending on their data type or class. More specifically, it is the ability to redefine methods 
for derived classes. In simple language, Poly means number of something. We can use same function for different 
purposes. By defining same function in different classes. In the example below, I have tried to print fly function 3
times with different class name. Due to the different behavior of same function in different class, we have different 
result. '''

class Bird():
    def walk(self):
        print("Birds can walk...")

    def fly(self):
        print("Birds can fly...")

    def swim(self):
        print("Birds can not swim...")


class Animal():
    def walk(self):
        print("Animal can walk...")

    def fly(self):
        print("Animal can not fly...")

    def swim(self):
        print("Some animal can swim...")


class Fish():
    def walk(self):
        print("Fish can not walk...")

    def fly(self):
        print("Fish can not fly...")

    def swim(self):
        print("Fish can swim...")

bird = Bird()
bird.fly()

ani = Animal()
ani.fly()

fish = Fish()
fish.fly()

print("----------------")


'''4. Inheritance: Inheritance is the process by which one object gets the properties of the other object. 
Class from which the properties are inherited is called base/parent class and class inheriting the properties is 
called derived/child class. 
In the example below I have a parent class named as Animal and two child class named as Leapord and Cat. And because 
of we have inherited Animal class into Cat, we can pass value of name and color directly to class Cat. Same for class 
Leapord.'''


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Leapord(Animal):
    def big(self):
        print("Big Cat...")


class Cat(Animal):
    def small(self):
        print("Small cat")


mini = Cat("Mini", "White")
print(mini.color)
mini.small()

leo = Leapord("Leo", "Brown")
print(leo.name)
leo.big()

'''5. Association: Association defines a relationship between classes of objects 
that allows one object instance to cause another to perform an action on its behalf.'''


'''6. Aggregation: A relationship where the child can exist independently of the parent. 
Example: Class (parent) and Student (child). Delete the Class and the Students still exist.  '''


'''7. Composition: A relationship where the child cannot exist independent of the parent. 
Example: House (parent) and Room (child). Rooms don't exist separate to a House.'''

