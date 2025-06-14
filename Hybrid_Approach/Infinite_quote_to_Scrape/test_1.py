# Scrape the Infinite Scrolling in Quotetoscrape.com
# test_1.py

r'''
Core Playwright Skills i needed based on Deepseek
1. Page Interaction
    page.evaluate() - Execute JavaScript in the page context
    page.mouse.wheel() - Simulate scroll actions
    page.waitForFunction() - Wait for specific conditions

2. Scroll Detection & Handling
    Detect when new content loads (DOM mutations)
    Track scroll position vs page height
    Identify "loading" indicators/spinners

3. Waiting Strategies
    page.waitForSelector() - Wait for new elements to appear
    page.waitForTimeout() (use sparingly)
    Custom wait conditions using promises
'''

r'''
My Observation in Infinite Scrolling

After Scrolling for a while if i reach the max quote 
i think 10 Quotes it will load another 10 Quotes 

I should observe in the DOM part if it is interactive changes 
    In Inspecting Elements i think something changing and i had no idea about that 

Next button is not Really needed 
'''

r'''
Based on the Recommendation of Deepseek i should Research about that and implement Really fast 

I quite notice that based on the deepseek he recommend me some of the concept that i needed 
but the learning part is also why he did put it from there to there that is a good question
'''


from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    page.mouse.wheel(0, 500)  # Scrolls down 500 pixels

    # for x in range(1,5):
    #     current_url = page.url
    #     print()
    #     print(f"Currently Scrapping {current_url}")
    #     page.wait_for_selector(".quote .text", timeout=12000)
    #     quotes = page.locator(".quote .text").all()
    #     for quote in quotes:
    #         print(quote.text_content())
    #         print()
        
  
        # next_page = page.locator('.next a')
        # next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
        # page.goto(next_page_url)
        # print()
        # print(f"Going to the Next Page {next_page_url}")

    # 1. Page Interaction
        # page.evaluate() - Execute JavaScript in the page context
        # page.mouse.wheel() - Simulate scroll actions
        # page.waitForFunction() - Wait for specific conditions

     # 1. page.evaluate()
        # Purpose: Execute JavaScript in the page context (e.g., extract data or manipulate the DOM).
        # What does it mean by Execute Javascript in the page context?
        # What does it mean by Manipulate the DOM? 
    
    
    input("Press Enter to close the browser...")
    #page.pause()
    # import time
    # time.sleep(30)  # Keeps browser open for 30 seconds
    # Why it Comments 
    #page.close() 
    #browser.close()

with sync_playwright() as playwright:
    run(playwright)
