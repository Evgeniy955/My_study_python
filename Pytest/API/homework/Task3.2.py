import requests

URL = 'https://restcountries.com/v3.1'

headers = {'User-Agent': 'Python Learning Requests'}

LANG_LIST = "languages"

num_population = dict()


def send_get(base_url, path_url, headers=None):
    return requests.get(f'{base_url}{path_url}', headers=headers)


def code_lang_list(lang_countries):
    result = dict()
    res = send_get(URL, "/all", headers).json()
    [result.update(i[f'{lang_countries}']) for i in res if f'{lang_countries}' in i]
    return result


def population_lang(code_language):
    sum = 0
    for code in code_language:
        url_lang = f'/lang/{code}'
        res_lang = send_get(URL, url_lang, headers).json()
        for country in res_lang:
            if 'population' in country:
                sum += country['population']
        num_population[code] = sum
        sum = 0
    return num_population


if __name__ == '__main__':
    list_lang = code_lang_list(LANG_LIST)
    print(population_lang(list_lang))
