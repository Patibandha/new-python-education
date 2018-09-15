# What is different of while and for loop? which one is fast & why ? Write program for example.

# A program using While loop
import datetime

a = datetime.datetime.now()


def While(i):
    while i <= 1000000:
        print(i)
        i = i + 1


i = While(1)
b = datetime.datetime.now()


# A program using for loop
c = datetime.datetime.now()


def For(one, two):

    for num in range(one, two+1):
        print(num)


print(For(0, 1000000))
d = datetime.datetime.now()


# Comparision between Elapsed time of while and for loop.
print("Elapsed time for while loop = " + str(b-a))
print("Elapsed time for for loop = " + str(d-c))

wh = b-a
fo = d-c
if wh < fo:
    print("While loop is faster than for loop...")
else:
    print("For loop is faster than while loop...")


""" According to program, it is almost similar time taking to run. There are few microsecondes difference. 
While loop is faster than for loop as in while loop it just have to check one condition 
and untill that condition is True that loop is continue running."""
