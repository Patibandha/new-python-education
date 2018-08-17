import Even
def test_even():
    response = Even.even(0, 10000)
    assert response[0] == 0
    assert response[0] != 2

    response2 = Even.even(-2, 10000)
    assert response2 == 'The value should be positive.'