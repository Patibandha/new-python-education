# Difference between regular open and with open in file management?
''' The main difference between with open and only open is that if we are using with open statement in program then
we do not need to close our file. Whereas if we are using open statement, then we need to close our file after
using it through <filename>.close(). And after closing the file you can not open it till you again give a command
to open and read it.'''

def fileoperation(path, str):

    try:
        with open(path, 'a+') as file:
            file.append(str)

    except:
        return "There is no file..."


def fileoper(path, str):
    try:
        file1 = open(path, 'r+')
        y = file1.read()
        print(y)
        file1.close()
        return y

    except:
        return "There is no file..."

