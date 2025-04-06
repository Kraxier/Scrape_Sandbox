import requests

params = {'firstname': 'Kraxier', 'lastname': 'Luthor'}
r = requests.post("https://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)

# start_url = 'https://pythonscraping.com/pages/files/form.html'
# from bs4 import BeautifulSoup
# response = requests.get(start_url)
# print(response)

# Based on my Understanding the request but "post" the parameter of things 
'''
# This is the HTML of this URL: https://pythonscraping.com/pages/files/form.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h2>Tell me your name!</h2>
    <form method="post" action="processing.php">
        <label for="firstname">First name:</label>
        <input type="text" id="firstname" name="firstname" required><br><br>

        <label for="lastname">Last name:</label>
        <input type="text" id="lastname" name="lastname" required><br><br>

        <input type="submit" value="Submit" id="submit">
    </form>
</body>
</html>

'''

'''
In terms of Login in the Website after Typing my name it Give me this 
Hello there, Kristian Binas!

But in Requesting in Python in the Code Itself it give me this 
Hello there,  !


The Question of 
Why is that after logging in i shoud put this url ? 
https://pythonscraping.com/pages/files/processing.php

instead of the Url itself which is 
https://pythonscraping.com/pages/files/form.html

Explain by Chatgpt:

    Understanding How HTML Forms Work
    When you submit a form in a web page, the <form> tag defines two important attributes:
    method="post" → Specifies that the form data should be sent using the POST method.
    action="processing.php" → Defines the URL where the form data should be sent.

    The action="processing.php" means that when you click the Submit button, the browser will send the form data to processing.php.
    Since the form is located at https://pythonscraping.com/pages/files/form.html, the processing.php file is relative to this URL. 
    This means that the full URL where the data should be

    What Happens If You Send Data to the Wrong URL?
    If you send your POST request to https://pythonscraping.com/pages/files/form.html, you’re just making a request to the form page itself, not the server-side script that processes the form.
    That’s why you’re getting back the HTML of the form itself instead of a response confirming that your data was received.

    Key Takeaways
        1. Always check the action attribute of the form to determine where the data should be sent.
        2. The processing script (e.g., processing.php) is responsible for handling the form submission.
        3. Sending a request to the wrong URL means the server doesn’t know how to process your data, and you might just receive the form page back.

Focusing Entirely in the Name of the Attriibute 


_____________________________________________________________________

Understanding the Forms more in terms of this 2 Things 
The name of the element (the name attribute of an input field).
The value of the element (the data you enter or that is automatically filled in).

# Simple Form 
<form method="POST" action="/submit">
    <input type="text" name="username" value="JohnDoe">
    <input type="password" name="password" value="mySecret">
    <input type="submit" value="Login">
</form>

# The name attributes are "username" and "password".
# The values are "JohnDoe" and "mySecret" (what gets sent to the server).
# When the form is submitted, it sends this data in a POST request:

{'username': 'JohnDoe', 'password': 'mySecret'}



'''



'''
From my Question of the Difference of Forms in HTML and the Latest and most Modern Website like the Upwork or Instagram Forms 
where the Java and Instagram Forms are using API and Javascript 

# Many websites today use JavaScript-based authentication instead of traditional form
* Instead of <form action="login.php">, the form sends data via JavaScript to a hidden API URL.
* This API URL is not visible in the HTML but can be found in the network requests.

Need to Inspect the Network Activity 
    1. Require Expertise in "Inspect or Chrome Developer Tools"
    2. Understanding X-crsf token 
    3. Understanding the Javascript Verification
    4. Expertise in Selenium 
    5. Learning Byassing Bot Detection [ Handling CAPTCHA's Rotating Proxies]

My Next Question is What is the Purpose of Learning Submitting Forms if the modern website use it different?
    * Modern Website Use Javascript Heavy Frameworks 
    * Smaller Website don't use javascript heavy frameworks 
    * Admin panels, dashboards, and internal company websites that have simple login forms.
    * Government websites, university portals, and older sites that still rely on standard form actions.
    * APIs and backend services that process form data similarly to how browsers handle them
    
    * Traditional Forms works i'm learning the Foundation Concept 
    
    Modern Website still follow the same data flow 
        1. Collect User Input from an HTML form 
        2. Proccess the data using a backend server
        3. Validate and Authenticate the request
        4. Redirect the User after login 

        Your knowledge of forms helps you understand where to look for login submission details (like API endpoints) when scraping.
        By learning about form submissions, you are also learning: ✅ How HTTP works (GET vs. POST requests).
        ✅ How web authentication works (sessions, cookies, tokens).
        ✅ How data is structured in HTTP requests (headers, form data, JSON).
        ✅ How to simulate a browser with Python (requests, Selenium).

        Find the login API URL (using DevTools → Network Tab).
        Use the same concepts (sending a POST request, adding headers, etc.).
        Handle authentication tokens and cookies (to stay logged in).

'''