import requests

# Step 1: Log in and retrieve the cookie
login_url = 'https://pythonscraping.com/pages/cookies/login.html'
welcome_url = 'https://pythonscraping.com/pages/cookies/welcome.php'
profile_url = 'https://pythonscraping.com/pages/cookies/profile.php'

# Credentials to log in
payload = {
    'username': 'Ryan',  # Replace with the correct username if needed
    'password': 'password'  # Replace with the correct password if needed
}

# Step 2: Send a POST request to log in
response = requests.post(welcome_url, data=payload)

# Check if login was successful
if response.status_code == 200:
    print('Login successful!')
    print('Cookie is set to:')
    print(response.cookies.get_dict())  # Print the cookies set by the server
else:
    print('Login failed. Status code:', response.status_code)
    exit()

# Step 3: Access the profile page
print('Going to profile page...')
profile_response = requests.get(profile_url, cookies=response.cookies)

# Print the profile page content
print('Profile page content:')
print(profile_response.text)