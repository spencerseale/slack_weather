#!/usr/bin/env python3

import requests

website = "https://api.weather.gov/points/44.1333,-123.2144"

data = requests.get(website)

#print(data)

weather_data = data.json()

#print(weather_data)

eugene_weather = (requests.get(weather_data['properties']['forecast'])).json()

#print(eugene_weather)

temp = (eugene_weather['properties']['periods'][0]['temperature'])
unit = (eugene_weather['properties']['periods'][0]['temperatureUnit'][0])

print(temp)

print(f"The current temperature is {temp}{unit}.")
