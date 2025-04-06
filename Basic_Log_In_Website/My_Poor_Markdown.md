# Concept of Log In Website and Basic To Handling Sessions 

Inspired by: Web Scraping with Python By Ryan Mitchel 


# Introductions
Logging in the Website and Sessions is one of the most important Web Scrapping Skills that the Web Scraper are needed to learn but it require an understanding 
so this is some of the things that i needed to learn in order to scrape a website that have a login in their website 

We will need to understand the "POST" method where you are the one who pushes information to a web server for storage and analysis where the "GET"  method is the one that request information from the web server 

One of the Most Common tool in order to do this is the "Python Request Library" where the Implementation of the code is $ import requests 

The Next thing we needed to understand is "Submitting Basic Form"
where in term of HTML this is something like this 
$ <form method="post" action="processing.php">
$ First name: <input type="text" name="firstname"><br>
$ Last name: <input type="text" name="lastname"><br>
$ <input type="submit" value="Submit">
$ </form>

Noticing the $ name="firstname" and name="lastname" 
where you needed to use that as a parameter in your code like this 
$ params = {'firstname': 'Kraxier', 'lastname': 'No_Lastname'}

After you got the parameter you can do 
$ r = requests.post("http://example.com/pages/processing.php", data=params)
The best Explanation of this line of code is 
r = requests.post(url, data={key: value}, json={key: value}, headers={key: value})
url is the endpoint you're sending the request to (required)
data is for sending form-encoded data (optional)
json is for sending JSON data (optional)
headers allows you to send HTTP headers (optional)

where the url should be the endpoint not the log_in page itself sending the POST request to the main page (not the login page)
data is the parameter thing , json I'm not sure of this, header is one thing i have familliarity in 

but the Most Important thing to do is 
1. The name of the field (or fields) you want to submit with the data
2. The action attribute of the form itself; that is, the page that the form posts

fron learning this stuff you can basically 
1. Spam the publisher with invalid signups which can create a Load in the Server so use this power as a good thing 

When you submit a form in a web page, the <form> tag defines two important attributes:
method="post" → Specifies that the form data should be sent using the POST method.
action="processing.php" → Defines the URL where the form data should be sent.

 The action="processing.php" means that when you click the Submit button, the browser will send the form data to processing.php.
    Since the form is located at https://pythonscraping.com/pages/files/form.html, the processing.php file is relative to this URL. 
    This means that the full URL where the data should be

    What Happens If You Send Data to the Wrong URL?
    If you send your POST request to https://pythonscraping.com/pages/files/form.html, you’re just making a request to the form page itself, not the server-side script that processes the form.
    That’s why you’re getting back the HTML of the form itself instead of a response confirming that your data was received.



in Terms of HTML there are many things other than Submitting basics forms like Radio Button, Checkboxes and other Inputs and if you include JAvascript the possibilities are endless thing but in the end you need to worry about 2 things the "Element Name" which can determine by looking at the source code and finding the name attribute 

If you are stuck with Complicated Looking POST form you need to know about the browser inspector developer tools especially for me which is Chrome Inpection Developer Tool ( I Needed to Study this Too)

You can also submit Files and Images which is very rare and i didn't encounter it yet and i don't want to get deep inside here because its very rare man 


# How to handle Logins and Cookies
Next Thing We needed to Know is How to Handle Logins and Cookies 
    The next thing we should know is how to handle the log in state because we already established on how to "Submit Forms" which is equivalent of Handling Logins but the next things is Maintaining the Log in State because you don't want to remain in the website that keep logging in man 

    Most Modern Website use cookies to keep track who is logged in and who is not after you a site authenticate your log in credentials it store it in browser cookies 

    Browser Cookies contain Server Generated Token, Time Out and Tracking Information 

    we Handle cookies using "Sessions" in Request Library 
    $ import requests
    $ session = requests.Session()
    $ r = sessions.post("http://example.com/pages/processing.php",

    Sessions track information like cookies, headers, and even Information protocols like HTTP and HTTPAdapters

    It's Important to always be aware of what the Cookies look like and what they are controlling when writing a web scrapers this means 

    1. You need to Inspect the cookies names and Values (e.g., session_id=abc123).
    2. Expiration times (session cookies vs. persistent cookies).
    3. HTTP-only, Secure, or SameSite flags (which affect how they're sent).
    4. Session tracking: Some sites track user behavior via cookies.
    5. CSRF protection: Some cookies (like csrftoken) are used to prevent unauthorized requests.
    6. Rate limiting: Cookies can track how many requests you’ve made.

    Very Important to not get blocks, Maintain the Sessions and Mimicks real users 

    You can also use the Selenium Library 

    Some Website Use HTTP Basic Authentication that you can see it from time to time for high security or corporate site 
    

log_in_1.py:
I use the fundamental that i learn in a web scrapping book 
Website: https://quotes.toscrape.com/login
Implementing the Basics in Logging in 
1. "post method" 
2. learning the "Request" Library to know what it is capabilities
3. learning the "Chrome Inspect Developer Tools"
  

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
1. What is a Cookie?
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

Understanding the How to Submit Forms and Login


1. Understanding the HTML Forms
	A. What is the Form and Structure of HTML Forms?
	- It's common in website that have login forms and usually that have input like username, email and password and submit button/ Login Butto
	B. What Happen if you clicked to "Submit/Log in"?
	- The data you entered will get process by a server 
	C. In <form method="post" action="processing.php"> What is "action" Attribute?
	- This tell the browser to where the data will get send 
	- in This case it will go to "processing.php"
	D. What is the "method" Attribute?
	- Specifies how the data is sent 

2. What is the Difference of processing.php and form.html?
- form.html is a structure to see where the form is and it doesn't process the data
- processing.php is a server-side script that handle the data you submit and send back a response 

3. What is the Difference between Traditional forms and Modern Website?
- Traditional form: are the foundation of how data is sent and processed some smaller website use this traditional method also it teach you the concepts like HTTP methods (GET,POST) data handling and Server Side Processing 
- Modern Website and APIS: most modern website use JavaScript to send data to APIs this is much more complex yet follow the same principle in traditional form (sending data to a server, processing it, and getting a response). You also neeed to use different tools to work with this modern website like Chrome Developer, Inspecting Network Request, Handling Authentication Tokens and Using the Libraries like Selenium. 


4. What is HTTP Method?
The Foundation of communication on the Web like how the data is set and receive between you as a client( Your Browser) and a Server 

5. What is Get?
- Requesting data from the server when you click a link or put a url in your browser you "Get request" to the server 

6. What is Post?
To Send a Data to a server to update or create resources [ Login forms or File Uploads] 

7. What is Server Side Processing?
refer to the work done by the server to handle a request and generate a response, 

Understanding the Browser Developer Tools 

1. For Login What is Network Panel?
	- Monitor Network Activity: View all network requests, including their methods, statuses, and response times.

Example: Submit a form and observe the POST request in the Network tab to see the data being sent.

