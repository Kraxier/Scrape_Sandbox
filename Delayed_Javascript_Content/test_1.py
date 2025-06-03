# venv_PS_Toscrape\Scripts\activate
# python test_1.py

r'''
Task: 
Scrape the Website https://quotes.toscrape.com/js-delayed/page/1/
Learning for Timeout and Stuff 
'''


r'''
Doesn't Work The Pagination code of Mine because it too fast 
If this is the Delayed Part 

Opening the Browser it take a time to load the content of it so i wonder how i can build a script for this ? 

Solution:
    1. Check if the Elements Appear and wait until it appeared so it is continually looping to get the elements appear 
    2. Wait for the Elements to appear 

Determine if the Elements first exist and then determine 
time.sleep(2.5)

My Question is 
1. If i add the Delays in my Script it is certainly easy but in real world there are random delay in a website i think so i needed a Full Proof Plan for that ?
2. Determine what are Real World Delayed vs this Website 

Manually Counting the Website takes 10 Seconds 

'''


r'''
From the Current Code it Didn't Scrape the Last Part Because of the Time so I maybe Need Adjusting the TimeSleep Part 

So Tomorrow I needed to do More Research for JS Delayed and go Full Throttle On this part 
'''
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import time # Adding delays in scripts (time.sleep()).




def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js-delayed/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    time.sleep(11.5)
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
        time.sleep(11.5)
    page.close() 
    browser.close()

with sync_playwright() as playwright:
    run(playwright)