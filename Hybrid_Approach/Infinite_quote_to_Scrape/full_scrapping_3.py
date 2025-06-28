# python full_scrapping_3.py
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time

# I understand a bit of Function i'm worried about it lol 
def extract_quote(page):
    quotes = page.locator(".quote .text").all()
    quote_count = 0 
    for quote in quotes: 
        print(quote.text_content())
        quote_count += 1
        print(f"Quote Count: {quote_count}")
        print()

# Focusing on Mouse Movement to Look like a Human so Basically the Behaviour of the Bot
# # 2. Scroll to bottom in increments
# for _ in range(5):
#     page.mouse.wheel(0, 1000)
#     page.wait_for_timeout(1000)  # Wait for content to load

# # 3. Scroll specific element into view
# element = page.query_selector('.target')
# box = element.bounding_box()
# page.mouse.wheel(0, box['y'] - 200)  # Scroll to position above element

# # 4. Horizontal scrolling (for rare cases)
# page.mouse.wheel(300, 0)  # Scroll right 300px

r'''

import random
import time
from math import sin


Human Behaviour for a Bot:
    "click": (0.2, 0.8),
    "navigate": (1.5, 3.0),
    "scroll": (0.1, 0.5),
    "think": (2.0, 5.0)


# Vary scroll speed with sinusoidal pattern

Learning the Dictionary in Python 
base_times = {
    "click": (0.2, 0.8),
    "navigate": (1.5, 3.0),
    "scroll": (0.1, 0.5),
    "think": (2.0, 5.0)
}






'''


def human_bot(page):
    base_times = {
    "click": (0.2, 0.8),
    "navigate": (1.5, 3.0),
    "scroll": (0.1, 0.5),
    "think": (2.0, 5.0)
}
    
    
def human_bot(page):
    base_times = {
        "click": (0.2, 0.8),    # Random delay between 200ms-800ms
        "navigate": (1.5, 3.0),  # Wait 1.5-3s after navigation
        "scroll": (0.1, 0.5),    # Short delay after scrolling
        "think": (2.0, 5.0)      # Pause between actions (2-5s)
    }

def random_delay(action,base_times): # action (str): A key from the base_times dictionary (e.g., "click", "navigate", etc.).
    min_time, max_time = base_times[action]
    r'''
    Explanation of the code "min_time, max_time = base_times[action]"
    # Looks up the action in the base_times dictionary.
    # Retrieves the (min_time, max_time) tuple associated with that action.
    '''

    delay = random.uniform(min_time, max_time)
    r'''
    Looks up the action in the base_times dictionary.
    Retrieves the (min_time, max_time) tuple associated with that action.
    '''
    time.sleep(delay)

# Working with different set of Function in Python Connecting things in there


def mouse_movement_human(page):
    page.mouse.wheel(0, 500)
    page.wait_for_timeout(3000)
    # Implementing Burst Scrolling 
    # Implement 
    # Timing is Crucial:
    # Use different delay profiles for different actions
    # Implement acceleration/deceleration in scrolling
    # Add random micro-variations (±10%) to all timings
    # Include "thinking time" before critical actions  


def mouse_click(page):

    # page.click("button#submit") 
    # Example of HTML for this is <button id="submit">Click Me</button>
    
    # Click using a CSS selector
    # page.locator("button.submit-btn").click()
    # HTML: <button class="submit-btn">Submit Form</button>

    # Click using text content
    # page.locator("text='Log In'").click()

    # Click using XPath
    # page.locator("//button[contains(@class, 'primary')]").click()

    # Clicking Coordinates
    # page.mouse.click(x=100, y=200)

    # Double Click 
    # page.locator("button").dblclick()

    # Definitely Working in Things 
    # page.locator("text='Login'").click(delay=random.randint(100, 300))

    # page.mouse.move(x, y, steps=20)  # Gradual movement (steps = smoother curve)
    # page.mouse.click(x, y)

    # Adding the Random Delay of things  
    # page.locator("button").click(delay=random.randint(100, 300))

    r'''
    <div class="col-md-4">
                <p>
                
                    <a href="/login">Login</a>
                
                </p>
            </div>
    '''

# Simulate Navigation Delays
# After page loads or link clicks, pause like a human reading

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    page.wait_for_selector(".quote", state="attached")
    mouse_click(page)

    
    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    # mouse_movement_human(page)
    # page.wait_for_timeout(5000)  
    # extract_quote(page)

    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



r'''
Concept: Websites use behavioral analysis to detect bots (e.g., checking if interactions are too fast/consistent

This function helps bypass such detection by:
    Varying delays between actions.
    Matching human response times.

Key Points
Avoids Detection:
    Bots often use fixed timings (e.g., time.sleep(1)), which are easy to flag.
    Randomization makes the script behave more like a human.

Flexible for Different Actions:
    Delays are tailored to specific actions (e.g., shorter for clicks, longer for "thinking").

Natural User Behavior:
    Humans don’t interact with perfect timing. Random delays add 
'''

r'''
My Thinking i needed to simulate the human behaviour based on the things that it said and there are 4 categories 
    1. Clicking clicking on the random stuff (Careful on clicking the Random stuff)
    2. Navigating (User need to think after the page loaded like 1 - 3 seconds after it loads)
    3. Scrolling i needed to scroll which is the MAIN PURPOSE of this but it needed to look like a humans 
        First is i needed to scroll like a burst and go up again after scrolling 
        second up and down thing scrolling 
    4. Thinking i need a bot where it can think sometimes so yeah that is a thing in there 

Problem is executing things because i know the block of code how it works but the logical building up to that code is really something man 
'''