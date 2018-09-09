import count_num_alphabet

def test_count():
    response = count_num_alphabet.count('ABCD123456')
    assert response == [6, 4]

    response1 = count_num_alphabet.count('AB123456')
    assert response1 != [6, 4]
