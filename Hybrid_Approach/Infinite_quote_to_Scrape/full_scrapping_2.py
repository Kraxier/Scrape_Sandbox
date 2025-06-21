
r'''Based on the Research the Total Quotes are 200'''
r'''
Recommendation Srapping: https://www.behance.net/galleries?tracking_source=nav20
https://scrapeops.io/playwright-web-scraping-playbook/
I think this can help me in things for the Gap Learning 

I already Scrapped Everything for some Reason because i check the Website and the Total Quotes are 100 Only 
a mind needs books as a sword needs a whetstone, if it is to keep its edge. # This is the Last Thing and i scraped it 


'''
from playwright.sync_api import sync_playwright, Playwright
import time

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    page.wait_for_selector(".quote", state="attached")

    last_height = page.evaluate("document.body.scrollHeight")
    quote_count = 0
    max_scroll_attempts = 20  # Prevent infinite loop
    scroll_attempts = 0

    while scroll_attempts < max_scroll_attempts:
        # Scroll to bottom and wait for new content
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)  # Allow time for dynamic loading

        # Check if new content was loaded
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break  # No more new content
        last_height = new_height
        scroll_attempts += 1

    # Extract all quotes after scrolling
    quotes = page.locator(".quote .text").all()
    for quote in quotes:
        print(quote.text_content())
        quote_count += 1
        print(f"Quote Count: {quote_count}")
        print()

    print(f"Total Quotes Found: {quote_count}")
    page.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

r'''
1. Auto-scrolling until no more content loads:
    Continuously scrolls to the bottom (document.body.scrollHeight).
    Waits for new content (using time.sleep(2) for simplicity; could also use page.wait_for_function).
    Stops when the page height stops increasing.

2. Prevents infinite loops:
    Uses max_scroll_attempts to avoid endless scrolling if something goes wrong.

3. Accurate quote count:
    Only counts quotes after all scrolling is done, ensuring no duplicates.
'''



# My Code 
# from playwright.sync_api import sync_playwright, Playwright
# from urllib.parse import urljoin


# def run(playwright: Playwright):
#     base_url = "https://quotes.toscrape.com/scroll"
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False) 
#     page = browser.new_page()
#     page.goto(base_url)
#     page.wait_for_selector(".quote", state="attached")

    

#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     page.wait_for_timeout(3000)  


#     quotes = page.locator(".quote .text").all()
#     quote_count = 0 
#     for quote in quotes: 
#         print(quote.text_content())
#         quote_count += 1
#         print(f"Quote Count: {quote_count}")
#         print() 
#     page.close() 
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)



# Identifying the Challenges for Infitinite Scrolling 
# Challenges in Scraping Infinite Scroll Pages
r'''
1. Dynamic Content 
2. Incomplete Initial Response 
    The Initial HTML response may not contain all the data available on the page
3. Asynchronous Loading 
    Multiple request in the server as the background user scroll 
4. Dynamic Selectors 
    Infinite Scrolls may have dynamically generated ID or Classes
5. Rate Limiting and Throttling 
    As Infinite scroll pages require multiple request to load it can trigger
    rate limiting or throttling mechanism increasing the blocked  by website

    
Method 2: Simulate Background API Requests
Simulating background API requests is another approach to handle infinite scroll pages, 
especially when the website dynamically loads content using AJAX or similar techniques.

This method involves inspecting the network traffic in the browser's developer tools to 
identify the API endpoints responsible for fetching additional content.
'''
