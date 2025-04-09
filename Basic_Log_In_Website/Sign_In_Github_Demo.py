# Demo Purpose If you have a Real Log in Data you should put it 

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
from bs4 import BeautifulSoup

# Start a sessions to Maintain Cookies
session = requests.Session()
login_url = "https://github.com/login"
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")

# Testing it Only 
header = soup.select_one("h1")
print(header)


# auth_token = soup.find("input", {"name": "authenticity_token"})["value"]
auth_token = soup.select_one('input[name="authenticity_token"]')['value']
print(auth_token)

# Using the Value of auth_token to have parameters 
# Define the login data with the extracted token
login_data_fake = {
    "login": "username",
    "password": "password",
    "commit": "Sign in",
    "authenticity_token": auth_token
}

'''
From my Question in Chatgpt he said that "commit": "Sign in"is not required but it is necessary 
When you click a "Sign in" button, it may submit a name="commit" and value="Sign in" to the backend.
The server might rely on it to validate that the form was submitted properly.

It's simulating the exact behavior of clicking the "Sign in" button.
Without it, the server might reject the request or behave unexpectedly.
'''

# Perform the login request
post_url = "https://github.com/session"
# Because in the form there are <form action="/session" method="post">
login_response = session.post(post_url, data=login_data_fake)
print(login_response)
print(login_response.url)

# response_login_state = session.get(login_response) Wrong it should be a url a string not a <Response [200]>
response_login_state = session.get(login_response.url)

soup_login_state = BeautifulSoup(response_login_state.text, "html.parser")

header = soup_login_state.select_one("h2")
print(header)

