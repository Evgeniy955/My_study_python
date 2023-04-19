import requests

URL = 'http://httpbin.org/post'

headers = {'User-Agent': 'Python Learning Requests'}

data = {
    "comments": "Hello world",
    "custemail": "test@mail.com",
    "custname": "Yevhen",
    "custtel": "123456",
    "delivery": "14:15",
    "size": "medium",
    "topping": [
        "bacon",
        "cheese"
    ]
}


def send_post(url, headers=None, data=None):
    return requests.post(url, headers=headers, data=data)


def resp():
    res = send_post(URL, headers, data).json()
    path_json = res['form']
    hed = res['headers']
    return tuple((path_json, hed))


if __name__ == '__main__':
    print(resp())
