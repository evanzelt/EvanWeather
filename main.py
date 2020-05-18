import os
from dotenv import load_dotenv
from Tweeper import tweeper
from weatherupdate import getWeatherData, closestFarthestCities
from time import time
from datetime import date


def main():
    API_key = os.getenv("API_key")
    API_secret = os.getenv("API_secret_key")
    token = os.getenv("token")
    token_secret = os.getenv("token_secret")

    my_account = tweeper(API_key, API_secret, token, token_secret)

    last_time = time()
    delay = 60*60*24
    main_city=  "Pittsburgh"

    updateWeather(main_city, my_account)

    while(1):
        if(time() - last_time > delay):
            updateWeather(main_city, my_account)
            last_time = time()


def updateWeather(city, account):
    weather_data = getWeatherData(city)
    cities = closestFarthestCities(city)
    tweet = "{} has {} with a temperature of {}°F today.\nComparable - {} with {} and a temperature of {}°F.\nDissimilar - {} with {} and a temperature of {}°F".format(city, weather_data["weather"][0]["description"], weather_data["main"]["temp"], cities[0][0], cities[0][2], cities[0][1], cities[1][0], cities[1][2], cities[1][1])
    print(tweet)
    account.sendTweet(tweet)


if(__name__ == '__main__'):
    main()
