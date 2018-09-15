import USDtoINR


def test_currency():
   result = USDtoINR.currency(20)
   assert result == 1370.0

   result1 = USDtoINR.currency(-20)
   assert result1 == 'The value should be positive.'

   result2 = USDtoINR.currency('abcd')
   assert result2 == 'It should be a positive value, not a string.'

