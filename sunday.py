from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def getWeather_city():
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": "london,UK", "units":"metric", "appid":"fe484c99838f8811a2ed7f7d0e72b97b"}
	response = requests.get(endpoint, params=payload)
	data = response.json()

	temperature = data["main"]["temp"]
	name = data["name"]
	weather = data["weather"][0]["description"]
	clouds = data ["clouds"]["all"]

	print u"It's {}C in {}, and the sky is {}{}".format(temperature, name, weather, clouds)
	print data 
	return render_template("sunday.html", temperature=temperature, name=name, weather= weather, clouds=clouds)

app.run(debug=True)
