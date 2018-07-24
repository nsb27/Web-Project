import requests

def getWeather_city(city):
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": city, "units":"metric", "appid":"fe484c99838f8811a2ed7f7d0e72b97b"}
	response = requests.get(endpoint, params=payload)
	data = response.json()
	temperature = data["main"]["temp"]
	name = data["name"]
	weather = data["weather"][0]["main"]

	print u"It's {}C in {}, and the sky is{}".format(temperature, name, weather)

getWeather_city("Brighton,UK")





