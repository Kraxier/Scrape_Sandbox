# Building Scrolling like a Infinite Scroller Thing 

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time

r'''
    A[Viewport Setup] --> B[Human-like Scrolling]
    B --> C[Explicit Waiting Core]
    C --> D[Verification Checks]
    D --> E[Retry Mechanisms]
    E --> F[Smart Verification]
    F --> G[Data Extraction]
    G --> H[State Management]
    H --> I[Stealth Optimization]
'''

# Building Simple Scrolling just Down Thing and then the Human Like Scrolling
r'''
    2. Scroll Detection & Handling
    Detect when new content loads (DOM mutations)
    Track scroll position vs page height
    Identify "loading" indicators/spinners
'''
def human_scrolling(page):
    # height = page.evaluate("document.body.scrollHeight") # Full page height 
    # scroll_pos = page.evaluate("window.scrollY") # 	Current scroll position (pixels)
    # print(f"Initial Height of the Page is {height}")
    # print(f"Initial Scroll Positon of the Page is {scroll_pos}")
    # page.mouse.wheel(0, 1000)
    # height = page.evaluate("document.body.scrollHeight") 
    # scroll_pos = page.evaluate("window.scrollY")
    # print(f" Final Height of the Page is {height}")
    # print(f" Final Scroll Positon of the Page is {scroll_pos}") 
    # r'''
    # This Code Track the Height and Scroll 
    #     Height Doesn't change when i try to scroll it 
    #     Only the Scroll Position Change After it Scrolled Obviously 
    #     After it Scrolled it Give me the Final Position of 
    # '''

    # for x in range(5):
    #     scroll_pos = page.evaluate("window.scrollY") 
    #     print(f"Initial Scroll Positon of the Page is {scroll_pos}")
    #     page.mouse.wheel(0, 895)
    #     scroll_pos = page.evaluate("window.scrollY") 
    #     print(f"Final Scroll Positon of the Page is {scroll_pos}")
    #     print()
    r'''
    I think The Problem With this Code is it Didn't wait to load the damn page
    because the code is really fast so i needed to wait it first 
    
    Preventing "Spammy" Scrolling and Ensuring Proper Loading 🛡️
    The output you're seeing indicates you're scrolling too fast without waiting for content to load. Here's why it happens and how to fix it:

    The Core Problem:
        Lazy-Loaded Content: Modern websites only load content when it enters/nears viewport
        Render Timing: DOM updates happen asynchronously after scrolling
        Scroll Chaining: Browsers limit consecutive scroll operations
    '''

    # for x in range(5):
    #     # prev_scroll_height = page.evaluate("document.body.scrollHeight")
    #     scroll_pos = page.evaluate("window.scrollY") 
    #     print(f"Initial Scroll Positon of the Page is {scroll_pos}")
    #     page.mouse.wheel(0, 895)
    #     # After Adding this line of Code it scroll for some of the things but it is not smoothly scrolling things 
    #     page.wait_for_load_state("networkidle", timeout=3000)
    #     scroll_pos = page.evaluate("window.scrollY") 
    #     print(f"Final Scroll Positon of the Page is {scroll_pos}")
    #     print()

    r'''
    # This Solution is Stupid Man 
        1. Creating a Condition where i need to keep a scrolling whenever there are new content after scrolling things better than timeout i think
        - because i need to keep counting the quotes making the code longer
    
    # Another Solution 
        2. Adding the numbers between new Height of the Page and using that as Conditions
    '''
    
    # I observe the code got bigger based on this stuff 
    # Adding to the state to attached is really necessary 
    r'''
    I should only add it once because it only get the first one 
    '''
    page.wait_for_selector(".quote", state="attached")
    initial_height_page = page.evaluate("document.body.scrollHeight")
    initial_scroll_pos = page.evaluate("window.scrollY")
    print(f"Initial Scroll Positon of the Page is {initial_scroll_pos}")
    print(f"Initial Height Positon of the Page is {initial_height_page}")


    r'''
    ✅ What's Really Going On
        This is typical of a lazy-loading/infinite scroll page that loads:
        New content only after reaching a certain point
        Content in batches, triggered by being near the bottom of current content
        Sometimes with delays, depending on backend or throttling
    '''
    scroll_pause_time = 1  # seconds
    while True:
        page.mouse.wheel(0, 895)
        time.sleep(scroll_pause_time)
        page.wait_for_load_state("networkidle", timeout=5000)
        new_height_page = page.evaluate("document.body.scrollHeight")
        new_scroll_pos = page.evaluate("window.scrollY")
        print(f"Scroll: {new_scroll_pos}, Height: {new_height_page}")

        if new_height_page >= 15848:
            page.mouse.wheel(0, 895)
            print("I Reached the Last Page")
            print(f"Scroll: {new_scroll_pos}, Height: {new_height_page}")
            
    # I let the Deepseek and Chatgpt Analyze my Code:
    r'''
    1. Remove the Magic Numbers Which means Avoid hard‑coding a terminal height (15848)—that value can change whenever the site content changes or you scroll on a different viewport
        *  Instead, detect when no new content is coming
        * Aka Dynamic Height Tracking  Works for any page size/resolution
    2. Use Exponential Backoff or Adaptive Pauses
        * Rather than a fixed 1 s pause, you can start small and back off if the page takes longer:
        * Combines network idle + short DOM wait
        * Handles both AJAX and DOM-render delays
    '''
    



def data_extraction(page):
    page.wait_for_selector(".quote", state="attached")
    quote_count = 0 
    quotes = page.locator(".quote .text").all()
    for quote in quotes: 
        print(quote.text_content())
        quote_count += 1
        print(f"Quote Count: {quote_count}")
        print()
    
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    context = browser.new_context(
        viewport={"width": 1366, "height": 768}  # Most common desktop size # Basically a 3/4 of My Laptop 
    )
    page = context.new_page()
    page.goto(base_url)
    
    
    human_scrolling(page)
    
    

    # data_extraction(page)
    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


# Viewport Size Concept
r'''
Desktop	1920x1080, 1366x768, 1440x900
Laptop	1280x720, 1536x864

Recommendation for "Human-Like" Desktop:
1366x768 or 1920x1080 (most statistically common).


Option 2: Randomize Between Common Human-Like Viewports
def get_random_human_viewport():
    common_viewports = [
        {"width": 1366, "height": 768},  # Most common
        {"width": 1920, "height": 1080}, # Full HD
        {"width": 1440, "height": 900},  # MacBook-like
        {"width": 1536, "height": 864},  # Common 16:9
    ]
    return random.choice(common_viewports)

    
What does it mean by "Context" in Playwright 🧠?
In Playwright, BrowserContext is a fundamental concept that represents an isolated browsing session. 
Think of it as an incognito-like session within your browser where all activities are isolated from other contexts. Here's a breakdown:

Key Characteristics of a Browser Context:
    1. Isolated Environment:
        * Each context has separate:
            Cookies
            Cache
            Local storage
            Session storage
    Like having multiple private browsing sessions in one browser

    2. Resource Management:
        * Controls settings for:
            Viewport size
            User agent
            Geolocation
            Permissions (camera, mic, etc.)
            Network settings

    3. Multi-Session Capability:
        Create multiple contexts to simulate different users/devices in parallel
'''

# Concepts in Scrolling Part 

r'''
Understanding the Scroll Behavior in Playwright
The behavior you're seeing is completely normal and occurs because of how browsers handle scrolling. 

1. Viewport Height Limitation:
Browsers can only scroll until the bottom of the viewport reaches the bottom of the page

2. Scroll Position vs. Scroll Distance:
window.scrollY = current vertical scroll position (pixels from top)
mouse.wheel() = relative scrolling distance (delta pixels to move)

Visualizing the Math 
    Page Height (document.body.scrollHeight): 2500px
    Viewport Height (window.innerHeight): 800px

    --------------------------------------------
    Max Scroll Position: 2500 - 800 = 1700px

    If you try to scroll 1619px from position 0:
    0 + 1619 = 1619px (which is < 1700px) → Works!

Why Use the Modified Code with Safety Checks? 🛡️
1. Prevents Impossible Scrolling Attempts
Browsers physically cannot scroll beyond (page height) - (viewport height). 
Attempting to do so silently fails, wasting resources and potentially missing data.
2. Handles Variable Page Sizes
Websites have wildly different page lengths:
News articles: 2,000-5,000px
Product listings: 10,000px+
Landing pages: <1,000px
Safety checks adapt to each page's actual dimensions.

Variable Chunk Sizes	Humans don't scroll fixed distances	Breaks robotic patterns
''' 

# Things i needed to work on Infinite Scrolling 
r'''
I needed to Get the Initial Metrics of the Website
    Height of the Page 
    Current "Y" Position of the Page 
    Viewport Size of my Code 

# Get initial metrics
    last_height = page.evaluate("document.body.scrollHeight")
    current_y = page.evaluate("window.scrollY")
    viewport_h = page.evaluate("window.innerHeight")
# Go to the Scroll Target 
    Which is really vague for me What do you mean by Scroll Target?
    But Deepseek Said Humans don't Scroll to the Very Bottom itself 
    so i needed to varies using the Current height of the page and then moving in different interval of things

# Next Question is How Data Extraction is the next thing? 
'''