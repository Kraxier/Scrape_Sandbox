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