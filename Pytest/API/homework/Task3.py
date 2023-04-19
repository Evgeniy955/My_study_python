import requests

URL = 'https://restcountries.com/v3.1/all'

headers = {'User-Agent': 'Python Learning Requests'}

code_language = dict()


def send_get(url, headers=None):
    return requests.get(url, headers=headers)


res = send_get(URL, headers).json()
#
# for i in res:
#     if "languages" in i:
#         print(i["languages"])

[code_language.update(i["languages"]) for i in res if "languages" in i]

if __name__ == '__main__':
    print(list(code_language))
