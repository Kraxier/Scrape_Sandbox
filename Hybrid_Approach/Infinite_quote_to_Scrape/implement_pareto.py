from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin

# https://chat.deepseek.com/a/chat/s/ab708a64-1d11-44f8-b994-d7bec84c2baf
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)

    # Wait for page to load completely
    page.wait_for_selector(".quote", state="attached")
    r'''
    I'm Going to Try to Explain the Code Properly in terms of line by line
    1. wait_for_selector() - The Core Method
        * playwright will wait until a specific element appear in page 
        * Essential modern website load content dynamically elements don't appear or always arent available 
        * Alternative for time.sleep() because timesleep is precisely 

    2.".quote" - The CSS Selector Parameter
        * Just a Selector for targeting things 
    
    3. state="attached" - The Waiting Condition
        * Specify the state that the element we want before continuing the program
        * State and meaning and when to use":
            "attached": Element exist within the DOM : Basic waiting for element existence
            "detached": Element is NOT in the DOM : Waiting for something to disappear
            "visible": Element is visible on page: When you need to interact with visible elements
            "hidden": 	Element exists but isn't visible: Waiting for elements to hide
    Common Mistake:
        Missing the wait: Trying to interact with elements before they exist
        Overusing "visible": Slower than "attached" when visibility isn't needed
        Not handling failures: These waits can timeout if elements never appear
    '''

    initial_position = page.evaluate("window.scrollY")
    print(f"Initial scroll position: {initial_position}") # Verification of the program


    page.close() 
    browser.close()

with sync_playwright() as playwright:
    run(playwright)