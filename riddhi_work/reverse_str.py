# wap to take string from the user and print it back in reverse order.


def reverse(s):
    try:

        # if entry.isalpha():
        if type(s) == str:
            entry = ""
            for i in s:
                entry = i + entry
                # return entry
            return entry

        elif type(s) == int or type(s) == float:
            # return 'It should not be any value...'
            return 'It should not be an integer or float value'

        elif type(s) == list or type(s) == tuple or type(s) == dict:
            # return 'It should not be any value...'
            return 'It should not be a list or tuple or dictionary...'

    except:
        return 'It should be a string...'


# s = input("Enter the string: ")
#
# print ("The original string  is : " + s)
#
#
# print ("The reversed string is : " + reverse(s))


