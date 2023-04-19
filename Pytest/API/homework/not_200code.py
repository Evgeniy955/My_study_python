import requests

URL = 'https://nghttp2.org/httpbin'

headers = {'User-Agent': 'Python Learning Requests'}

d1 = dict()


def send_get(base_url, url, headers=None):
    return requests.get(f'{base_url}{url}', headers=headers)


r = send_get(URL, "/spec.json", headers).json()

urls = [i for i in list(r['paths'])]

for uri in urls:
    res = send_get(URL, uri, headers)
    status = res.status_code
    if status != 200:
        d1[uri] = status

# print(dict(zip(url_result, code_result)))
if __name__ == '__main__':
    print(urls)
    # print(d1)
