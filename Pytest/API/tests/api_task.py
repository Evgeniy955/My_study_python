import requests

# URL = 'https://earthquake.usgs.gov/fdsnws/event/1/'
URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

parameters = {
    'format': 'geojson',
    'starttime': '2019-01-01',
    'endtime': '2019-05-01',
    'latitude': '51.51',
    'longitude': '-0.12',
    'maxradiuskm': '2000',
    'minmagnitude': '2'
}

response = requests.get(URL, headers={'Accept': 'application/json'}, params=parameters)

data = response.json()

number = 1

for country in data['features']:
    print(f"{number}. Place: {country['properties']['place']}. Magntude: "
          f"{country['properties']['mag']}.")
    number += 1
