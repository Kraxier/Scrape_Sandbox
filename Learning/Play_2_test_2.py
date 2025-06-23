# new_playwright_venv\Scripts\activate
# python test_2.py

# from playwright.sync_api import sync_playwright, Playwright
# def run(playwright: Playwright):
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=True) 
#     page = browser.new_page()
#     page.goto("https://quotes.toscrape.com/js/")
#     print(page.title())
#     # Printing the Header of the Website Trying the Simple Extraction
#     h1_text = page.locator('h1').text_content()
#     print(f"H1 text: {h1_text}")


#     quote = page.locator('.quote .text').all()
#     for quote in quote:
#         print(quote.text_content()) 
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)


# import requests
# from bs4 import BeautifulSoup

# # URL of the quotes page to scrape
# # url = "https://quotes.toscrape.com" # Testing the Actual Quotetoscrape to see if it is working and the code is working 
# url = "https://quotes.toscrape.com/js/"

# # Send a GET request to the website
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all quote elements - inspect the page to find the right selectors
#     quotes = soup.find_all('div', class_='quote')
    
#     # Loop through each quote and extract information
#     for quote in quotes:
#         # Extract the quote text
#         text = quote.find('span', class_='text').text
#         # Extract the author
#         author = quote.find('small', class_='author').text
#         # Extract tags
#         tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        
#         # Print the extracted information
#         print(f"Quote: {text}")
#         print(f"Author: {author}")
#         print(f"Tags: {', '.join(tags)}")
#         print("\n" + "="*50 + "\n")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")


r'''
Understanding Why the Playwright Works and HTML Parsing like Beautiful Soup and Request is not Working Against the Site 
# My Reflection is i overthink how javascript will be complex but after running the code it definitely working and it super easy for some reason and i just need understanding of why? 


Playwright vs Request + BeautifulSoup: Key Differences

What is Request and Beautiful Soup Fundamentally 
    * HTTP Request Only: Just fetches the initial HTML document from the server
        # What does it mean by HTTP Request Only?+
        # But it said that it goes right into the server 
    * No JavaScript Execution: Gets only static HTML content
    * Lightweight: Minimal resource usage
    * Fast: No browser overhead
    * Limited: Can't interact with dynamic content
    
What is Playwright Fundamentally? 
    * Full Browser Automation: Controls an actual browser (Chromium, Firefox, WebKit)
    * JavaScript Execution: Renders pages exactly like a real user would see them
    * Heavier: Requires browser instances
    * Slower: Has to load all page resources
    * Powerful: Can handle all modern web interactions

It give me a neat Diagram called "Sequence Diagram"

Basically a Beautiful Soup and Request are like this 
My Code -----> Server # Going Straight into the Server getting the HTML
# The Problem with this is there are no JS execution 

In Playwright 
My Code ----> Browser ----> Server 

My Code 
    1. Launch the Actual Browser
Browser 
    1. Execute the Javascript, Render the DOM, Load Dynamic Content
    2. Request top the Server With Full Headers 
    3. Getting the HTML AND JS AND CSS back to my Code a Fully Rendered Page

Each of this have their own Advantage and Disadvantage 
and i can combine Both of them 

'''


r'''
Determining my Proficiency and the Level of Playwright 

in This Deepseek Research and Break it Down 
https://chat.deepseek.com/a/chat/s/4c00b2f2-b0ed-434e-9992-d5e137c4e955

1. Fundamental Competence (Beginner)
Basic Usage: Launching browser, navigating pages, simple text extraction
    Uses basic selectors (CSS/XPath)
    Basic page navigation and content extraction
    Handling iframes and shadow DOM
    Managing multiple tabs/windows
    File downloads/uploads
    Taking screenshots/PDFs

    Dynamic Content Handling
        Waiting for elements to appear/disappear
        Handling infinite scroll
        Dealing with lazy-loaded content
        Processing WebSocket data
        Intercepting and modifying network requests

2. Intermediate Proficiency
Complex Interactions: Form filling, dropdown selection, pagination
    Indicators:
        * Implements explicit waits (wait_for_selector, wait_for_timeout)
        * Handles common anti-bot techniques (basic ones)
        * Can scrape multi-page dynamic content
        * Uses more advanced selectors (>> chaining, :has-text())
3. Advanced Mastery
Stealth Techniques: Full browser fingerprint masking
    Indicators:
        Implements proxy rotation
        Handles Cloudflare and other advanced anti-bot systems
        Can reverse-engineer complex API calls
        Builds custom browser automation patterns




'''

r'''

'''