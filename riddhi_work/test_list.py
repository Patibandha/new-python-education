import list_push_append

def test_list():
    response = list_push_append.list()
    assert response == [1, 2, 3, 4, 5, 6]

    response1 =list_push_append.list()
    assert  response1 != [1, 2, 3, 4, 5, 7]

    response2 = list_push_append.list1()
    assert response2 == [1, 2, 6 ,3, 4, 5]

    response3 = list_push_append.list1()
    assert response3 != [1, 2, 6, 3, 4]