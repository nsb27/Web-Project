
from flask import Flask, render_template, request

from datetime import datetime 
import requests

app = Flask("HomeApp")

@app.route("/")
def home_default():
	return render_template('Home.html')

@app.route("/dob", methods=["POST"])
def get_dob():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	dateOfBirth =  form_data["dob"] # from the form object getting value of dob field.
	date = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
	month = date.month
	year = date.year
	
	return dob 

def calculate_age(user_date):
	weekend = 'N/A'
	today = datetime.today()
	minus18 = today.replace(year=today.year-18)
	if user_date >= minus18:
		return render_template("under_18.html")

	else:
		return render_template("over_18.html")

# def calculate_age(user_year, user_month, user_day):
# 	weekend = 'N/A'
# 	if user_year >=2000 and user_month >=6 and user_day >=25:
# 		weekend = 'Try again when you are 18 or grab a mocktail!' 
# 	else:
# 		weekend = 'Have a great weekend!' 

# 	return render_template(
# 		"showmyweekend.html",
# 		data=weekend)

@app.route("/age", methods=["POST"])
def get_weekend():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	dateOfBirth =  form_data["dob"] # from the form object getting value of dob field.
	date = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
	# day = date.day
	# month = date.month
	# year = date.year
	
	return calculate_age(datetime(date.year, date.month, date.day)) 

@app.route("/friday")
def friday():
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": "london,UK", "units":"metric", "appid":"fe484c99838f8811a2ed7f7d0e72b97b"}
	response = requests.get(endpoint, params=payload)
	data = response.json()

	temperature = data["main"]["temp"]
	name = data["name"]
	weather = data["weather"][0]["description"]
	humidity = data ["main"] ["humidity"]

	print u"It's {}C in {}, and the sky is {}{}".format(temperature, name, weather, humidity)
	print data 
	return render_template("Friday.html", temperature=temperature, name=name, weather= weather, humidity=humidity)

@app.route("/saturday")
def saturday():
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": "london,UK", "units":"metric", "appid":"fe484c99838f8811a2ed7f7d0e72b97b"}
	response = requests.get(endpoint, params=payload)
	data = response.json()

	temperature = data["main"]["temp"]
	name = data["name"]
	weather = data["weather"][0]["description"]
	wind = data ["wind"]["speed"]

	print u"It's {}C in {}, and the sky is {}{}".format(temperature, name, weather, wind)
	print data 
	return render_template("Saturday.html", temperature=temperature, name=name, weather= weather, wind=wind)

@app.route("/sunday")
def sunday():
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
	return render_template("Sunday.html", temperature=temperature, name=name, weather= weather, clouds=clouds)

# user_dob = get_dob()
# user_year = datetime.strptime(user_dob,'%m/%d/%Y').year
# user_month = datetime.strptime(user_dob,'%m/%d/%Y').month
# user_day = datetime.strptime(user_dob,'%m/%d/%Y').day
# user_gen = calculate_age(user_year)

# print 'Your DOB :' + user_dob
# print 'Your Weekend:' + user_gen

if __name__ == "__main__":
    app.run(debug=True)

# app.run(debug=True)