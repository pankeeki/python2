import json
import requests

apiKey: str = input("add api key: ")
city: str = input("Select city: ")

try:
    request: str = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={apiKey}"
    respons = requests.get(request)
    if respons.status_code == 200:
        city = respons.json()[0]['name']
        request = f"https://api.openweathermap.org/data/2.5/weather?lat={respons.json()[1]['lat']}&lon={respons.json()[1]['lon']}&units=metric&appid=e17e88ee38906634fb17b2734beb65c6"
        respons = requests.get(request)
        if respons.status_code == 200:
            weatherRespons = respons.json()
            print(
                f"current weather in {city}: {weatherRespons['weather'][0]['description']}. Temperature is: {weatherRespons['main']['temp']} celcisus")
except requests.exceptions.RequestException as e:
    print("failed to load data.")
