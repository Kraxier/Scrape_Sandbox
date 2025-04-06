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
