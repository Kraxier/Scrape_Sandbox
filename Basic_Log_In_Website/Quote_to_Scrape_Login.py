# Login Page_url = https://quotes.toscrape.com/login
# Going to: https://quotes.toscrape.com/

'''
To Check Wether i log in is there is a "logout"
'''

# Didn't Log in Due to crsf Token 
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# import requests
# session = requests.Session()
# login_url = "https://quotes.toscrape.com/"
# params = {'username': 'Kraxier', 'password': 'password'}
# s = session.post(login_url, data=params)
# s = session.get('https://quotes.toscrape.com/')
# if "Logout" in s.text:
#     print("Logged in successfully!")
# else:
#     print("Login failed")
# # logout_button = s.select_one('a:contains("Logout")')

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
from bs4 import BeautifulSoup
session = requests.Session()
login_page = session.get("https://quotes.toscrape.com/login")
soup = BeautifulSoup(login_page.text, 'html.parser')

# Getting Crsf Token
csrf_token = soup.select_one('input[name="csrf_token"]')['value']
print(csrf_token)
'''
<input type="hidden" name="csrf_token" value="MnmNLJfaSeUyQoDvYrHwOCVqBzIGEKxgjRtTuiXAsdbplZkPWhFc">
'''
login_data = {
    'username': 'Kraxier',  
    'password': '123456789',
    'csrf_token': csrf_token  
}
response = session.post("https://quotes.toscrape.com/login", data=login_data)
if "Logout" in response.text:
    print("Success! You’re logged in.")
else:
    print("Failed. Check the token/form data.")

# Contain session data
print(session.cookies.get_dict())
# Knowing My Site i'm currently in 
print(f"Current URL: {response.url}")
print(f"Redirect history: {response.history}")
'''
What does 302 Mean?
A HTTP 302 status code means "Found" (previously called "Moved Temporarily"). 
It's a redirect response from the server telling your browser (or script) to automatically go to a different URL. 
'''

'''
I'm DOne Logging in the Quotetoscrape

Maybe Organizing Things is the Key Here Man Becuase i get things Job from now on 
    
Figuring out the Next Steps at things 


'''