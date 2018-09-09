import Temp_Conv


def test_temp():
    response = Temp_Conv.conv_celsuis(20)
    assert response == (-6.67)

    response1 = Temp_Conv.conv_celsuis(25)
    assert response1 != (-6.6666666)

    response2 = Temp_Conv.conv_Fahrenheit(-6.66)
    assert response2 == 20.01

    response3 = Temp_Conv.conv_Fahrenheit(6.66)
    assert response3 != 20.012