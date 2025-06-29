
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
    browser = chromium.launch(headless=True) 
    page = browser.new_page()
    page.goto(base_url)



    # current_url = page.url # Get the Current URL of the Page itself
    # print(f"Printing the Current URL:{current_url}") 
    # print()

    # quotes = page.locator(".quote .text").all() 
    # print(quotes)
    # print()
    r'''
    Output: 
    [<Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=0'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=1'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=2'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=3'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=4'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=5'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=6'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=7'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=8'>, 
    <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.quote .text >> nth=9'>]
    '''
    # x = page.wait_for_selector('.quote')
    # print(x)
    # r'''
    # Output: JSHandle@node
    # '''
    # page.wait_for_selector('.quote') # Basically i want to Wait if the quote appear
    # quotes_text = page.locator(".quote .text").all()
    # for quote in quotes_text:
    #     print(quote.text_content())
    # print()


    # Getting the Next Page 
    # next_page = page.locator('.next a')
    # print(f"Print the Next Button HTML:{next_page}")
    # print()
    r'''
    Output : <Locator frame=<Frame name= url='https://quotes.toscrape.com/js/'> selector='.next a'>
    '''

    # Getting the Next Page Attribute 
    # next_page_url = page.locator('.next a').get_attribute('href')
    # print(f"Print the Next Button HTML Attribute itself: {next_page_url}")
    # r'''
    # Output : /js/page/2/ 
    # '''
    # print()

    # next_page = page.locator('.next a')
    # next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
    # page.goto(next_page_url)
    # current_url = page.url # Get the Current URL of the Page itself
    # print(f"Printing the Current URL:{current_url}") 


    while True:
        current_url = page.url # Get the Current URL of the Page itself
        print(f"Printing the Current URL:{current_url}") 
        print()
        page.wait_for_selector('.quote') # Basically i want to Wait if the quote appear
        r'''
        ✅ Why use page.wait_for_selector('.quote')?
            Because JavaScript-rendered content (like quotes loaded dynamically) might not appear immediately when you visit a page. If you try to scrape elements before they load, your code will either:
            Throw an error (e.g., element not found), or
            Return None or empty data.
        '''

        quotes_text = page.locator(".quote .text").all()
        for quote in quotes_text:
            print(quote.text_content())
        print()
        
        
        
        next_page = page.locator('.next a')
 
        r'''
        page.locator('.next a') always returns a Locator object, even if nothing is matched.

        if next_page == None:
            break
        So next_page == None is always False, even when no element exists.

        Then next_page.get_attribute('href') fails because there is no actual matching DOM node.

        '''
        next_page_hidden = not page.locator(".next a").is_hidden()
        next_page_visibility  = page.locator(".next a").is_visible()
        print(next_page_hidden)
        print(next_page_visibility)
        '''
        Output: 
            True
            True 
            # Both are True until the Next they have a next page 
            After Reaching the Last Page it return 
            False
            False 

            locator.is_visible()
            Returns True if the element exists in the DOM and is visible (i.e., not display: none, not opacity: 0, and not offscreen).

            locator.is_hidden()
            Returns True if the element is not visible or doesn't exist.

            ✅ Best Practice for Pagination Check 
            next_button = page.locator(".next a")
            if not next_button.is_visible():
                break

            href = next_button.get_attribute("href")
            page.goto(urljoin(base_url, href))

        '''



        if next_page.count() == 0:
            break
        r'''
        🔢 What does .count() mean in Playwright?

        next_page = page.locator('.next a') # next_page is a Locator object, which can point to zero or more elements.
        🧠 What .count() does: 
            0 → No matching element found (like if there’s no “Next” link).
            1 or more → At least one match found.

        '''
        next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
        page.goto(next_page_url)


    page.close() 
    browser.close()

    

with sync_playwright() as playwright:
    run(playwright)


# Learning the Loops
# In terms of Web Scrapping assuming i don't know how much page are needed so i'm going to focus at while loop 
# because While Loop is Good For Uncertainty 
# For Loops if you already know how much to begin with 

# while True:
#     if condition:
#         break


# Conclusion inner_text() vs text_content()
r'''
Try First the text_content if it is cleaned go for it 
But if it is not cleaned data go to inner_text() and look for the Challenge there
'''

# ✅ inner_text()
r'''
Returned the Text what i can currently see in the browser 
'''
# ✅ text_content()
r'''
Returns: the raw text inside the element, regardless of visibility or layout. and Includes: hidden text, and preserves all whitespace and newlines as in the HTML source
Faster: Doesn't wait for rendering or visibility.
'''

# ✅ inner_text() ✔️ Advantages (for web scraping)
r'''
1. Clean output: Gives you only the visible, user-facing text, which is usually what scrapers want.
2. Whitespace is normalized: Easier to work with programmatically.
3. Ignores hidden elements: Avoids accidental capture of unwanted or misleading data (like hidden SEO text or JavaScript-generated labels).
4. Ideal for user-facing content: Great when scraping articles, reviews, or product descriptions.
'''
# ✅ inner_text() ❌ Disadvantages
r'''
1. Slower: It waits for the page to fully render and the element to become visible.
2. Might miss data: If important content is hidden (e.g. behind tabs, accordions, or for screen readers), it won’t be included.
3. JavaScript dependency: Requires the browser to fully execute scripts — if rendering fails, text may be missing.
'''

# ✅ text_content() ✔️ Advantages (for web scraping)
r'''
1. Faster: Does not wait for visibility/rendering — great for large-scale scraping where speed matters.
2. Full HTML text: Useful for capturing all content, including hidden text, comments, or dynamic placeholders.
3. Better for debugging: You can see everything the DOM contains.
'''
# ✅ text_content() ❌ Disadvantages
r'''
1. Includes hidden text: Might capture text that’s not actually shown to users, which can pollute your data.
2. Messier output: Whitespace, line breaks, and formatting can be inconsistent or excessive.
3. More cleanup needed: Often needs post-processing or regex to get usable results.
'''
# ✅ Rule of Thumb
r'''
1. Use inner_text() when you're scraping visible user content like articles, 
headlines, reviews, or prices.

2. Use text_content() when you're scraping for raw or technical data, 
or you want to capture everything including hidden fields (e.g., for analysis or reverse engineering).
'''


# To do for Tomorrow 
r'''

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

