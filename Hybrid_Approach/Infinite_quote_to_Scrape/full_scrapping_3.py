# python full_scrapping_3.py
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random


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


def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    page.wait_for_selector(".quote", state="attached")

    
    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    mouse_movement_human(page)
    # page.wait_for_timeout(5000)  
    # extract_quote(page)


    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

