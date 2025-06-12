# This is the Goal for Javascript Website
# venv_PS_Toscrape\Scripts\activate
# python goal.py

r'''
Hybrid Approach Gradually Implement Things

To Do List 
1. Launching a browser (chromium.launch())
    Chrome
    Firefox
    Websocket (WebKit (Safari's engine)
    Multiple Tabs 
    Multiple Browser
2. Data Extraction 
    Getting the elements Safety
    Content Retrieval 
    State Checking 
    Basic CSS/XPath selectors
    Extracting text (page.textContent(), page.$$eval())
. Navigating URL 
    Paginations 
    Paginations on Multiple Tabs 
    Pagination on Multiple Browser 
__________________________________________________
2. Hidden vs Visible Text (Content Retrieval)
.text_content()
    Gets ALL text content, including:
        Text hidden with CSS (display: none, visibility: hidden)
        Text inside <script>, <style> tags
        Text in hidden input fields (<input type="hidden">)
    Questions: Why they need to hide things?
.inner_text()
    Gets only visible text (what a user actually sees on screen). 
    Respects CSS visibility rules.

Use .text_content() when you need raw data (e.g., scraping metadata).
Use .inner_text() when testing user-facing content (e.g., verifying UI text).

2. State Checking (Explained)
Method              Purpose                                                     Example Use Case
.is_visible()	    Checks if element is visible on the page	                Verify a modal appears
.is_hidden()	    Checks if element is not visible (or doesn't exist)	        Confirm a loading spinner disappears
.is_enabled()	Checks if element is clickable/editable (not disabled)	        Test if a submit button is active
.is_checked()	Checks if checkbox/radio is selected	Validate a "Terms & Conditions" checkbox
'''


from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    # Testing Different Browser
    chromium = playwright.chromium
    # chromium = playwright.firefox
    # chromium = playwright.webkit
    r'''
    Firefox: playwright.firefox
    WebKit: playwright.webkit

    I notice that in terms of Firefox it is really fast 
    Conclusion: Stick to Chrome because user almost use that 
    '''
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    while True: 
        next_page = page.locator('.next a')
        quotes = page.locator(".quote .text").all()
        for quote in quotes: 
            print(quote.text_content())
            print()
        if next_page.count() == 0:
            print("Reached last page. Stopping.")
            break
        next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
        print(next_page_url)
        page.goto(next_page_url)
    page.close() 
    browser.close()

    

with sync_playwright() as playwright:
    run(playwright)

# ⌚ 📱 💻 🖥️ 🖨️ 🔋 🔌 💡 🔦 🕯️ 🧯 📷 📺 📻 🧭 🔑 🪑 🛏️ 🚪


