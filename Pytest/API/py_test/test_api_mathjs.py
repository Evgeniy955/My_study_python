import pytest
import requests
import math

URL = "http://api.mathjs.org/v4/"

headers = {'User-Agent': 'Python Learning Requests'}


@pytest.mark.get_request
@pytest.mark.parametrize("expression, expected", [('sqrt(56)', math.sqrt(56)), ('sqrt(11111111)', math.sqrt(11111111))])
def test_sqrt_positive(rounding_result, expression, expected):
    math_expression = {'expr': expression, 'precision': rounding_result}
    resp = requests.get(URL, headers=headers, params=math_expression)
    assert resp.status_code == 200, "Test failed. Status code should be 200"

    value = resp.json()
    print(value)
    expected_format = '%.{}g'.format(rounding_result) % expected
    assert float(value) == float(expected_format), "Test failed. Expression entered incorrectly"


@pytest.mark.get_request
@pytest.mark.parametrize("expression", [('sqrt(5,)'), ('sqrt(*/)')])
def test_sqrt_negative(rounding_result, expression):
    math_expression = {'expr': expression}
    resp = requests.get(URL, headers=headers, params=math_expression)
    assert resp.status_code == 400, "Test failed. Status code should be 400"
