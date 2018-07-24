import requests

def getWeather_London():
	endpoint = "http:://api.openweathermap.org/data/2.5/weather"
	payload = {"q": "London,UK", "units":"metric", "appid":"&APPID=fe484c99838f8811a2ed7f7d0e72b97b in any queries."}
	response = requests.get(endpoint, params=payload)
	print response.url	
	print response.status_code
	print response.headers["content-type"]

def getWeather_city(city):
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": city, "units":"metric", "appid":"YOUR_APP_ID"}
	response = requests.get(endpoint, params=payload)
	print response.url	
	print response.status_code
	print response.headers["content-type"]


getWeather_London()

getWeather_city("London,UK")
getWeather_city("Brighton,UK")



