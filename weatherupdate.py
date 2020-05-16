import requests
import json
import os
from dotenv import load_dotenv

major_cities = ["Tokyo", "Delhi", "New York", "London", "Chicago", "Hong Kong", "San Francisco", "Toronto", "Miami", "Boston", "Dubai", "Melbourne", "Houston", "Los Angeles", "Beijing", "Moscow", "Paris", "Phoenix", "Berlin", "Rome"]
weather_api_key = os.getenv("weather_API")

def getWeatherData(location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(location, weather_api_key)
    return requests.get(url).json()

def closestFarthestCities(location):
    cities_weather = []
    for city in major_cities:
        weather_data = getWeatherData(city)

        weather_data = (city, weather_data["main"]["temp"], weather_data["weather"][0]["description"])
        cities_weather.append(weather_data)
        
    location_temp = getWeatherData(location)["main"]["temp"]

    closestTemp = abs(cities_weather[0][1] - location_temp)
    farthestTemp = abs(cities_weather[0][1] - location_temp)

    closestCity = cities_weather[0]
    farthestCity = cities_weather[0]

    for group in cities_weather:
        difference = abs(location_temp - group[1])

        if(difference > farthestTemp):
            farthestTemp = difference
            farthestCity = group
        
        elif(difference < closestTemp):
            closestTemp = difference
            closestCity = group


    return (closestCity, farthestCity)
