import requests

def send_simple_message(message):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox29d827ea4bdf4b47b52a46cb883243f0.mailgun.org/messages",
		auth=("api", "a2ab13398dbad0ae1efc6e805a6a9420-8889127d-c656532e"),
		data={"from": "excited user <mailgun@sandbox29d827ea4bdf4b47b52a46cb883243f0.mailgun.org>",
        		"to": ["natalie.brooks@thetrainline.com", "natalie.brooks@thetrainline.com"], 
        		"subject": "Hello, from code frist girls",
        		"text": message})


response = send_simple_message("my first")
print response

print send_simple_message("my second")