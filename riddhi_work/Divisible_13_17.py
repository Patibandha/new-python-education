# Number is divisible by 13 and 17 in a range of 100 to 50000

def div(one, two):
    l = []
    if one>0 and two>0:
        try:
            for num in range(one, two+1):
                if (num % 13 == 0) and (num % 17 == 0):
                    l.append(num)
            return l
        except(TypeError):
            return 'The value is suppose to be positive number, not string'
    else:
        return 'The value is suppose to be positive, not negative.'
print(div(100, 50000))