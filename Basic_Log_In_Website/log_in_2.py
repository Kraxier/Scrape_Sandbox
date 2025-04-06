# r = requests.post(url, data={key: value}, json={key: value}, headers={key: value})
'''
url is the endpoint you're sending the request to (required)
data is for sending form-encoded data (optional)
json is for sending JSON data (optional)
headers allows you to send HTTP headers (optional)
'''

# This imports the requests library, which is a popular HTTP library for making web requests in Python.
# import requests

# params = {'username': 'Kraxier', 'password': '12345'}
# Dictionary  in Python used for login credential 

# r = requests.post("https://quotes.toscrape.com/", data=params)
# Sends a POST request to the main page (not the login page) with the credentials
# data=params sends the username/password as form data

'''
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
'''
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# import requests
# login_url = "https://quotes.toscrape.com/login"
# target_url = "https://quotes.toscrape.com/"
# credentials = {'username': 'Kraxier', 'password': '12345'}
# response = requests.post(login_url, data=credentials)
# print(response)
# print()
# protected_content = requests.get(target_url)
# print(protected_content.text)

'''
import requests

params = {'firstname': 'Kraxier', 'lastname': 'Luthor'}
r = requests.post("https://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)
'''



















# Trying to get the Cookies 
import requests
session = requests.Session()

login_url = "https://quotes.toscrape.com/login"
login_data = {"username": "kraxier", "password": "12345"}
response = session.post(login_url, data=login_data)
print(session.cookies) 


'''
Results are:
1. <RequestsCookieJar[<Cookie session=eyJ1c2VybmFtZSI6ImtyYXhpZXIifQ.Z-xIdA.VTo8NMQps953UkmhIAWCCnMmGs8 for quotes.toscrape.com/>]>
2. <RequestsCookieJar[<Cookie session=eyJ1c2VybmFtZSI6ImtyYXhpZXIifQ.Z-xIlQ.CHRMsXu280REQPUzK6zP-8DJqFA for quotes.toscrape.com/>]>
'''
