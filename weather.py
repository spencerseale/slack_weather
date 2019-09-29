
import os
import time
import re
import slack
import api_keys


# get app token 
token = api_keys.SLACK_TOKEN

#importing requests to use API
import requests

#API with Eugene, OR geographic coordinates
website = "https://api.weather.gov/points/44.1333,-123.2144"

#Forcing json format
weather_data = requests.get(website).json()

#Moving to current forecast API from the initial coordinate API
eugene_weather = requests.get(weather_data['properties']['forecast']).json()

#These are less detailed weather descriptors
# temp = (eugene_weather['properties']['periods'][0]['temperature'])
# unit = (eugene_weather['properties']['periods'][0]['temperatureUnit'][0])
# time_of_day = eugene_weather['properties']['periods'][0]['name']

#This gives a nice detailed summation
detailed_forecast = eugene_weather['properties']['periods'][0]['detailedForecast']


# access slack web client
client = slack.WebClient(token=token)

# post message in the test channel
# channel ids are indicated by string in URL 

while True:
    if int(time.time()) == 1569790740:
        client.chat_postMessage(
      channel="GNNRVLMLZ",
      text= '\n :cloud: :cloud: :cloud: Good morning! Here\'s todays weather for Eugene... :cloud: :cloud: :cloud:\n'+ '```'  +         detailed_forecast + '```'
    )
    break
