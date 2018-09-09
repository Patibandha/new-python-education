# Test case for open and open with file.

import open_openwith


def test_with():
    result = 'Hello!!! This is a Python world...'
    path = '/home/riddhi/Desktop/Riddhi_Python/Python/new.txt'
    open_openwith.fileoperation(path, result)
    with open(path, 'r') as file:
        x = file.read()
        assert result in x


