# wap to take string and print number of occurance of numerical value and alphabet in a string.

def count(string):
    count1 = 0  # type: int
    count2 = 0
    for i in string:
        if (i.isdigit()):
            count1 = count1 + 1

        else:
            count2 = count2 + 1

    return [count1, count2]


count('R1234R')

