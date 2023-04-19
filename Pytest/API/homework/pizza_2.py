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
    res = requests.post(f'{url}', headers=headers, data=data).json()
    return res['form'],res['headers']


if __name__ == '__main__':
    print(send_post(URL, headers, data))

