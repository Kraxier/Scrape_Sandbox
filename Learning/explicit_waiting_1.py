# 🎯 1. MASTER EXPLICIT WAITING (Core Skill)
# python explicit_waiting_1.py
# Skills for MASTER EXPLICIT WAITING 
# Implementing Part of things 
# venv_PS_Toscrape\Scripts\activate


from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
from playwright.sync_api import expect
def run(playwright: Playwright):
    # base_url = "https://quotes.toscrape.com/js-delayed/"
    base_url = "https://quotes.toscrape.com/js-delayed/page/9/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    while True: 
        next_page = page.locator('.next a')
        # quotes = page.locator(".quote .text").all()
        # AttributeError: 'ElementHandle' object has no attribute 'all'
        # quotes = page.wait_for_selector(".quote .text").all()
        r'''
        Error is wait_for_selector is only for single element
        The problem on that is i need at least 10 Elements in delayed thing 

        Why Use first.wait_for()?
        
        '''
        
        # This Work Perfectly Fine and It Scrape Everything in a page 

        quotes_locator = page.locator(".quote")
        quotes_locator.first.wait_for()  
        quotes = quotes_locator.all()  
        r'''
        Reason it worked
        page.locator(".quote") → Finds all .quote elements (but doesn’t wait).
        .first.wait_for() → Explicitly waits for the first quote to exist/be visible.
        .all() → After waiting, safely extracts all quotes (since we know the page is ready).

        Considering the Challenge off 
        Content loads unevenly (some elements appear faster than others).
        Lazy-loading/AJAX fetches data in chunks (e.g., infinite scroll).
        Dynamic pages render elements at different times.
        '''

        # Other Code 

        # Wait for a Minimum Count of Elements
        r'''
        page.wait_for_function(
    """(selector, minCount) => {
        return document.querySelectorAll(selector).length >= minCount;
    }""",
    args=[".quote", 5]  # Wait for at least 5 quotes
)
        quotes = page.locator(".quote").all()
        '''

        # Hybrid Approach Checking if everything is loaded 
        # Wait for at least 1 element (to confirm JS executed)
        # page.locator(".quote").first.wait_for()

        # # Then wait for count to stabilize
        # prev_count = 0
        # while True:
        #     quotes = page.locator(".quote").all()
        #     if len(quotes) == prev_count:
        #         break  # No new elements detected
        #     prev_count = len(quotes)
        #     page.wait_for_timeout(1000)  # Wait 1s between checks

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

# Concepts:
r'''
🎯 1. MASTER EXPLICIT WAITING (Core Skill)
# Train with these patterns (in order of complexity):
from playwright.sync_api import expect

# 1. Basic presence
page.wait_for_selector(".target-element")


# Wait for the elements to appear in the DOM part 
# Use Case is when you need to confirm if the elemenet are loaded 

# 2. Visibility check (rendered & not hidden)
page.wait_for_selector(".target-element", state="visible")

# Wait for the element to load in the DOM and "visibly rendered" or not hidden
# Testing interactive elements that must be visible to user 

# 3. Content verification
page.wait_for_selector("text='Specific Text'")

# Waiting for element that contain text that are specific in the DOM 
Use case is for Dynamic Content

# 4. Combined check (Modern Playwright)
expect(page.locator(".quote")).to_be_visible()

# A Modern approach to verify if elements are visible and it have an own retry mechanism


# 5. Quantity verification
expect(page.locator(".quote")).to_have_count(10)

# Basically to count at things if there are 10 matching elements 
# Use case is when you know the exact thing in there 


# 6. Custom logic waiting
page.wait_for_function("""
  () => {
    const el = document.querySelector('.price');
    return el && parseFloat(el.textContent) > 100;
  }
""")
'''

r'''
What is expect? 
* Part of Modern testing for API 
* What is Assertion Library?
* Writing Clean and reliable test assertion in web Automations 
* It Automatically Wait and retries for conditions to be met 
* Desined to work with locator objects 

What are Key Features? 
1. Autowaiting unlike the traditional assertions # What is the Traditional Assertions
2. Supports validations and readable syntax for things 

Using the "expect" is for testing purpose (get hype by deepseek) only and not for web scrapping 

Useful tools for Web Scrapping 
1. page.wait_for_selector()

# Wait for a price element to load, then extract text
await page.wait_for_selector(".price")
price = await page.text_content(".price")

2. page.locator() + .text_content() / .get_attribute()

3. page.evaluate()
Use Case: Extract complex data (e.g., JSON from <script> tags).
'''

r'''

print()
i ask a question of what is the content inside the parentheses

In Programming general are called aurguments or parameters of a function and method 
basically that line of code is what are things that can do 

____________________________________________________________________
page.wait_for_selector()
- Purpose: Wait for an element to meet conditions (exists/visible/hidden).

examples:
    # CSS selector
    await page.wait_for_selector(".product-list")

    # Text selector
    await page.wait_for_selector("text='Loading...'")

    # XPath (rarely needed)
    await page.wait_for_selector("//div[@class='price']")

    # Wait for element to be hidden
    await page.wait_for_selector(".loading-spinner", state="hidden")
    # Short timeout (fail fast)
    await page.wait_for_selector(".error", timeout=2000)

____________________________________________________________________
page.locator() 
Purpose is to extract 

    # CSS selector
    button = page.locator("button.primary")

    # Text selector
    title = page.locator("text='Welcome'")

    # XPath (use sparingly)
    price = page.locator("//span[@class='price']")
page.evaluate()
Purpose: Run JavaScript in the page context to extract complex data.

'''

r'''
Handling Challenges if things don't go as planned if the elements is variability 

Key Takeaways
1. first.wait_for() is sufficient for 90% of cases because:
    Pages typically load elements sequentially.
    Playwright’s .all() captures current state (not just the state at wait_for()).

2. For edge cases (async/lazy-loaded content):
    Use wait_for_function() to enforce a minimum count.
    Implement polling logic if elements trickle in unpredictably.

3. Never assume all elements load simultaneously—design your scraper to handle variability.

'''


r'''
Succesfuly Scrape the Dynamic Content 

Dynamic Content Definition Based on Web Scrapping 
The page are still loading after the inital load 

Due to Javascript Executions: 
    A stock price updates in real-time via WebSocket/AJAX.
User Interactions Trigger Changes
    Clicking, scrolling, or typing may load new content.
    Infinite scroll (like Twitter or Facebook).
    A modal popup appearing after a button click.
Data Fetched from APIs
    Many modern websites (React, Angular, Vue apps) load a skeleton HTML first, then fill data via API calls.
    Example:
    An e-commerce product list loaded via fetch() after page load

'''