
r'''

Defining What i needed tp do because there are state checking 


1. Data Extraction 
    Getting the elements Safety
    Content Retrieval 
    State Checking 
    Basic CSS/XPath selectors
    Extracting text (page.textContent(), page.$$eval())

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

3. State Checking (Explained)
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
    chromium = playwright.chromium
 
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

# To do for Tomorrow 
r'''
Critical Improvements Needed:
1. Missing Auto-Waiting for Dynamic Content
Problem: The site uses JavaScript rendering (/js/ path), but your code doesn't wait for elements to load.
Solution: Add wait_for_selector after navigation:

python
page.goto(current_url)
page.wait_for_selector('.quote')  # Wait for quotes container
2. Incorrect Text Extraction Method
Problem: Uses text_content() which gets hidden text (not needed here).
Solution: Use inner_text() for visible text:

python
print(quote.inner_text())  # Gets only visible text
3. Fragile Pagination Check
Problem: next_page.count() might fail if page loads slowly.
Solution: Use state checking with timeout:

python
if next_page.is_visible(timeout=3000):
4. No Error Handling
Problem: Network failures or missing elements crash the script.
Solution: Add try/except blocks.
'''

# The Code he said 
r'''
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import time

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        current_url = base_url
        
        while True:
            # Navigate with auto-wait
            page.goto(current_url, wait_until="domcontentloaded")
            
            # Wait for dynamic content
            page.wait_for_selector('.quote', state="visible", timeout=10000)
            
            # Extract quotes (visible text only)
            quotes = page.locator(".quote .text").all()
            for quote in quotes:
                print(quote.inner_text().strip())
                print()
            
            # Robust pagination check
            next_page = page.locator('.next a')
            if not next_page.is_visible(timeout=3000):
                print("Reached last page. Stopping.")
                break
                
            # Get next URL
            next_url = urljoin(
                current_url, 
                next_page.get_attribute('href')
            )
            print(f"Navigating to: {next_url}")
            current_url = next_url
            
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        page.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
'''


# Concepts

# 1. "Getting the Elements Safely"
r'''
This refers to robust element selection that accounts for dynamic web content and prevents flaky tests. Playwright handles these automatically:

Auto-Waiting: Playwright waits for elements to be:
    Attached to the DOM
    Visible (not hidden by CSS)
    Stable (no animations)
    Enabled (interactable)
    Ready for action (e.g., receiving events)
Without safety: Directly interacting with elements could cause errors if they're not ready.
'''
# 2 Hidden vs. Visible Text
# Practice this with a website that have this because i doubt that 
# IDENTIFY THE js quote to Scrape if it is have Hidden Text 

r'''
Html example 
<div style="display:none">Secret Text</div>
<div>Hello <span style="visibility:hidden">World</span></div>
'''

# 3. Relevance of State Checking
r'''
State checking ensures elements are interactable before actions. Critical for:
    Reliable tests: Avoid errors from interacting with disabled/hidden elements.
    Accurate validation: Verify UI state (e.g., is a checkbox checked?).
    Performance: Reduces unnecessary waits with explicit checks.
'''


# 80/20 Rules
r'''
1. Element Selection (90% of Scraping Success)
    # CSS (80% of use cases)
    elements = page.locator(".product-card")  # Classes
    title = page.locator("#title")            # IDs

    # XPath (20% special cases)
    price = page.locator("//span[contains(@class, 'price')]")  # Partial matches
    out_of_stock = page.locator("//div[text()='Sold out']")     # Text search

2. Text Extraction (Core Data Capture)
    # Visible text (95% of scraping needs)
    product_name = product.locator(".name").inner_text()

    # All text (special cases only)
    hidden_data = product.locator(".metadata").text_content()

3. Attribute Extraction (Structured Data)
    # Essential for links/media
    product_url = product.get_attribute("href")
    image_src = product.get_attribute("data-src")

    # Extracting data attributes
    product_id = product.get_attribute("data-product-id")

4. Auto-Waiting (The Silent Hero)
    Why it's 20% magic: Eliminates 80% of timing issues without explicit code
    # Playwright handles these automatically:
    element.click()          # Waits for clickability
    element.fill("text")     # Waits for editability
    element.inner_text()     # Waits for visibility

5. State Checks (Avoiding Errors)
    # Only 2 checks cover most cases:
    if page.locator(".cookie-banner").is_visible():
        page.locator("#accept-cookies").click()
        
    if not page.locator(".loading-spinner").is_hidden():
        page.wait_for_selector(".results-loaded")
'''

