
'''Logging in Quote_to_Scrape'''


'''
HTML Website:
<body>
    <div class="container">
        <div class="row header-box">
            <div class="col-md-8">
                <h1>
                    <a href="/" style="text-decoration: none">Quotes to Scrape</a>
                </h1>
            </div>
            <div class="col-md-4">
                <p>
                
                    <a href="/login">Login</a>
                
                </p>
            </div>
        </div>
    <form action="/login" method="post" accept-charset="utf-8">
        <input type="hidden" name="csrf_token" value="hrisoNvEqlTWuafFcVOGAUmtXbLkPDKgYjQynISxCdBJpeHRZMzw">
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


    </div>
    <footer class="footer">
        <div class="container">
            <p class="text-muted">
                Quotes by: <a href="https://www.goodreads.com/quotes">GoodReads.com</a>
            </p>
            <p class="copyright">
                Made with <span class="zyte">❤</span> by <a class="zyte" href="https://www.zyte.com">Zyte</a>
            </p>
        </div>
    </footer>

</body>

'''

# Login_Website: https://quotes.toscrape.com/login
# Website to Scrape: https://quotes.toscrape.com/

# Website: https://pythonscraping.com/pages/files/form.html
# Website: https://pythonscraping.com/pages/files/processing.php
# My Next Question is how to know the next page of it? 
    # [Website Domain] + [action path]
    # https://pythonscraping.com/pages/files + /processing.php
    # https://pythonscraping.com/pages/files/form.html 
    # It Did Change Things up 
# import requests

# params = {'firstname': 'Kraxier', 'lastname': 'Luthor'}
# r = requests.post("https://pythonscraping.com/pages/files/processing.php", data=params)
# print(r.text)
# print()

'''
Question:

Why do i need to post in https://pythonscraping.com/pages/files/processing.php url instead of url https://pythonscraping.com/pages/files/form.html
    Why POST to processing.php?
        It's designed to receive data (like form submissions) and process it (save to a database, return a response, etc.).
        In this case, it likely takes firstname and lastname, processes them, and returns a confirmation message.
    Return confirmation message (e.g., "Hello Kraxier Luthor!").

POST is used to send data securely to a server.
processing.php is the server’s endpoint that handles the data.
This is how login forms, APIs, and file uploads work behind the scenes.

Understanding of Code 
    params is parameter to send a data in the proccessing.php but in term of post it stored in "data"

    How do you know the Parameter of Submissions?
        1. <input type="text" class="form-control" id="username" name="username"> # Input Type of Files Submission in HTML this part is the key name="username"
        2. 
My Own Words:
    Basically i send the "Kraxier" and "Luthor" to the processing.php which is called the "server side script" where it can proccess and handle the data 

'''

# I'm Going to try to do this also in the 
# https://quotes.toscrape.com/login
# If i log in the website of this it change from /login to https://quotes.toscrape.com/
# There are lot more complicated than the simple Submission thing 

# import requests

# params = {'username': 'Kraxier', 'password': '12345'}
# login_url = "https://quotes.toscrape.com/login"
# r = requests.post(login_url, data=params)
# print(r)

# import requests
# # login_url = "https://pythonscraping.com/pages/files/form.html"
# login_url = "https://pythonscraping.com/pages/files/processing.php" 
# params = {'firstname': 'Kraxier', 'lastname': 'Luthor'}
# r = requests.post(login_url, data=params)
# print(r)
# print("Status:", r.status_code)  # Should be 200
# print("Response:", r.text)  # Will show server's response
# print("Cookies:", r.cookies)  # Check if any auth cookies were set
'''
# Successfuly Logging in 
<Response [200]>
Status: 200
Response: Hello there, Kraxier Luthor!
Cookies: <RequestsCookieJar[]>
'''
# With Logging in and File Submission 
# Website: https://pythonscraping.com/pages/cookies/login.html
# https://pythonscraping.com/pages/cookies/welcome.php

# The Corrected URL 
import requests
session = requests.Session()
login_page = session.get("https://pythonscraping.com/pages/cookies/login.html")
login_url = "https://pythonscraping.com/pages/cookies/welcome.php" 
params = {'username': 'Kraxier', 'password': 'password'}
s = session.post(login_url, data=params)
print('Cookie is set to:')
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)

# basically Cookies is set to maintain a login state in website that you don't need to reanswering the submission thing 
# using "Session" to handle things 

# Output
'''
Cookie is set to:
{}
Going to profile page...
You're not logged into the site!<br>Visit <a href="login.html">the login page</a> to log in

i think Selenium Can handle Cookies too man 
but it really depends on how you use it man 
'''


