import requests

city = input('City? ')

api_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {'q': city, 'appid': 'api_key', 'units': 'metric'}

res = requests.get(api_url, params=params)
# print(res.status_code)
data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))
