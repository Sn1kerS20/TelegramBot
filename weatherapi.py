import requests
import config

def get_weather(city: str):
    url = "http://api.weatherapi.com/v1/current.json" 
    params = {
        "key": config.API_TOKEN,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(url, params)

    return response.json()