# Problem JS delayed simply delay the website in fixed time before it load (Delayed also in terms of pagination )

# Implementation Ladder 
r'''
Rough Overview 
🎯 1. MASTER EXPLICIT WAITING (Core Skill)
✅ 2. VERIFICATION CHECKS (Add Gradually)
🔁 3-4. RETRY MECHANISMS (Essential Safety Net)
🛠️ 5. JUST-ENOUGH VERIFICATION (Smart Checks)

Ladder Part 🚀 The Vital 20% - Playwright's Power Features


3. Expect Assertions (Smart Waiting) - Your Core Skill
from playwright.sync_api import expect

# Wait for visibility
expect(page.locator("#results")).to_be_visible()

# Wait for text content
expect(page.locator(".status")).to_have_text("Completed")

# Wait for element count
expect(page.locator(".items")).to_have_count(15)

# Wait for disappearance
expect(page.locator("#loader")).to_be_hidden()

5. Navigation (Page Control)
# Basic navigation
page.goto("https://example.com")

# Wait for navigation after click
with page.expect_navigation():
    page.locator("a.next-page").click()

# Reload
page.reload()
'''

# From these 2 I quite notice the Difference from the Old vs to New Thing 
# from playwright.sync_api import sync_playwright, Playwright
# from playwright.sync_api import sync_playwright, expect

# 🔍 Key Differences
r'''
sync_playwright vs Playwright
    sync_playwright: The context manager for launching browsers (required)
    Playwright: The main class (rarely needed directly in scripts)

expect
    The assertion library for smart waiting/verification

# BEST PRACTICE (all essentials in one line)
from playwright.sync_api import sync_playwright, expect, Playwright

1. Minimum Viable Imports
    sync_playwright: Required to launch browsers
    expect: Needed for all smart waiting/assertion
2. What You're NOT Importing
    Playwright class (only needed for advanced configuration)
    Redundant imports that clutter your namespace
3. When You Might Need Playwright Class
    Direct access to Playwright API
    Custom browser server configuration
    Very advanced use cases

'''

# Problem in Using only tthe "from playwright.sync_api import sync_playwright, expect"


from playwright.sync_api import sync_playwright, expect, Playwright
from urllib.parse import urljoin
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js-delayed/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=True) 
    page = browser.new_page()
    page.goto(base_url)

    # for x in range(1,5):
    #     # Printing out the Current URL that we are going to Scrape 
    #     current_url = page.url
    #     print()
    #     print(f"Currently Scrapping {current_url}")
  

    #     # Going to the Next Page Part 
    #     next_page = page.locator('.next a')
    #     next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
    #     page.goto(next_page_url)
    #     print()
    #     print(f"Going to the Next Page {next_page_url}")
    
    # page.wait_for_selector(".quote", state="attached")  # DOM existence
    # expect(page.locator(".quote .text")).to_be_visible()
    
    quotes_text = page.locator(".quote .text").all()
    for quote in quotes_text:
        print(quote.text_content())
    r'''
    It's Funny that i study more in "expect" but it didn't even run LOL 

    # This Works
    page.wait_for_selector(".quote", state="attached")  # DOM existence

    # This Doesn't Work Alone 
    page.goto("https://quotes.toscrape.com/js-delayed/", wait_until="networkidle")

    # This Work
    page.wait_for_selector(".quote .text") # or page.wait_for_selector(".target-element", state="visible") for Visibility check (rendered & not hidden)
    
    # This give me Error 
    expect(page.locator(".quote .text")).to_be_visible()
    '''

    page.close() 
    browser.close()



with sync_playwright() as playwright:
    run(playwright)


# Concepts:

# expect
r'''
How expect() Works:
    Starts waiting from the moment it's called
    Doesn't know about future JavaScript injections
    Default 5s timeout may be too short for delayed content

wait_until="networkidle" ensures JavaScript execute
expect() then handles dynamic element appearanc

'''


r'''
You've hit on a crucial insight! This perfectly illustrates the nuances of dynamic content handling. Let me clarify why this happens and how to think about it:

🤯 The "Expect Paradox" Explained
expect() can handle dynamic elements, but only after they exist in the DOM. Your JS-delayed site creates a special case:


# This works because it waits for EXISTENCE
page.wait_for_selector(".quote", state="attached")

# This fails because it's trying to verify VISIBILITY of non-existent elements
expect(page.locator(".quote .text")).to_be_visible()

🧠 Mental Model: The Two Stages of Element Lifecycle
    Existence (attached to DOM)
        Handled by: page.wait_for_selector(..., state="attached")
        Required before any visibility checks

Visibility (rendered, not hidden)
    Handled by: expect(...).to_be_visible()

Why Your Specific Site Breaks Expectations
The quotes.toscrape.com/js-delayed site:
    Loads an empty container first
    Later injects .quote .text elements via JavaScript
    There's a gap where .text elements don't exist at all

expect() fails because it:
Starts checking immediately for visibility

But the elements don't even exist yet at check time
    Errors immediately with "element(s) not found"

The Complete Solution
python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # 1. Load page (networkidle helps but isn't enough)
    page.goto("https://quotes.toscrape.com/js-delayed/", wait_until="networkidle")
    
    # 2. FIRST ensure PARENT container exists (crucial!)
    page.wait_for_selector(".quote", state="attached", timeout=15000)
    
    # 3. THEN wait for child VISIBILITY
    expect(page.locator(".quote .text")).to_be_visible()
    
    # 4. Now safely extract
    quotes = page.locator(".quote .text").all()
    for quote in quotes:
        print(quote.text_content())
    
    browser.close()

Why Your Second Approach Worked
python
page.wait_for_selector(".quote .text")  # This waits for EXISTENCE first
This works because:

It handles the existence stage
    By default, wait_for_selector checks for visibility after existence
    It's essentially doing two operations in one call

💡 Key Takeaways
    Existence before visibility: Always ensure elements exist before visibility checks
    Parent-first strategy: Wait for containers before children
Combined tools are best:
    Use wait_for_selector for existence guarantees
    Use expect for visibility/state assertions

When to use what:

python
# For elements that MIGHT exist but aren't visible yet
expect(locator).to_be_visible()

# For elements that DON'T EXIST YET
page.wait_for_selector(selector)
This isn't a flaw in expect() - it's about understanding the different phases of dynamic content loading. The most robust scrapers combine both approaches strategically!
'''



#🎯 Concepts Understanding Explicit Waiting and expect 

# What is Playwright already have?
r'''
Playwright have a built-in-Autowaiting mechanism to handle complex synchronization scenario 
'''
# What does it mean to master explicit waiting?
r'''
It is Overriding the built-in-autowaiting mechanism in playwright 
'''
# What is the Core Concepts of Explicit Waiting?
r'''
It is to control the flow by pausing execution until the condition are met 
like Elements, Visibility, Netwrok Stability 
'''
# What is the Difference between Autowaiting and Explicit Waiting?
r'''
Autowaiting handle the basic readiness like e.g., element visibility, stability) before interactions

Explicit waiting: Manually defines advanced conditions (e.g., networkidle, text content changes)
'''

# What does it mean by Assertions as Explicit Waits?
r'''
In Playwright, assertions (like expect(locator).to_have_text()) are explicit waits because they:
    Automatically retry until the condition is met (e.g., element appears/text changes) or timeout expires.
    Replace manual wait_for_* calls in most cases, making code cleaner.

    Code:
    # Assertion waits EXPLICITLY for text to appear (retries every 100ms by default)  
    expect(page.locator("#status")).to_have_text("Data loaded!")  # This IS an explicit wait  
'''

# What are Conditions for Explicit Waiting & Common Use in Web Scraping
r'''
Method/Condition	                            Use Case
page.wait_for_selector(selector)	            Wait for element to exist in DOM
page.wait_for_function("js_code")	            Wait for custom JS condition (e.g., window.dataReady)
page.wait_for_load_state("networkidle")	        Wait for all network calls to finish (critical for SPAs)
locator.wait_for()	                            Wait for element to be actionable (visible, stable, etc.)
'''

# What expect means?
r'''
expect is Playwright's assertion library (from playwright.sync_api import expect).
    Retrying checks until the condition passes (e.g., element becomes visible).
    Failing only after the timeout (default: 5 seconds).

Not just for tests: Useful in scraping to ensure page state before extraction.
'''
# When to use Which (Explicit Waiting and expect)? 
r'''
Use Explicit Waiting to pause until a resource/element is available
Use expect to validate assumptions before proceeding:
'''
# The Workflow should  be 
r'''
    # 1. Navigate & wait for network stability  
    page.goto("https://quotes-to-scrape.com")  
    page.wait_for_load_state("networkidle")  

    # 2. Explicitly wait for content container  
    page.wait_for_selector(".quotes")  

    # 3. Validate presence of critical elements  
    expect(page.locator("h1")).to_contain_text("Quotes")  

    # 4. Extract data  
    quotes = page.locator(".quote").all()  
    for quote in quotes:  
        text = quote.locator(".text").inner_text()  
        print(text)  

'''


