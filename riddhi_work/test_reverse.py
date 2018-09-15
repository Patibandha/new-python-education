import reverse_str

def test_reverse():
    result = reverse_str.reverse('Riddhi')
    assert result == 'ihddiR'

    result1 = reverse_str.reverse('Rid123')
    # import pdb
    # pdb.set_trace()
    assert result1 != 'ihddiR'

    result2 = reverse_str.reverse(123)
    assert result2 == 'It should not be an integer or float value'

    result3 = reverse_str.reverse([1, 2, 3])
    assert result3 == 'It should not be a list or tuple or dictionary...'

