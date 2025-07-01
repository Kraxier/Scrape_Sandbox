from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import time


def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=True) 
    page = browser.new_page()
    page.goto(base_url)

    page.wait_for_selector(".quote", state="attached") # Wait the Page to Load 
    quote_initial_count = len(page.query_selector_all(".quote")) # Counting the Quotes



    # page.mouse.wheel() Implementing this for Human Behaviour Using the test_2.py for some Guidance 
    r'''
    What is my Goal in implementing "page.mouse.wheel() :: human traits: randomness, pauses, backtracking, and varied speeds
    Variable scroll amounts: Humans scroll in unpredictable bursts.
    Pauses/delays: Reading time between scrolls
    Backtracking: Occasionally scroll up to recheck content.
    Speed variations: Slow/fast scrolls based on context.

    Implementation from this New Found Knowledge in Python:
        Unpredictable scroll bursts: Math.floor(Math.random() * 20 + 5)
        Re-reading content: 10% chance of negative step
        Stopping to view content : 10% chance of 1-3s extraPause
        Slow/fast scrolling moods : Random baseDelay (50-250ms)
        Imperfect mouse control : Math.random() * 6 - 3 (horizontal delta)

        Advance Enhacement: 
            1. Content-aware pauses: Use page.evaluate() to detect images/videos and extend delays:
            2. Acceleration curves: Simulate scroll momentum:
            3. Cursor drift: Slight mouse movements during scrolling:

    Best Practices 
        Vary patterns per session: Randomize initial delays/backtracking rates.
        Add "fatigue": Gradually increase pauses after 3-4 scroll steps.
        Combine with other actions: Insert random clicks/hovers during pauses.
        Environment adaptation: Adjust speeds based on viewport size:

    Thinking about this reflecting on the past what things that the server use to know if the user is a human or not other than behaviour 
    '''
    initial_pos = page.evaluate("window.scrollY") # Finding the Position of the Current 
    print(f"Initial Position of Scroll: {initial_pos}")
    page.mouse.wheel(0, 100)
    # time.sleep(1)  # Pause to see the effect


    page.close() 
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


r'''

Behavioral Priority Checklist:
    ✅ Vary scroll speeds (fast flicking vs slow reading)
    ✅ Random cursor movements between actions
    ✅ Occasional mis-clicks with corrections
    ✅ Page-specific dwell times (longer on content pages)
    ✅ Session-specific behavior patterns

# Playwright test
page.goto("https://bot.sannysoft.com")
page.screenshot(path="bot_test.png")

Remember: The key to human-like behavior is introducing controlled randomness - 
not too predictable, not too erratic. 
Start with these fundamentals, then iterate based on target website responses.
'''