Concept of Log In Website and Basic To Handling Sessions 

Inspired by: Web Scraping with Python By Ryan Mitchel 

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

in Terms of HTML there are many things other than Submitting basics forms like Radio Button, Checkboxes and other Inputs and if you include JAvascript the possibilities are endless thing but in the end you need to worry about 2 things the "Element Name" which can determine by looking at the source code and finding the name attribute 

If you are stuck with Complicated Looking POST form you need to know about the browser inspector developer tools especially for me which is Chrome Inpection Developer Tool ( I Needed to Study this Too)

You can also submit Files and Images which is very rare and i didn't encounter it yet and i don't want to get deep inside here because its very rare man 

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
  