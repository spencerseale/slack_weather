#!/usr/bin/env python3

#importing requests to use API
import requests

#API with Eugene, OR geographic coordinates
website = "https://api.weather.gov/points/44.1333,-123.2144"

#Forcing json format
weather_data = (requests.get(website)).json()

#Moving to current forecast API from the initial coordinate API
eugene_weather = (requests.get(weather_data['properties']['forecast'])).json()

#These are less detailed weather descriptors
# temp = (eugene_weather['properties']['periods'][0]['temperature'])
# unit = (eugene_weather['properties']['periods'][0]['temperatureUnit'][0])
# time_of_day = eugene_weather['properties']['periods'][0]['name']

#This gives a nice detailed summation
detailed_forecast = eugene_weather['properties']['periods'][0]['detailedForecast']

#std out giving forecast
print(f"The current forecast for Eugene, OR is: {detailed_forecast}")
