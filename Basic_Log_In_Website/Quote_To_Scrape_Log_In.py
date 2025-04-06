

'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
from bs4 import BeautifulSoup


session = requests.Session()
login_url = "https://quotes.toscrape.com/login"

login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

csrf_token = soup.select_one('input[name="csrf_token"]')["value"] if soup.select_one('input[name="csrf_token"]') else None

crsf_token_extractor = soup.select_one('input')
print(crsf_token_extractor) 
'''


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