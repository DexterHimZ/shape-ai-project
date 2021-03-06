import requests
import sys
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'                                              #created api_key using open weathermap.org
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)                                          #variables to store and display data
weather_desc = api_data['weather'][0]['description']
cnt  = api_data['sys']['country']
hmdt = api_data['main']['humidity']
prs = api_data['main']['pressure']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('output.txt', 'w') as f:

    f.writelines("\n"+"----------------CODE BY HIMANGSHU SHEKHAR------------------"+"\n")       #writing the data to a text file
    f.writelines("Weather Stats for - {}  || {}".format(location.upper(), date_time)+"\n")
    f.writelines(("Country   :  "+cnt)+"\n")
    f.writelines("-------------------------------------------------------------"+"\n")
    f.writelines("Current temperature is: {:.2f} deg C".format(temp_city)+"\n")
    f.writelines("Current weather desc  : "+weather_desc+"\n")
    f.writelines("Current Humidity      : "+str(hmdt)+ ' %'+"\n")
    f.writelines("Current Pressure      : "+str(prs)+ " hPa"+"\n")
    f.writelines("Current wind speed    : "+str(wind_spd) +' m/s'+"\n")
    f.close()
    print(open('output.txt').read())
