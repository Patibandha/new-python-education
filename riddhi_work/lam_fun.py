# what is lambda in python give exmple of it?

'''Python allows you to create anonymous function i.e function having no names using a facility called lambda function.
lambda functions are small functions usually not more than a line. It can have any number of arguments just like a
normal function. The body of lambda functions is very small and consists of only one expression. The result of the
expression is the value when the lambda is applied to an argument. Also there is no need for any return statement
in lambda function.'''

'''For example, define a function add and pass the parameter x and y. If you want to add those two numbers, you have 
to write a logic and print the answer. While using lambda function, you can do same task in only one line. '''


def add(x, y):
    print(x + y)


add(2, 3)

print("Next result is using Lambda!!!")

print((lambda x, y: x + y)(2, 3))

print("------------------------")


# what is map, reduce and lambda in python, what are the differece between them, give example?

'''map functions expects a function object and any number of iterables like list, dictionary, etc. It executes the 
function_object for each element in the sequence and returns a list of the elements modified by the function object.
In another language, Mapping is one of the common things we do with list and other sequences is applying an operation 
to each item and collect the result.'''

items = [1, 2, 3, 4, 5]


def add(x):
    return x + 2


print(list(map(add, items)))

print("------------------------")

'''Reduces: This function reduces a list to a single value by combining elements via a supplied function. 
For example, if you want to add all numbers in a list given, then you can use reduce function. It will add all numbers 
present in that list and give single value.
The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, 
but it's not an iterator itself.'''

from functools import reduce
print(reduce( (lambda x, y: x + y), [1, 2, 3, 4] ))

print("------------------------")

# what is inline function, what are the advantage of using it?

'''Python lambda functions, also known as anonymous functions, are inline functions that do not have a name. 
They are created with the lambda keyword. This is part of the functional paradigm built-in Python.
 Inline function has following advantages: 
 1. Inline function can saves the overhead of push/pop variables on the stack when function is called.
 2. Also saves overhead of a return call from a function.'''

