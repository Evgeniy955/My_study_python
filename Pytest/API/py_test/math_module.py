import requests

URL = "http://api.mathjs.org/v4/"

headers = {'User-Agent': 'Python Learning Requests'}


def math_positive_test(rounding_result, expression, expected):
    value = {'expr': expression, 'precision': rounding_result}
    resp = requests.post(URL, headers=headers, json=value)
    result = resp.json()
    expected_format = '%.{}g'.format(rounding_result) % expected

    assert float(result["result"]) == float(expected_format), "Test failed. Expected result entered incorrectly"
    assert result["error"] == None, "Test failed. The result must be 'None'"


def math_negative_test(rounding_result, expression, expected):
    value = {'expr': expression, 'precision': rounding_result}
    resp = requests.post(URL, headers=headers, json=value)
    result = resp.json()

    assert result["result"] == None, "Test failed. Expression entered incorrectly"
    assert result["error"] == expected


def test_list_positive(rounding_result, expression):
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
