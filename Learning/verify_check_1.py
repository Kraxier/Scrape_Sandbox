# Verify Checking 
# python verify_check_1.py
r'''
✅ 2. VERIFICATION CHECKS (Add Gradually)

# Presence (Is the element in DOM?)
assert page.locator(".target").count() > 0

Visibility (Can users see it?)
assert page.locator(".target").first.is_visible()

Content (Has real data loaded?)
assert "Expected Text" in page.locator(".target").first.text_content()

Count (Are all items loaded?)
assert page.locator(".items").count() == expected_count

'''


from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
from playwright.sync_api import expect
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js-delayed/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    while True: 
        # Find the next_page thing in targeting the elements 
        next_page = page.locator('.next a')
        quotes_locator = page.locator(".quote")
        assert await items.count() > 0
        for i in range(await items.count()):
            assert await items.nth(i).is_visible()
        # Wait for the element to pop up in the DOM PART 
        quotes_locator.first.wait_for()
        # Based on deepseek it should combine to wait_for()

        # storing the elements in "quotes"
        quotes = quotes_locator.all()  

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


r'''
Combining Verify Checking and Explicit Waiting 
📊 When to Use expect() in Scraping
Scenario	Recommended Approach
Debugging	Temporary expect() to verify selectors
Prototyping	Quick validation during development
Production	Custom logic with precise timeout control

'''

