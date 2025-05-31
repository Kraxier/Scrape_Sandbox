
# venv_PS_Toscrape

r'''
Goal Scrape the Entirety off https://quotes.toscrape.com/js/ # A javascript Website 

Skills that Needed to Implement 
Launching a browser (chromium.launch())
Navigating to a URL (page.goto())
Extracting text (page.textContent(), page.$$eval())
Basic CSS/XPath selectors



Content Retrieval:
.text_content() - Gets all text (including hidden)
.inner_text() - Gets visible text only
.input_value() - For form inputs

State Checking:
.is_visible()
.is_hidden()
.is_enabled()
.is_checked()

Action Methods:
.click()
.fill()
.type()
.press()
.hover()

3. Advanced Locator Strategies
Filtering Locators:

# Get the third quote
third_quote = page.locator('.quote').nth(2)

# Get last matching element
last_item = page.locator('.item').last
Chaining Locators:

# Find element with class 'text' inside element with class 'quote'
quote_text = page.locator('.quote').locator('.text')
Combining Selectors:

# Element that has both classes
page.locator('.btn.primary')

# OR condition
page.locator('button:has-text("Log in"), button:has-text("Sign in")')

'''

r'''
To Do List
1. Re Learning how to Re Install the Playwright
2. Create the VENV first 
3. Do the Content Retrieval for Scrapping the JS Website
    * Defining the https://quotes.toscrape.com/js/
    * After Getting All the Data Move on to Step no. 4 

4. Experiment on State Checking 
    * Defining the Clear End Goal for State Checking 
    * Implementing Stuff 
5. Experiment on Action Method 
     *Defining the Clear End Goal for State Checking 
     Implementing Stuff on that 
6. Multiple Page Tabs and Multiple Browser When to Use it ?
7. Asynchronous Scrapping 
'''

# Installing the Playwright 
r'''

Navigate to Folders: 
eg: cd C:\Users\klabi\OneDrive\Desktop\Scrape_Quotes_To_Scrape

Create the VENV: 
eg: python -m venv venv_PS_Toscrape

Activate the VENV: 
venv_PS_Toscrape\Scripts\activate

Using the VENV for any folder access 
if your folder is: cd C:\Users\klabi\OneDrive\Desktop\Scrape_Quotes_To_Scrape\Javascript

Activate it Using: 
..\venv_PS_Toscrape\Scripts\activate

or 
Navigate to 
cd C:\Users\klabi\OneDrive\Desktop\Scrape_Quotes_To_Scrape
Activate the VENV and then CD to Javascript 
'''

# new_playwright_venv\Scripts\activate
# python test_1.py

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin

def run(playwright: Playwright):

    base_url = "https://quotes.toscrape.com/js/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=True) 
    page = browser.new_page()
    page.goto(base_url)
    print(page.title())
    # Printing the Header of the Website Trying the Simple Extraction
    h1_text = page.locator('h1').text_content()
    print(f"H1 text: {h1_text}")


    # quote = page.locator('.quote .text').all()
    # for quote in quote:
    #     print(quote.text_content())

    # 10 URL and i needed to loop it to create paginations 

    # next_page_partial = page.locator('.next a').get_attribute('href')
    # next_page_url = urljoin(base_url, next_page_partial) 
    # print(next_page_url)
    # page_2 = browser.new_page()
    # page_2.goto(next_page_url)

    # Creating a Paginations for the Next URL
    while True:
        # Getting the href from the page.locator itself
        # So the Problem is "page" itself because it will infinitely loop in there 

        next_page_partial = page.locator('.next a').get_attribute('href')
        next_page_url = urljoin(base_url, next_page_partial) 
        print(next_page_url)
        page_2 = browser.new_page()
        page_2.goto(next_page_url)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

