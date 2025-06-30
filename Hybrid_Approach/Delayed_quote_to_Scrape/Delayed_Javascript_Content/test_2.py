r'''
Progression Path for Learning the Delayed Content of Javascript 

🎯 1. MASTER EXPLICIT WAITING (Core Skill)
✅ 2. VERIFICATION CHECKS (Add Gradually)
🔁 3-4. RETRY MECHANISMS (Essential Safety Net)
🛠️ 5. JUST-ENOUGH VERIFICATION (Smart Checks)
'''

# 🎯 To Do List 
# 1. MASTER EXPLICIT WAITING (Core Skill)

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin

from playwright.sync_api import expect
r'''
This code is supposed to be a synchronous version as opposed to async version 
but basically this line of code is to verify wether the elements exist 
'''


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

r'''
🔁 3-4. RETRY MECHANISMS (Essential Safety Net)

from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), 
       wait=wait_exponential(multiplier=1, min=2, max=10))
def safe_click(selector):
    page.wait_for_selector(selector, state="visible")
    page.click(selector)

# Usage example:
safe_click("button.submit")

Progression Exercises:
    Wrap your most common failure points
    Add basic logging to retries:

@retry(...)
def safe_action():
    try:
        # action
    except Exception as e:
        print(f"Attempt failed: {str(e)}")
        raise

'''

r'''
🛠️ 5. JUST-ENOUGH VERIFICATION (Smart Checks)

def verify_critical_elements():
    """Check only the most important indicators"""
    critical_selectors = {
        ".main-content": "visible",  # Key container
        "[data-loaded='true']": "attached",  # Data attribute
        "text='Loading'": "hidden"  # Loading spinner gone
    }
    
    for selector, state in critical_selectors.items():
        if state == "count":
            assert page.locator(selector).count() > 0
        else:
            page.wait_for_selector(selector, state=state)
'''


r'''
🛠️ Analyzing my Python Skills
    1. try and except (Error Handling)
        try lets you test a block of code for errors
        except handles those errors if they occur
    Note: Using Different web scrapping libraries like scrapy, playwright and request have their own 
    set of exception and error handling thing 
    Practical: 
        1. Learn the basics of Try and Except Error handling in Phone
        2. Learn the Common Types of errors in Web Scrapping 
        3. Figure out the Across of LibrariesWhat is 20/80 Rule for Error handling thing 
        4. In Each Libraries like Playwright, Scrapy, Request and BS4 research what is 20/80 Errors that occurs
    General Best Practices for Error Handling in Web Scraping:
        1. Always use timeouts (Prevent indefinite hanging).
        2. Retry mechanisms (Use tenacity or backoff for transient errors).
        3. Log errors properly (Helps in debugging).
        4. Handle anti-bot measures (Rotate user agents, use proxies).
        5. Check HTTP status codes (Avoid parsing invalid responses).
        6. Use finally or context managers (Clean up resources like browser

    2. Classes (Object-Oriented Programming)
        Definitions: Blueprint for creating the methods (Function of the Code) and creating objects with properties

        Practical: 
            A. Learn the basics Stuff
            B. Build Out of Something from the Basic Stuff 
            C. Learn the Blueprint or classes for Scrapy Stuff 
    3. Context Managers  (using __enter__ and __exit__) 
        Definitions: a way to manage the resources efficiently so it is properly "initialized and cleaned up"
        Common used for 
            1. File handling 
            2. Database Connections
            3. Browser Automations like Playwright
            4. Netwrok Sessions like Scrapy Resources
            5. Lock and Thread Management # I had no Idea what this means

    4. main() and if __name__ == "__main__":
        Definitions: Make script import-safe
    5. Combining the Concepts Gradually is Important Things to Learned man 

'''
