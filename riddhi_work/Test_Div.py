# Test case for Numbers Divisible by 13 and 17.

import Divisible_13_17
def test_div():
    response = Divisible_13_17.div(100, 50000)
    assert response[0] == 221
    assert response[2] != 221

    response2 = Divisible_13_17.div(-20, 200)
    assert response2 == 'The value should be positive.'



