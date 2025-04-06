# import requests
# params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
# r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi",
# data=params)
# print(r.text)


# Chatgpt Code 
import requests

url = "http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi"
data = {
    "client_token": "oreilly",
    "subscribe": "optin",
    "success_url": "http://oreilly.com/store/newsletter-thankyou.html",
    "error_url": "http://oreilly.com/store/newsletter-signup-error.html",
    "topic_or_dod": "1",
    "source": "orm-home-t1-dotd",
    "email_addr": "ryan.e.mitchell@gmail.com",
}

r = requests.post(url, data=data)
print(r.text)