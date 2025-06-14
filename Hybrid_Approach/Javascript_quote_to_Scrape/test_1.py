
# I think I'm Done in this part 
# Goal Scrape the Website 
# python test_1.py
r'''
Just Print it, because it means i can scrape the website 
'''
r'''
How can you know if you truly understand the code without copy pasting it and lying to yourself that you understand it? 

Core Principles: 
    1. Active Manipulation of the code changing the context of it 
    2. Verbalization: Explaining it in my own words
    3. Prediction: I can see the effects of it changes 
    4. Problem Solving: to Fix or to Create Something
    
Rubber Duck Debugging + Feynman + Whiteboard Diagram:
    Explain the Code line by line while also teaching it 

Or Just Recreate it the Entire program
'''

# Rewriting the Program Only going to 1 - 5th Page
  
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)

    for x in range(1,5):
        current_url = page.url
        print()
        print(f"Currently Scrapping {current_url}")
        quotes = page.locator(".quote .text").all()
        for quote in quotes:
            print(quote.text_content())
            print()
        next_page = page.locator('.next a')
        next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
        page.goto(next_page_url)
        print()
        print(f"Going to the Next Page {next_page_url}")


    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


r'''
Go to:
    https://quotes.toscrape.com/js/
Scrape the Entire Quotes and print it 
Get the Href Attribute of "Next Page"
Using that Href Attribute to go to the next_page_url 

Now Repeat it 5 Times

'''

r'''
Q1: What core Playwright concept does this implement?  
Q2: Why does this specific approach work?  
Q3: What would happen if [key variable] changed?  
Q4: How does this relate to previous concepts?  
Q5: What's the underlying browser mechanic?  

'''