from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time



r'''
Mostly Used Modules are "Random" and "Time"
    I need to Debug Things
    

Testing Area for Bots: https://botscan.com/
Defining the Goal in Human Stealth Mode or Human Micmicing 
Random scroll distances (700-1000px)
Variable pauses (1.5-2.5s)
Mimics natural reading patterns

1. Understanding the Problem 

What is the Problem?
    1. Some of the Website can Detect Bots based on how Playwright Moves
    2.  You will get blocked if you are consistent in your actions 

Why do We need to Solve the Problem?
    1. Well Because We need to scrape a website properly and we don't want to get blocked
    2. 
Breaking Down the Problem 


2. Research and Refine the Problem
Note 80% human-like detection avoidance with 20% effort 

1. Ip and Proxy is the No. 1 Best Way to Do things 
2. Headers Perfection Adding Different User Agents is the Thing 
3. Basic Behaviour of the Bot 

Focusing on Basic Behaviour of the bot is the Thing Here 

Delaying action of the Bot 
Implement acceleration/deceleration in scrolling
Add random micro-variations (±10%) to all timings
Include "thinking time" before critical actions
Use different delay profiles for different actions

Varying Speed in Human Scrolling 
    1. Human Like Scrolling Acceleration
    2. Horizontal Variation
    3. Vary Wait Time Based on Scroll Speed 

Figuring out the Level of Complexity and Breaking Down the Steps that i needed to do 
Going Back to the File 
    1. basic_python.py
    2. basic_python_2.py
    3. Relearning the Import Module of "Time" and Observe the Randomness of Thing the seconds it take to do the Stuff 
    4. Focusing on Base_Time first and observe the Randomness and Seconds for it  takes 
    5. Putting it to playwright 
    6. Adding the Scrolling Behaviour in Playwright 
        a. Agressive Scrolling in Playwright 
        b. Sinosidial Pattern 
    

'''
delay_profiles = {
    "pre_click": (1.2, 3.5),    # Decision-making before action
    "post_click": (0.1, 0.4),   # Natural reaction after click
    "scroll": (0.2, 1.5),       # Reading time during scroll
    "typing": (0.08, 0.15),     # Per-key typing speed
    "page_load": (0.8, 4.0),    # "Reading" after navigation
    "think": (3.0, 8.0)         # Strategic pauses
}
# What This Code Does is to pick the numbers and sleep things out to delay the actions
# I needed to Completely Strategize Where i'm going to put the code in the website
# Understanding the Function 
r'''
("context: str") -> None

Working in Multiple Functions at the Same time Especially in human_scrolling functions, I may Add Data Extraction on the code 
'''
def human_delay(context: str) -> None:
    """Delay based on behavioral context"""
    min_time, max_time = delay_profiles[context]
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

def human_scrolling(page):
    page.wait_for_selector(".quote", state="attached")
    initial_height_page = page.evaluate("document.body.scrollHeight")
    initial_scroll_pos = page.evaluate("window.scrollY")
    print(f"Initial Scroll Positon of the Page is {initial_scroll_pos} and Initial Height Positon of the Page is {initial_height_page} ")
    print()
    print()

    scroll_pause_time = 2  
    scrolling_attempt_max = 20
    scrolling_attempt = 0
    scrolling_max = 5
    scrolling_fail = 0
    

    initial_count_quotes = len(page.locator(".quote .text").all())
    while scrolling_attempt_max > scrolling_attempt:
        page.wait_for_load_state("networkidle", timeout=5000)
        prev_scroll_pos = page.evaluate("window.scrollY")
        prev_height_page = page.evaluate("document.body.scrollHeight")

        print()

        page.mouse.wheel(0, 895)
        time.sleep(scroll_pause_time)
        new_scroll_pos = page.evaluate("window.scrollY")
        new_height_page = page.evaluate("document.body.scrollHeight")

        print()

        

        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                print("We Reached the Last Page")
                # break
        scrolling_attempt += 1

        counting_quotes = len(page.locator(".quote .text").all())
        print(f"Updated Counting of Quotes : {counting_quotes}")
        print(f"A Non Updated Counting of Quotes {initial_count_quotes}")

        
        if counting_quotes == initial_count_quotes:
            scrolling_fail += 1
            print(f"No new quotes found. Fail count: {scrolling_fail}")
            if scrolling_fail == scrolling_max:
                break
        else:

            scrolling_fail = 0
            initial_count_quotes = counting_quotes
            print(f"There are New Quotes Found so It will Reset to: {scrolling_fail}")
            print(initial_count_quotes)
    print("Function: Human_Scrolling_Done")
def data_extraction(page):
    quotes_text = page.locator(".quote .text").all()
    for quote in quotes_text:
        print(quote.text_content())
        print()
    
def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    context = browser.new_context(
        viewport={"width": 1366, "height": 768}  
    )
    page = context.new_page()
    page.goto(base_url)
    human_scrolling(page)
    data_extraction(page)
    # data_extraction(page)
    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

r'''
things to Do Learn to 
1. Learn to Simulate Interleaving Things in terms of Function "simulation_2_Function.py"


2. Getting only the new Quotes of things per extractions (I had no idea how to do that )
Position-Based Slicing (90% effective)
https://chat.deepseek.com/a/chat/s/01f5989b-e21a-452e-a4e8-5282b2c0977b
https://chatgpt.com/c/6872c30a-db10-8013-892e-8e3c65d712ff
Works for sites that append content sequentially (most infinite scroll implementations)


3. Apply that in Playwright --> Scrolling, Extraction, Scrolling, Extraction 

def optimized_scrape(page):
    all_quotes = []
    last_position = 0
    
    while True:
        # Scroll and wait for new content
        page.evaluate(f"window.scrollTo(0, {last_position + 1000})")
        page.wait_for_timeout(2000)  # Network-aware wait better
        
        # Get ONLY new quotes
        quotes = page.query_selector_all(".quote")[last_position:]
        if not quotes: 
            break
            
        for quote in quotes:
            text = quote.query_selector(".text").inner_text()
            all_quotes.append(text)
        
        last_position += len(quotes)
4. Implement the Human Mimicing Behavior 
    A. Pre-Action Delays (The 50% Solution)
    B. Human-Like Mouse Movements (30% Solution)
    C. Chunked Scrolling with Variable Pauses (20% Solution)
And Then I'm Done At This Website 
'''