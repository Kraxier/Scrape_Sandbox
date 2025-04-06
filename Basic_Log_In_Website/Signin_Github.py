# import requests
# params = {'add_account': 'MaskKr','login':'q28akE@fR9wNZn2'}
# r = requests.post("https://github.com/session", data=params)
# print(r.text)

import requests
from bs4 import BeautifulSoup

# Start a session to maintain cookies
session = requests.Session()

# Get GitHub login page
login_url = "https://github.com/login"
response = session.get(login_url)

# Parse the authenticity token
soup = BeautifulSoup(response.text, "html.parser")
auth_token = soup.find("input", {"name": "authenticity_token"})["value"]

# Define the login data with the extracted token
login_data = {
    "login": "MaskKr",
    "password": "q28akE@fR9wNZn2",
    "commit": "Sign in",
    "authenticity_token": auth_token
}

# Perform the login request
post_url = "https://github.com/session"
login_response = session.post(post_url, data=login_data)

# Check if login was successful
if "Incorrect username or password" in login_response.text:
    print("Login failed. Check your credentials.")
else:
    print("Login successful!")

# How the Code Works 
# What Should Approach that i make ? 


'''
PS C:\Users\klabi\OneDrive\Desktop\Advance_Phase> git init
Reinitialized existing Git repository in C:/Users/klabi/OneDrive/Desktop/Advance_Phase/.git/
PS C:\Users\klabi\OneDrive\Desktop\Advance_Phase> git add .
PS C:\Users\klabi\OneDrive\Desktop\Advance_Phase> git commit -m "Trying to Log in Github Chatgpt help me "
[main aa43a4f] Trying to Log in Github Chatgpt help me
 1 file changed, 39 insertions(+)
 create mode 100644 Signin_Github.py
PS C:\Users\klabi\OneDrive\Desktop\Advance_Phase> git push origin main
Enumerating objects: 4, done.
'''