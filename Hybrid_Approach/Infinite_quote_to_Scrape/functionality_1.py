# Defining the Minimum Viable Product
# Output: Scrape the Infinite Scrolling and Gathering 100 of the Quotes
r'''
Realize After Going all the Stop of Research and Implementation i realize that my Aim is like a Moving Stars man i found out sometimes my aims are wrong and 
it moves and right now i refining the aims and defining the aims so i always needed to be clear of what i aiming for at things so if it moves i understand why it moves
'''


from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time

def human_scrolling(page):
    page.wait_for_selector(".quote", state="attached")
    initial_height_page = page.evaluate("document.body.scrollHeight")
    initial_scroll_pos = page.evaluate("window.scrollY")
    print(f"Initial Scroll Positon of the Page is {initial_scroll_pos} and Initial Height Positon of the Page is {initial_height_page} ")
    print()
    print()

    scroll_pause_time = 2  
    scrolling_attempt = 3

    while True:
        page.wait_for_load_state("networkidle", timeout=5000)
        prev_scroll_pos = page.evaluate("window.scrollY")
        prev_height_page = page.evaluate("document.body.scrollHeight")
        print(f"Previous Scroll {prev_scroll_pos} Previous Height {prev_height_page}")
        print()

        page.mouse.wheel(0, 895)
        time.sleep(scroll_pause_time)
        new_scroll_pos = page.evaluate("window.scrollY")
        new_height_page = page.evaluate("document.body.scrollHeight")
        print(f"New Scroll {new_scroll_pos} New Height {new_height_page}")
        print()

        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                print("We Reached the Last Page")
                break
        
        quotes = page.locator(".quote .text").all()
        seen_quotes = set()
        for quote in quotes: 
            seen_quotes.add(quote.text_content())
        length_quote = len(seen_quotes)
        print(f"The Length of the Quote that i Currently Scraped: {length_quote}") # Total Quote is 100 Thing Using the 100 As Condition seems Bad because it is a fixed Number to
        print()
    
# def data_extraction(page):
#     page.wait_for_selector(".quote", state="attached")
#     quote_count = 0 
#     quotes = page.locator(".quote .text").all()
#     for quote in quotes: 
#         print(quote.text_content())
#         quote_count += 1
#         print(f"Quote Count: {quote_count}")
#         print()
    
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


# Next Thing is 
r'''
Print the Quote while it Scroll 
Output:

    Quote 
    Height and Scroll Positions 
    Quote
    Height and Scroll Positions 

'''


# Reflect on the Code from the Core and Functionality 
r'''
1. What Things i Implement?
2. How i can Improve the Reliability 
3. How i can Implement Autowaiting and Explicit Waiting and Timeout Handling Implementation 
'''

# For Project Based Learning Approach 
r'''
The Problem That i do 
1. Project based Learning Overload 
	- I did try to Implement All Topics at Once 
	- Maybe i should go step by step for each of the concept that i do 
	- Solution is Implement the Imperfect Concept Each of one of things 
	(Define the Baseline of When i'm Done for each of the concept)
		- Figure out What is things i didn't know yet 
		- Move on After Defining and Completing the Concept of it 

2. Build a Good Enough and then Optimize it for later 
3. Concept Stack Overload 
4. Research Paralysis 
	Roadmap Plans 
	Fix Implementation Before Research, Build First and then Consult references when stuck

5. Identify the Core Goal 
	Break it Down how you can do it 
	Basic Scrolling 
	Make it Work 
	Make it Reliable
	Make it Human Like
	MAke it Fast 
6. Define the MVP (Minimum Viable Product) and Timebox How much you can do it 


How to Research for Project Based Learning Approach 
1. The Right Now Test 
	Figure out what is the necessary The Basic Functionality 
	and then the Should Have like Improve Reliability 
	and then Could have Advance Optimization 

Core Functionality 
Reliability 
Stealth 
Performance 

Playwright Scroll Detection 
Infinite Scroll Termination Conditions
Wait_for_selector vs wait_for_functions 

Stage Specific  Researches for the Website 
	Playwright Detect End of Infinite Scroll 

Apply the 20 Minute Research Rules 
Find the 1 - 2 Solution for you CRRENT blocking Pattern 
Implement Immediately 

Mindset Shifts
1. Learn Through Failure not Prevention 
# this hit hard because i want to prevent things not to learn through it and adapt through it even though i can avoid the failure in the future 



Summary of Things i needed to do right now

1. Mindset i should have is learn through failure not prevention in terms of Coding 
2. Research Only What is the Functionality of the Program
	* Define the MVP (Minimum Viable Product) What Work must be done so also the output
		- Make it Work (Functionality)
		- Goal Create a Script that achieve the Core Task 
	* Define the Reliability 
		- Ensuring the Script Works 9/10 Under Normal Conditions 
		- Error Handling and Adaptive Behaviour 
	* Define the Optimization 
		- Refine the Performance and Avoid Detection 
		- Quality over Raw Functionality 

'''