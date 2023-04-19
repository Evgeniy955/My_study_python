import requests


class APICall:

    @classmethod
    def send_get(cls, url, headers=None):

        return requests.get(f'{url}', headers=headers).json()


    def send_post(self, url, headers=None, data=None):
        self.url = url
        self.headers = headers
        self.data = data
        post_res = requests.post(f'{url}', headers=headers, data=data).json()
        return post_res['form'], post_res['headers']

    def send_delete(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers
        self.params = params
        delete_res = requests.delete(f'{url}', headers=headers, params=params).json()
        return delete_res

    def send_put(self, url, headers=None, data=None):
        self.url = url
        self.headers = headers
        self.params = data
        put_res = requests.put(f'{url}', headers=headers, data=data).json()
        return put_res

    def send_head(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers
        self.params = params
        head_res = requests.head(f'{url}', headers=headers, params=params)
        return head_res.headers

    def send_patch(self, url, headers=None, data=None):
        self.url = url
        self.headers = headers
        self.params = data
        patch_res = requests.patch(f'{url}', headers=headers, data=data).json()
        return patch_res



# print(a.send_get('https://restcountries.com/v3.1/all'))
# print(a.send_post('http://httpbin.org/post', headers = {
#     'User-Agent': 'Python Learning Requests'
#     },
#     data = {
#     "comments": "Hello world",
#     "custemail": "test@mail.com",
#     "custname": "Yevhen",
#     "custtel": "123456",
#     "delivery": "14:15",
#     "size": "medium",
#     "topping": [
#         "bacon","cheese"
#     ]
#     }))
# print(a.send_delete('https://httpbin.org/delete'))
# print(a.send_put('https://httpbin.org/put', data={'key': 'value'}))
# print(a.send_head('https://httpbin.org/get'))
# print(a.send_patch('https://nghttp2.org/httpbin/delay/200'))
