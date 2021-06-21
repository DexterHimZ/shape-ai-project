import requests
import sys
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('readme.txt', 'w') as f:

    f.writelines("-------------------------------------------------------------"+"\n")
    f.writelines("Weather Stats for - {}  || {}".format(location.upper(), date_time)+"\n")
    f.writelines("-------------------------------------------------------------"+"\n")
    f.writelines("Current temperature is: {:.2f} deg C".format(temp_city)+"\n")
    f.writelines("Current weather desc  :"+weather_desc+"\n")
    f.writelines("Current Humidity      :"+str(hmdt)+ '%'+"\n")
    f.writelines("Current wind speed    :"+str(wind_spd) +'kmph'+"\n")
    f.close()
    print(open('readme.txt').read())
