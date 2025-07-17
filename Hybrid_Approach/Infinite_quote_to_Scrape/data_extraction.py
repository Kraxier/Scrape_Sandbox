# Learning to Data Exxtraction in terms of Position Based and Also Adding the Human Delay in the Proccess 


# To Do List I get Paralyze in terms of Doing Multiple Stuff i needed to Prioritize Things
r'''
Focusing on High Yield Results 
    1. Data Extraction 
        - We are collecting all the quotes on every scroll, which is inefficient. We should instead collect only the new quotes that appear after each scroll.
        -  Fix This Parts on Every Scroll 
        - Interleaving “scroll → extract → scroll → extract” is almost always better than doing all your scrolling up‑front and then dumping all the data at once.

    2. Chunked Scrolling With Variable Pauses 
    3. Pre Action Delays 
    4. MHuman Like Mouse Movement 
'''

r'''
Extracting the Scroll
0. How can i Switch to Different Function while the 
1. position-based extraction where as you scroll you are getting only the New Quotes 
2. Pre-Action Delays (The 50% Solution)
    Insert before EVERY interaction (click, type, etc.)
    Why it matters: Bots act instantly, humans hesitate
    Implementation: pre_action_delay() before every action
3. Human-Like Mouse Movements (30% Solution)
    Curved paths instead of straight lines
    Variable speed during movement
    Why it matters: Straight-line movement is #1 bot indicator
4. Chunked Scrolling with Variable Pauses (20% Solution)
    Never scroll full page at once
    Vary scroll distance and speed
    Exponential pauses between chunks

Switching the Function What is the Problem and Formulating the Problem 
1. I want to run a different function while it is Running for example 
    A. i want it to scroll a Function 
    B. And then a Randomize Stop or Delays a Different Function 
    C. A Function that get the Data and Extracting the Data 
Both Deepseek and Chatgpt recommended "Threading" but i ask the question of should i go further to that road 
    Chatgpt and Deepseek
    Best Approach: Asynchronous (Async/Await)
    Playwright’s async API lets you run multiple tasks concurrently in a single thread.

This is the Problem That i been Doing 
Yes! Concurrency is exactly what you need—running multiple tasks in overlapping time periods (not necessarily in parallel). 
Since you're using Playwright for web scraping, here’s the best way to achieve concurrency for your goals:


The Problem in Concurrency is it is Async Thing and i don't want to get ahead of myself jumping from that so maybe i needed to delay things out in there 

I think i will just randomize stuff Things in terms of Function like Scrolling and Pre Action Delay and Human Like Mouse Movement to simulate things 
    - Focusing on Scrolling that there are much higher Ration than the Human Like Mouse Movement and Pre Action Delays +


'''

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time


r'''
How i can procceed to this part? 
What is the Goal?
position-based extraction where as you scroll you are getting only the New Quotes 


page.evaluate('window.scrollBy(0, window.innerHeight)')
    Scrolls by exactly one viewport height
    More reliable than fixed pixel values (works across devices)
    evaluate() executes JavaScript in the page context

Data Merging
for item in current_data:
    if item not in all_data:
        all_data.append(item)    


Adding the Early Termination of the stuff 




Problem 1 is Done i can do it  
putting data_extraction inside of human_scrolling 
They are both 2 Function 
Basically i have a 2 Function let's call it "A" and "B" and i want to put "A" inside of "B" how i can do that in python ? 
How i can put a Function to another Function, Will that able to run ?  

problem 2 

'''

# def data_extraction(page):
#     quote_item = []
#     quotes_text = page.locator(".quote .text").all()
#     for quote in quotes_text:
#         # print(quote.text_content())
#         if quote not in quote_item:
#             quote_item.append(quote)
#             print(quote) 
#         print()
r'''
What is the Problem of the code here? 
1. You're comparing quote (a Playwright Locator object) with items in quote_item (also Locator objects)
    * What does it mean by Playwright Locator Object? 
    # i think the problem lies on the printing the locator quote 
    quotes = page.locator(".quote .text") results: <Locator frame=<Frame name= url='https://quotes.toscrape.com/scroll'> selector='.quote .text'
    not the actual text content 
2.Incorrect Appending:
    You're storing locator objects instead of the actual text content
3. 
'''   

# Second Version of data_extraction(page):
def data_extraction(page):
    quote_item = []
    # Wait for quotes to be present first
    page.wait_for_selector(".quote .text")
    
    quotes = page.locator(".quote .text").all()
    for quote in quotes:
        text_content = quote.text_content().strip()  # Get cleaned text
        if text_content and text_content not in quote_item:  # Check for non-empty and unique
            quote_item.append(text_content)
            print(text_content)  # Print the actual text
    
    return quote_item  # Return the collected data for further use




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

        print("Putting a Data Extraction Function")
        print("Putting a Data Extraction Function")
        print("Putting a Data Extraction Function")
        data_extraction(page)
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
    # data_extraction(page)
    # data_extraction(page)
    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)