# w.a.p. to convert celsius to fehrenheit vice versa user will enter value and give instruction to convert F to C or C to F.


def conv_celsuis(temp):
    cel = (temp - 32) / 9.0 * 5.0
    C = round(cel,2)
    return C


def conv_Fahrenheit(temp):
    fahr = 9.0 / 5.0 * temp + 32
    F = round(fahr, 2)
    return F


conv_celsuis(20)
conv_Fahrenheit(-6.66)

