# W.a.p.to find even number 0 to 10000(both included)

def even(one, two):
    l = []
    try:
        for num in range(one, two+1):
            if num % 2 == 0:
                l.append(num)
        return l
    except(TypeError):
        return 'The value is suppose to be positive number, not string'

print(even(0, 10000))