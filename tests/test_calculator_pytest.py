import pytest
from unit_testing import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_no_operator():
    with pytest.raises(ValueError) as e:
        calculator('sdfdfds')
    assert 'Expression must contain atleast one of those +-/*' == e.value.args [0]


def test_two_operator():
    with pytest.raises(ValueError) as e:
        calculator('2+2+2')
    assert 'Expression must contain two integers and one operator' == e.value.args [0]


b = lambda a, list: [x for x in list if x > a]

if __name__ == '__main__':
    pytest.main()
