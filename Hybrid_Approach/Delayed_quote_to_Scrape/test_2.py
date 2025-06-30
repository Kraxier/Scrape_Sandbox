# Problem JS delayed simply delay the website in fixed time before it load (Delayed also in terms of pagination )

# Implementation Ladder 
r'''
Rough Overview 
🎯 1. MASTER EXPLICIT WAITING (Core Skill)
✅ 2. VERIFICATION CHECKS (Add Gradually)
🔁 3-4. RETRY MECHANISMS (Essential Safety Net)
🛠️ 5. JUST-ENOUGH VERIFICATION (Smart Checks)

Ladder Part 🚀 The Vital 20% - Playwright's Power Features

1. Locators (Find Elements) - 80% of scraping starts here
# CSS selector (most common)
element = page.locator("css=.class-name")

# Text-based (great for buttons/links)
button = page.locator("text='Submit'")

# Combined
row = page.locator("tr:has-text('Item 5')")

2. Actions (Element Interactions)
# Click
page.locator("button#submit").click()

# Type text
page.locator("input#search").fill("playwright")

# Select dropdown
page.locator("select#country").select_option("US")

# Check checkbox
page.locator("input.agree").check()

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