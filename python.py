from flask import Flask , render_template,request
from datetime import datetime
from horoscopeapi import get_horoscope, zodiac_sign

#This is create instance of Flask. app is variable
app = Flask("MyApp")


#Default route his method will be called when you hit http://127.0.0.0:5000/
@app.route("/")
def home():
	return render_template ("home.html") # render_template method is a special function flask which redirect to the html file mentioned in the paramter

#This method will be called when you hit http://127.0.0.0:5000/writeanythinghere
#This is an example when you want to hit a URL with Paramaters. This is called GET request.
@app.route("/<message>")
def hello_Name(message):
	return render_template ("printmessage.html",message=message.title()) # This example take additional paramter which can be passed to the html


#This method is internal method. This can only be called in this python code.
#This menthod is being call from below 
def calculate_generation(year_parameter):
	result = ''

	if year_parameter < 1996:
		result = 'Classic'
	if year_parameter in range(1966,2000):
		result = 'Have a great weekend'
	elif year_parameter in range(2001,2018):
		result = 'Try again in a few years'
   	
   	else:
   		result = 'IoT'
   	return result
