'''
Understanding the 3 Key Roles with Web Authentication 

1. What is Sessions 
- is a temporary connection  between Client and Server
- Server create sessions to track your activity 
- Sessions are identified using "Sessions Ids" stored in Cokkies or Headers
- It typically expire a certain period of time or inactivity

2. How Sessions Work
    A. You log in a website sending your username and password
    B. Website check and verified your credential creating a session 
    C. A session ID is stored in your cookies on your browser
    D. for every request your browser automatically sends the session ID, allowing you to remain logged in
    E. When you log out the session is Deleted in the browser
'''
# Code Examples: 
import requests

session = requests.Session()  # Creates a session object
login_url = "https://example.com/login"
login_data = {"username": "user", "password": "pass"}

session.post(login_url, data=login_data)  # Login and store session cookies
response = session.get("https://example.com/profile")  # Session persists
print(response.text)

# My Own Foundational Concept 
# params = {'firstname': 'Kraxier', 'lastname': 'Luthor'}
# r = requests.post("https://pythonscraping.com/pages/files/processing.php", data=params)
# print(r.text)
'''
Understanding 
    1. params and login_data is quite the same
    2. they just add the session part 
'''
'''
Question from the Code 
    1. 
'''


'''
2. What is a Cookie?
    - A cookie is a small piece of data stored in your browser by a website.
    - Used for tracking sessions, authentication, and preferences.
    - Stored as key-value pairs in the browser.
    - Can be temporary (session cookies) or persistent (stored cookies).
    - Websites set cookies in the Set-Cookie header.

Example: How Cookies Work
    - You log in → The server sends a cookie with Set-Cookie: session_id=abc123.
    - Browser stores the cookie.
    - Next request to the website → The cookie is sent automatically in Cookie: session_id=abc123.
    - Server identifies you based on the session ID.

📌 Why use cookies?
    - They allow websites to remember users without requiring re-authentication.
    - Web scraping tools like requests and Selenium use cookies for persistent logins.
'''

import requests

session = requests.Session()
login_url = "https://example.com/login"
login_data = {"username": "user", "password": "pass"}

response = session.post(login_url, data=login_data)
print(session.cookies)  # Prints session cookies


'''
3. What is a Token?
    A token is a piece of data used to verify identity and protect against security threats like CSRF (Cross-Site Request Forgery) and authentication attacks.
    CSRF tokens prevent attackers from performing unwanted actions on behalf of users.
    Authentication tokens (JWT, OAuth, API keys) allow users to access resources securely.
    Tokens are often short-lived and must be refreshed.

Example: How a CSRF Token Works
    You visit the login page → Server generates a CSRF token.
    The token is included in the form as:
    <input type="hidden" name="csrf_token" value="123xyz">
    When you submit the form, the server verifies if the token matches.

If the token is missing or incorrect, the request is rejected.
'''
import requests
from bs4 import BeautifulSoup

session = requests.Session()
login_page = session.get("https://example.com/login")

soup = BeautifulSoup(login_page.text, "html.parser")
csrf_token = soup.find("input", {"name": "csrf_token"})["value"]

login_data = {"username": "user", "password": "pass", "csrf_token": csrf_token}
response = session.post("https://example.com/login", data=login_data)
print(response.text)

# 📌 Why use tokens?

# Prevent CSRF attacks.

# Authenticate users securely.

# Used in APIs (JWT, OAuth) for authentication instead of session cookies.



