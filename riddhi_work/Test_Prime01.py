
import Prime_01
def test_prime():
    response = Prime_01.prime(0, 500)
    assert response[0] == 2
    assert response[5] != 2

    response2 = Prime_01.prime(-1, 500)
    assert response2 == 'The value should be positive.'