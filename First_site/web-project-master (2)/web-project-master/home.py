
from flask import Flask, render_template, request

from datetime import datetime 

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
		weekend = 'Try again when you are 18 or grab a mocktail!' 
		page = "dontshowmyweekend.html"
	else:
		weekend = 'Have a great weekend! Here are our tips' 
		page = "showmyweekend.html"

	return render_template(
		page,
		data=weekend) 

# def calculate_age(user_date):
# 	weekend = 'N/A'
# 	today = datetime.today()
# 	minus18 = today.replace(year=today.year-18)
# 	if user_date <= minus18:
# 		weekend = 'Have a great weekend! Here are our tips' 
# 	return render_template(
# 		"showmyweekend.html",
# 		data=weekend)

# def calculate_age(user_year, user_month, user_day):
# 	weekend = 'N/A'
# 	if user_year >=2000 and user_month >=6 and user_day >=25:
# 		weekend = 'Try again when you are 18 or grab a mocktail!' 
# 	else:
# 		weekend = 'Have a great weekend!' 

# 	return render_template(
# 		"showmyweekend.html",
# 		data=weekend)

@app.route("/showmyweekend", methods=["POST"])
def get_weekend():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	dateOfBirth =  form_data["dob"] # from the form object getting value of dob field.
	date = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
	# day = date.day
	# month = date.month
	# year = date.year
	
	return calculate_age(datetime(date.year, date.month, date.day)) 

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