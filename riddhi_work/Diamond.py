# Print Diamond pattern


def diam(rows):
    result = ""
    for i in range(0, rows):
        result = '\n' + result
        result = ' ' * (rows - i - 1) + '* ' * (i + 1) + result

    for j in range(rows-1, 0, -1):
        result = '\n' + result
        result = ' ' * (rows-j) + '* ' * (j) + result

    return result


diam(4)


