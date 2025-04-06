import requests

# params = {'username': 'Kraxier', 'password': 'Luthor'}
# r = requests.post("https://pythonscraping.com/pages/cookies/welcome.php", data=params)
# print('Cookie is set to:')
# print(r.cookies.get_dict())



# https://pythonscraping.com/pages/cookies/welcome.php



import requests
session = requests.Session()
params = {'username': 'username', 'password': 'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)
# Pg 156 Understanding Cookies 