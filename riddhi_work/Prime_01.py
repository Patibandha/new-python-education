# Find the prime numbers between 0 to 500

def prime(one, two):
    l = []
    if one >= 0 and two > 0:
        try:
            for num in range(one, two + 1):
                if num > 1:
                    for z in range(2, num):
                        if num % z == 0:
                            break
                    else:
                        l.append(num)
            return l
        except(TypeError):
            err = 'The value is suppose to be positive number, not string'
            return err
    else:
        return 'The value is suppose to be positive, not negative.'
print(prime(0, 500))
