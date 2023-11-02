import requests


# 1
def tell_joke():
    joke = requests.get("https://api.chucknorris.io/jokes/random").json()
    print(joke['value'])


# 2

def get_weather():
    municipality = input("Give municipality: ")
    apikey = ''
    geo_data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={municipality}&appid={apikey}').json()
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]
    res = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude="currently"&units={"metric"}&appid={apikey}').json()
    print(res['current']['weather'][0]['description'])
    print(res['current']['temp'], 'Celcius')

