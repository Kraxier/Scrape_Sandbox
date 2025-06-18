# python implement_pareto.py

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

    # initial_position = page.evaluate("window.scrollY")
    # print(f"Initial scroll position: {initial_position}") # Verification of the program


    # I think the problem is How to keep it scrolling and wait for it to load something
    # First is Scrolling to the Bottom and wait 
    # Maybe Getting all the Quotes in a unscrollable way first after that i need to define the how many pixel will it be or there are more alternative in this way 

    r'''
    “A day without sunshine is like, you know, night.”
    by Steve 
    

    “A day without sunshine is like, you know, night.”
    by Steve Martin

    Maximum Page Load is The Scrolling thing 
    '''

    # full_height = page.evaluate('document.body.scrollHeight') # Determine the Fully Height of the Page
    # page.evaluate('document.body.scrollHeight')
    # initial_position = page.evaluate("window.scrollY") # Determine the where is the currently scroll of the page 
    # page.evaluate("window.scrollY") 
    # page.mouse.wheel(0, 1615) # Scrolling of Something 
    
    # Create a Program that can keep Scrolling to the very Last page if that is exist i don't know it yet if it is infinite 
    # page.mouse.wheel(initial_position, full_height)
    # full_height = page.evaluate('document.body.scrollHeight')
    # print(f"This is a new Height can this be added ? {full_height}")
    
    # What if instead of Variable i will add it 
    r'''
    Page Height is 1601 What if i Double it? 
    '''
    # page.mouse.wheel(initial_position, 3202) # I try to Double the numbers height from 1601 to 3202 the problem is i think the browser are still loading it up 
    # I needed to wait until it's loaded 


    ############################################### Goal is to Keep it Scrolling #################################################
    # Phasing it Properly i want to continously scroll it 

    # page.wait_for_selector(".quote", state="attached")
    # full_height = page.evaluate('document.body.scrollHeight')
    # print(f"First Height of the page{full_height}")
    # page.mouse.wheel(0, 1601)
    # page.wait_for_selector(".quote", state="attached")
    # page.mouse.wheel(0, 1601)
    # full_height = page.evaluate('document.body.scrollHeight')
    # print(f"Second Height of the page{full_height}")

    ################################################# Second Version to Keep it Scrolling ###############################################
    
    i = 1 
    page.wait_for_selector(".quote", state="attached")
    full_height = page.evaluate('document.body.scrollHeight')
    print(f"First Height of the page:{full_height}")
    for _ in range(25):
        print(i)
        i += 1
        updating_height = page.evaluate('document.body.scrollHeight')
        print(f"Updating the Height:{updating_height}")
        page.mouse.wheel(0, full_height)
        page.wait_for_timeout(2000)  # Wait for content to load 
        # from the page.wait_for_timeout i think this is like timesleep() maybe i was wrong but i think this is precise 
        # I needed a new Alternative for this stuff 

    r'''
    Output 
        First Height of the page1622
    Updating the Height1622
    Updating the Height3547
    Updating the Height3547
    Updating the Height5107
    Updating the Height6539
    Updating the Height8022
    Updating the Height9530

    notice that some of it got repeating for some reason

    Updating it Adding the range(7) --> range(12)

            First Height of the page1626
        Updating the Height:1626
        Updating the Height:5107
        Updating the Height:5107
        Updating the Height:5107
        Updating the Height:6539
        Updating the Height:8022
        Updating the Height:9530
        Updating the Height:11193
        Updating the Height:11193
        Updating the Height:12702
        Updating the Height:14365
        Updating the Height:14365
    range(12) --> range(25)
    First Height of the page:1621
        1
        Updating the Height:1619
        2
        Updating the Height:3547
        3
        Updating the Height:3547
        4
        Updating the Height:5107
        5
        Updating the Height:6539
        6
        Updating the Height:8022
        7
        Updating the Height:9530
        8
        Updating the Height:11193
        9
        Updating the Height:11193
        10
        Updating the Height:12702
        11
        Updating the Height:14365
        12
        Updating the Height:14365
        13
        Updating the Height:15848
        14
        Updating the Height:15848
        15
        Updating the Height:15848
        16
        Updating the Height:15848
        17
        Updating the Height:15848
        18
        Updating the Height:15848
        19
        Updating the Height:15848
        20
        Updating the Height:15848
        21
        Updating the Height:15848
        22
        Updating the Height:15848
        23
        Updating the Height:15848
        24
        Updating the Height:15848
        25
        Updating the Height:15848


    Based on the Feedback by Deepseek:
        1. Fixed Scroll Distance:
            page.mouse.wheel(0, full_height) scrolls by a fixed distance (initial page height). 
            After new content loads, this distance may not reach the bottom of the expanded page.
        2. Stagnant Height Values:
            Repeated height values (e.g., 3547 appearing twice) occur because:
            The scroll distance was insufficient to trigger new content loads
            The timeout (2000ms) might be too short for dynamic content
            Content loading might require specific triggers (not just scrolling)
        3. Premature Termination:
            The loop runs 25 times regardless of whether new content exists, 
            wasting time on redundant operations once all content is loaded.

        Solution is 
            Proper Waiting of the Content to load 
            Figure out how many times it needed to loop 

        Deepseek Solution 
            Scroll to Absolute Bottom:
            Uses window.scrollTo(0, document.body.scrollHeight) instead of relative wheel movement.

            Content-Aware Waiting:
            Uses wait_for_selector with a timeout to detect new .quote elements. Adjust the selector based on your content patterns.

            Early Termination:
            Breaks the loop immediately if the page height doesn't change after a scroll.

            Flexible Attempt Limit:
            Still caps attempts at 25 but exits early when content stops loading.
    
     
       '''



    input("Press Enter to Stop the Program ")
    page.close() 
    browser.close()

with sync_playwright() as playwright:
    run(playwright)



# Scroll Mechanism
# Use page.evaluate() to scroll to absolute bottom:
# $ page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
# Why better than mouse wheel? Guarantees reaching bottom regardless of screen size


# Content Loading Detection

# Option A: Height comparison
# new_height = page.evaluate("document.body.scrollHeight")
# if new_height == last_height:
#     break

# Option B: Wait for new elements (more precise)
# quote_count = len(page.query_selector_all(".quote"))
# page.wait_for_function(
#     f"{quote_count} < document.querySelectorAll('.quote').length",
#     timeout=5000
# )

# Dynamic Waiting
# Hybrid approach (recommended):
# try:
#     page.wait_for_selector(".quote >> nth=-1", state="attached", timeout=3000)
# except:
#     # Fallback to height check
#     if page.evaluate("document.body.scrollHeight") == last_height:
#         break
# Termination Conditions
# Exit when:
# Content stops loading (height stabilizes)
# Maximum attempts reached (safety net)
# New elements fail to appear