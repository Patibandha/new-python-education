#regular prime program using list
#def prim(min, max):
#    ls_num = []
#    for num in range(min, max + 1):
#        if num > 1:
#            for j in range(2, num):
#                if num % j == 0:
#                    break
#            else:
#                ls_num.append(num)
#    return ls_num

#x = prim(500,10000)

#print(x)

# prime program using try and except

def prim(min, max):
    ls_num = []
    if min > 0 and max > 0:
        try:
            for num in range(min, max + 1):
                if num > 1:
                    for j in range(2, num):
                        if num % j == 0:
                            break
                    else:
                        ls_num.append(num)
            return ls_num
        except(TypeError):
            err = 'the value must be positive'
            return err
    else:
        return 'value is suppose to be positive, no negative value allowed'

