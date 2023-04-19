import pytest
import requests

URL = "http://api.mathjs.org/v4/"

headers = {'User-Agent': 'Python Learning Requests'}


@pytest.mark.post_request
@pytest.mark.parametrize("expression", [(
        "5.3*96",
        "b = 180-65.68412",
        "c = 2.126+95.321354656",
        "d = 122/11",
        "875.654/0"
)])
def test_math_method3(rounding_result, expression):
    value = {'expr': expression, 'precision': rounding_result}
    math_data = [
        '%.{}g'.format(rounding_result) % (5.3 * 96),
        '%.{}g'.format(rounding_result) % (180 - 65.68412),
        '%.{}g'.format(rounding_result) % (2.126 + 95.321354656),
        '%.{}g'.format(rounding_result) % (122 / 11),
        "Infinity"
    ]

    resp = requests.post(URL, headers=headers, json=value)
    result = resp.json()

    assert result["result"] == math_data, "Test failed. Expected result entered incorrectly"
    assert result["error"] == None, "Test failed. The result must be 'None'"
