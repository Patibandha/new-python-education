import Diamond


def test_diamond():
    response = Diamond.diam(4)
    assert response == "   * \n  * * \n * * * \n* * * * \n * * * \n  * * \n   * \n"
