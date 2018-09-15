from calc import Calculate, Sci


def test_calc():

    calc1 = Calculate(2, '+', 3)
    resp1 = calc1.simple_clac()
    assert resp1 == 5

    calc2 = Sci(25, 'sqrt')
    resp2 = calc2.sci_calc()
    assert resp2 == 5.0

    calc3 = Sci(25, 'sq')
    resp3 = calc3.sci_calc()
    assert resp3 == 625.0

    calc4 = Sci(20, 'sq')
    resp4 = calc4.sci_calc()
    assert resp4 != 625.0

