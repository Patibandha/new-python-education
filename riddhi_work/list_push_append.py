# What is difference between push and append in list?


# Program to add data in a list through append
def list():
    l = [1, 2, 3, 4, 5]
    l.append(6)
    return l


# print("Through append: {0}".format(l))      #Output: [1, 2, 3, 4, 5, 6]


# Program to add data in a list through append

def list1():
    l = [1, 2, 3, 4, 5]
    l.insert(2, 6)
    return l


# print("Through insert/push: " + str(list1()))       #Output: [1, 2, 6 ,3, 4, 5]

"""By using append in list we can add any value at the end of the list, while by using insert/push, as shown in program
we can give an index number where we want to put that new value. For example I am adding '6' into list through append 
and insert/push."""
