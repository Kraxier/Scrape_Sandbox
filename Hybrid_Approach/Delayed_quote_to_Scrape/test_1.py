# python test_1.py
# venv_PS_Toscrape\Scripts\activate
r'''
I already Scrape it based on the Solution of time.sleep importing the module of time 
The Concept Behind it is 
'''

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js-delayed/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)

    for x in range(1,5):
        current_url = page.url
        print()
        print(f"Currently Scrapping {current_url}")
        # quotes = page.locator(".quote .text").all()
        # checker_quote = page.wait_for_selector(".quote .text", timeout=12000)
        page.wait_for_selector(".quote .text", timeout=12000)
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
    # def next_page_Function(url_next_page):
    #     url_next_page = urljoin(base_url, next_page.get_attribute('href')) 
    #     pass


with sync_playwright() as playwright:
    run(playwright)

# First Solution is Time Module
# Second Solution is to Wait the Program to Respond like we are not going to the next page if we didn't print everything
# Figure out right now that i still lacking experience in Function man especially the Return thing 

r'''
Reflection Phased: 
Q1: What core Playwright concept does this implement?  
It Apply the Explicit Waiting Thing $ page.wait_for_selector()

Q2: Why does this specific approach work?  
This Handle the JS delayed because it dynamically render the quotes 

Q3 What are the Alternative i can Implement 
Option 1: Modern Locator Expectations (Recommended)

from playwright.sync_api import expect

# Wait for MINIMUM 1 quote to be visible
$ expect(page.locator(".quote .text")).to_have_count(count=1, timeout=12000)
$ quotes = page.locator(".quote .text").all()
# expect is not good for web Scrapping 

Option 2: Wait for Exact Quote Count
# Wait for EXACTLY 10 quotes (if you know the count)
$ expect(page.locator(".quote .text")).to_have_count(10, timeout=12000)

Option 3: Custom JavaScript Condition
$ page.wait_for_function("""
  $ () => document.querySelectorAll('.quote .text').length > 0
$ """, timeout=12000)
$ quotes = page.locator(".quote .text").all()

Option 4: Network-Based Waiting (If Quotes Load via API)
# Wait for API response that provides quotes
page.goto(url, wait_until="networkidle")  # or intercept specific API call

Q4: Is This the Best Way for JS-Delayed Content?
✅ Good: Explicitly waiting for .quote .text is the correct approach for content loaded via JS.
⚠️ Improvement Needed: Add a secondary wait inside the loop after page.goto() to handle delays during page navigation:

Notes:
✅ Why expect is GREAT for Web Scraping
Automatic Retries & Smart Waiting:
expect(locator).condition() automatically retries until the condition is met (or times out).
→ No need to guess fixed delays (e.g., time.sleep(5)), which are unreliable for dynamic sites.
→ Combines waiting and assertion in one line.
→ Handles flaky networks, slow JS rendering, and element stalling better than manual methods. (Built in Resillience)

🚫 When to Avoid expect
Only if:
You need low-level control over waiting logic (rare in scraping).
You’re in an async context and prefer callbacks (but expect works in async too).

💡 Key Takeaways
expect is NOT just for tests – it’s a robust tool for production scraping.
Always wait for content after navigation (goto(), click(), etc.).
Combine with .all() to scrape multiple elements after waiting.
'''



r'''
Logging Error of Mine 

1. I was Trying to if it is visible and then run the next_page locator 
 File "C:\Users\klabi\OneDrive\Desktop\Scrape_Quotes_To_Scrape\Hybrid_Approach\Delayed_quote_to_Scrape\test_1.py", line 26, in run
    if quotes.is_visible():
    AttributeError: 'list' object has no attribute 'is_visible'

2. Same Line 
    UnboundLocalError: cannot access local variable 'quote' where it is not associated with a value

3. I change this quotes = page.locator(".quote .text").all() to this quotes = page.wait_for_selector(".quote .text", timeout=12000)
    TypeError: 'ElementHandle' object is not iterable 
    # i think this means in terms of gathering the entire quote and i think this only work for a single element 
'''

