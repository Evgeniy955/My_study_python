import pytest
from math_module import math_positive_test, math_negative_test, test_list_positive


@pytest.mark.post_request
@pytest.mark.parametrize("expression", [(
        "5.3*96",
        "b = 180-65.68412",
        "c = 2.126+95.321354656",
        "d = 122/11",
        "875.654/0"
)])
def test_data_list(rounding_result, expression):
    test_list_positive(rounding_result, expression)


@pytest.mark.post_request
@pytest.mark.parametrize("expression, expected", [
    ("5.3+123.444", 5.3 + 123.444),
    ("a = 18.06+65.87", 18.06 + 65.811),
])
def test_math_addition(rounding_result, expression, expected):
    math_positive_test(rounding_result, expression, expected)


@pytest.mark.post_request
@pytest.mark.parametrize("expression, expected", [
    ("8.654-723.444", 8.654 - 723.444),
    ("a = 65484.321-654215.870546", 65484.321 - 654215.870546),
])
def test_math_subtraction(rounding_result, expression, expected):
    math_positive_test(rounding_result, expression, expected)


@pytest.mark.post_request
@pytest.mark.parametrize("expression, expected", [
    ("8.654*723.444", 8.654 * 723.444),
    ("a = 65484.321*654215.870546", 65484.321 * 654215.870546),
])
def test_math_multiplication(rounding_result, expression, expected):
    math_positive_test(rounding_result, expression, expected)


@pytest.mark.post_request
@pytest.mark.parametrize("expression, expected", [
    ("875.654/3.444", 875.654 / 3.444),
    ("a = 652484.321/6542.870546", 652484.321 / 6542.870546),
])
def test_math_division(rounding_result, expression, expected):
    math_positive_test(rounding_result, expression, expected)


@pytest.mark.post_request
@pytest.mark.parametrize("expression, expected", [
    ("875.654/12a.&", "Error: Property name expected after dot (char 13)"),
    ("652484.321/5*", "Error: Unexpected end of expression (char 14)")
])
def test_negative_data(rounding_result, expression, expected):
    math_negative_test(rounding_result, expression, expected)
