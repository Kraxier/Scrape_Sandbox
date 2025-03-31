# https://toscrape.com/
# Scrapping Everything on This Website
'''
Bookstoscrape is Done 

Next is Quote_To_Scrape
    0. Micro Data with Pagination
    1. Log in With CRSF Token
    2. Javascript Generated Content
    3. 
'''

'''Logging in Quote_to_Scrape'''
# import requests
# session = requests.Session()

# # Login_Website: https://quotes.toscrape.com/login
# # Website to Scrape: https://quotes.toscrape.com/
# params = {'username': 'Kristian', 'password': '12345'}
# r = requests.post("https://quotes.toscrape.com/", data=params)
# print(r.text)

# Results are 
'''
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
'''
'''
# Where does it take me"?
# What URL did i get from this? 

'''

'''

quote_to_scrape HTML 
<form action="/login" method="post" accept-charset="utf-8">
        <input type="hidden" name="csrf_token" value="kYTqDtaohFvHQCpzKcjdGgnRPJlsIOEZrfbMiSuyxWAXmLNwUeBV">
        <div class="row">
            <div class="form-group col-xs-3">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username">
            </div>
        </div>
        <div class="row">
            <div class="form-group col-xs-3">
                <label for="username">Password</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
        </div>
        <input type="submit" value="Login" class="btn btn-primary">
        
    </form>
'''
# Trying to get the Cookies 
# import requests
# from bs4 import BeautifulSoup
# session = requests.Session()
# from urllib.request import urlopen
# login_url = "https://quotes.toscrape.com/login"
# login_data = {"username": "kraxier", "password": "12345"}

# response = session.post(login_url, data=login_data)
# print(session.cookies) 
# # Results are: <RequestsCookieJar[<Cookie session=eyJ1c2VybmFtZSI6ImtyYXhpZXIifQ.Z-rgDQ.WBpBCskUYlrfvpfUmvot8J1_b0s for quotes.toscrape.com/>]>
# # i using the parameter of "session.get" to get the quotetoscrape instead of urlopen it 
# response = session.get("https://quotes.toscrape.com/")
# soup = BeautifulSoup(response.text, 'html.parser')

# # Check for logged-in elements
# username_display = soup.find('a', href='/logout')
# if username_display:
#     print(f"Success! Logged in as: {username_display.text.strip()}")
# else:
#     print("Login failed - no logout link found")
'''
Explanation for this 
    1. Log in Was Successful that server sent back a session Cookie
    2.  The Cookie contain your session Information "kraxier"
    3. Cookie Jar is just the name for where cookies are stored in the requests library (like a real jar stores cookies)
'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
from bs4 import BeautifulSoup

# 1. Create a session
session = requests.Session()
login_url = "https://quotes.toscrape.com/login"

# 2. First GET request to fetch the CSRF token
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

# 3. Extract CSRF token (if it exists)
csrf_token = soup.select_one('input[name="csrf_token"]')["value"] if soup.select_one('input[name="csrf_token"]') else None

crsf_token_extractor = soup.select_one('input')
print(crsf_token_extractor) # Notice the Value Keep Changing 
# <input name="csrf_token" type="hidden" value="mpdsSfeTgYHvqrUnlzLuDoQhMEjOGAxNWyVRcBXZPbKaFkJCiIwt"/>
# <input name="csrf_token" type="hidden" value="pvaCZLXgtfRQsjWcEGHBPuMlVemIKwqkndhYTASNUrFOxyziJoDb"/>


# if csrf_token:
#     print("✅ CSRF Token Found:", csrf_token)
# else:
#     print("❌ No CSRF Token (Site doesn't use CSRF protection)")

# # 4. Login with the token (if required)
# login_data = {
#     "username": "kraxier",
#     "password": "12345",
#     "csrf_token": csrf_token  # Include only if token exists
# }

# response = session.post(login_url, data=login_data)

# # 5. Check if login succeeded
# if "logout" in response.text:
#     print("✅ Login Successful!")
# else:
#     print("❌ Login Failed")


'''
Token Type	                        Behavior	                                    Example Use Case
Per-Session Token	                Changes when the user logs in/out	            Basic security
Per-Request Token	                Changes on every HTTP request (most secure)	    Banking, high-security apps
Time-Based Token	                Expires after a set duration	                Balanced security & performance
'''

'''
This is why web scrapers must re-fetch tokens dynamically! If you skip this step, the server rejects your requests for security reasons.


Learning How To Test if the 
    1. Per-Session Token
    2. Per Request Token
    3. Time Based Token

Also Organizing Learning is Really Necessary 
'''