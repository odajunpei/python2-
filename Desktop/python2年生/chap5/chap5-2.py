import requests
import json

#現在の天気を取得する：神戸
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe.JP", key="81f8dc82d6ebc486fdf133a97554ed55")

jsondata = requests.get(url).json()
print(jsondata)
