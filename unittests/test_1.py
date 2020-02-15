import pytest


def div(a, b):
    return a / b

@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expection",{
    (10,2,5),
    (10,3,3.33333),
    (-10,-2,5),
    (-10,5,-2),
    (100000000,1,100000000),
    (2,20000,0.0001),
    (0,200,0),
    (100,0,0),
    (66.72,11.12,6)
}

)
def test_div(number1,number2,expection):
    assert div(number1, number2) == expection
