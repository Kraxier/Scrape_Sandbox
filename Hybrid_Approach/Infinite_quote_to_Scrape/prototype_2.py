# python prototype_2.py

r'''
Goal Fix the Scrollable for more Robust Thing 
    1. No more Magic Numbers 
    2. Implement Data Extraction
    3. Implement Explicit Waiting part of things 
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


    scroll_pause_time = 2  # seconds
   
    # Using this as Dynamic Thing Thing 
    # countering_loop_height = 0 
    # counter = 0 

    # Attempts 
    scrolling_attempt = 3

    while True:
        page.wait_for_load_state("networkidle", timeout=5000)
        prev_scroll_pos = page.evaluate("window.scrollY")
        prev_height_page = page.evaluate("document.body.scrollHeight")
        print(f"Previous Scroll {prev_scroll_pos} Previous Height {prev_height_page}")

        page.mouse.wheel(0, 895)
        time.sleep(scroll_pause_time)
        new_scroll_pos = page.evaluate("window.scrollY")
        new_height_page = page.evaluate("document.body.scrollHeight")
        print(f"New Scroll {new_scroll_pos} New Height {new_height_page}")

        # print(f"Scroll: {new_scroll_pos}, Height: {new_height_page}")

        
        # if new_height_page > prev_height_page:
        #     # Continue Scrolling 
        #     pass
        # if new_height_page < prev_height_page
        
        # countering_loop_height = prev_height_page
        # print(f"Observing Countering Loop Height Thing: {countering_loop_height}")  

        # Problem with the Code is The Attempt Thing to Early To Break 
        # Scrolling Position will never be Equal i think 
        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                print("We Reached the Last Page")
                break

        print()
        quotes = page.locator(".quote .text").all()
        seen_quotes = set()
        for quote in quotes: 
            seen_quotes.add(quote.text_content())
            # print(quote.text_content())
            # quote_count += 1
            # print(f"Quote Count: {quote_count}")
            # print()
        # print(f"Outside of Loop Quote Count: {quote_count}")
        length_quote = len(seen_quotes)
        print(f"The Length of the Quote that i Currently Scraped: {length_quote}") # Total Quote is 100 Thing Using the 100 As Condition seems Bad because it is a fixed Number to
        print()
    
        
        # What is Good Conditional After Getting the Initial Height and the Final Height  
        r'''
        The Problem first i needed to solve is "15848" 
        I needed to Keep it scrolling Until there are no New Content at things 
        Based on my Code it Keep Scrolling until it Reaches to 15848 Thing Geting the Height  

        First Condition if Scrolling Position is Equal to Height of the Page # There are no Equal because if it is Endless Running it will never be equal 
        Second Condition if the Height of the page Doesn't Change means it keep repeating 
            Problem in Second Condition until the scroll doesn't reach a certain point Height Will not Change 
                Scroll: 5831.2001953125, Height: 8022
                Scroll: 6726.39990234375, Height: 8022

        Height Change Depends on Where the Scroll Position is so it is very relative to each other 
        Height Change Where you Reaches a Certain Point 

        Third Condition Where it Keeps Extracting the Number of Quotes if it is Steadily increasing it means it still loading a content 
        Also Maybe Adding an Attempt in While Loop to be more Robust at Things 

        Chatgpt and Deepseek Reconmmended Height Dynamic Tracking (I had No Idea How to Do that Yet but Maybe Later)

        '''

        # First Condition to Stopped 
        # if new_height_page >= 15848:
        #     page.mouse.wheel(0, 895)
        #     print("I Reached the Last Page")
        #     print(f"Scroll: {new_scroll_pos}, Height: {new_height_page}")

        # Second Condition to Stopped Using the Number of Quotes good for the Limitation in Scrapping things 
        # if length_quote == 100:
        #     print(f"No More Content To Extract")
        #     print(f"We Reached the Last Page")
        #     break 
        
        # Third Condition to Stopped Which is Using the Scrolling Position i think this is not good for the things because it will just keep scrolling 
        # Fourth Condition is how to do Detecting Height Thing for Dynamic Height Tracking 
        r'''
        What is my Observation so far ?
        Height Will Change after the Scrolling Position Reaches a Certain Point that is a good Detector 
        Height Will not CHange if you reach Fully at the Bottom of things 

        Get the Previous Height 
        Scroll 
        Get the New Height 
        Compare the Previous Height to New Height and if new Height is Greater than Previous Height that means a New Loaded Content 
            I needed to be Careful on this because it will not Update the new height if the Scrolling Position Doesn't reaches a Certain Point 
                - Solution is if the Comparing the Previous Height of the Scrolling Position to New Height of Scrolling Position if it is still increasing (Greater than)
                it means the Loop Will Continue 
        
        When will it Stop? 
            If the Previous Height is Equal to New Height (Maybe Adding the Attempts in terms of Scrapping things ) i Should Break the Damn Loops 

        '''

        # if new_height_page == countering_loop_height:
        #     print()
        #     print("They Are Same Period of Time")
        #     counter += 1
        #     print(f"Counter Number Currently are {counter}")
        #     print()



            
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
    r'''
    ✅ What's Really Going On
        This is typical of a lazy-loading/infinite scroll page that loads:
        New content only after reaching a certain point
        Content in batches, triggered by being near the bottom of current content
        Sometimes with delays, depending on backend or throttling
    '''

# Use This Guide as a Thing
# def scroll_to_bottom(page, max_attempts=20):
#     """Scrolls to page bottom dynamically"""
#     scroll_pause = 0.8  # Seconds between scrolls
#     scroll_step = 895   # Pixels per scroll
#     attempts = 0
    
#     # Initial measurements
#     last_height = page.evaluate("document.body.scrollHeight")
#     print(f"Starting height: {last_height}px")
    
#     while attempts < max_attempts:
#         # Scroll down
#         page.mouse.wheel(0, scroll_step)
        
#         # Wait for content to load
#         time.sleep(scroll_pause)
#         page.wait_for_load_state("networkidle", timeout=3000)
        
#         # Get updated metrics
#         new_height = page.evaluate("document.body.scrollHeight")
#         current_scroll = page.evaluate("window.scrollY")
        
#         # Progress tracking
#         print(f"Attempt {attempts+1}: Scrolled to {current_scroll}px, Height: {new_height}px")
        
#         # TERMINATION CONDITIONS:
#         # 1. Height unchanged (no new content)
#         if new_height == last_height:
#             print("✅ Reached end of content - no height change")
#             return True
            
#         # 2. Near bottom detection
#         if current_scroll + 1000 >= new_height:
#             print("✅ Reached bottom of page")
#             return True
        
#         # Update for next iteration
#         last_height = new_height
#         attempts += 1
    
#     print(f"⚠️ Stopped after {max_attempts} attempts (safety limit)")
#     return False
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



r'''
Learning to be Problem Solver as a Developer 

Why first learn to be a problem solver because you don't need to know everything 
in features of a language buts instead of focusing on solving problems and this 
is that the company want 



7 Concept of Problem Solver
1. Identifying the Problem First understanding the ature 
    * Spend more Time Thinking the Problem 
    * defining the Problem through Agile approach where 
        - Break the Problems into a smaller steps 
        - Identify the PRoblem Statement 
            - What is the Context
            - What is the Issue 
            - Why do we need to solve the problem (Why was it Worth of Time)\
2. Research and Refine the Problem 
    - What People go Through the Problem because you are unlikely to be the one in that 
    - Use the Code as the Solution but understanding the code is really important 
    - Discussion to other developers 
3. Pseudo Code 
    - Writing the Outline how we can implement the Damn Code 
    - Focus on the Logic of the Code without Worrying about the syntax 
    - Cache Validating THings
    - Naming THings 
    - Understanding and then Implementing the Code 
4. Test Driven Development 
    - Test if there are new Feature in the Code 
    - What Test Will be good in that Feature 
    1. Failing the Test
        This should be force you to think What you are trying to do 
    2. Write the Code to Pass the Test 
        - Implementing 
    3. OPtimize it to Pass the Damn Test 
        - SImplify and Optimize your Code and do some reflection here 
5. Implement Code (Work As Fast as Possible )
    Pyschological Tool to Help as a Programmer 
    Done is Better than Perfect 
    Rushing the Code like you are in the Hackaton 
6. Good Time and have a Sleep to solve the problem 
    - Focus Mode and Relax Mode thing forgot the term but this is the Break down 
    - Take a 15 Minute Break (Fixing the Scene)

7. Optimzation 
    - Improve Readavility 
    - Add Comment
    - Remove Duplication 
    - Optimize Time/Space Complexity 
    - Add Error Handling 
8. Practice Seriously there are infinite new problems 
    - No Amount of Framework or Language if you can really solve the problem
    - Kinda Vague and hard to measure for real man 
    - Practice Different PRoblem Solving Approach at things 
    - PRactice Repeat , Getting the Feedback in the problem 


Identifying the Problem in Infinite Scrolling 
1. UNderstanding the Nature of the Website
    - After A Certain amount of Scroll it trigger something to load a new content until i reaches at the very bottom 
2. What is the Problem 
    - Create a Code or Bot or Program that will Continous Scroll until it reaches to the very bottom {Done}
    - Problem of my Code based on the Analyzation of the Deepseek and Chatgpt is 
        1. I used the Magic Number 
            - It Means i use the "15848" as the stopping code of the loops
            - This means it is not dynamics and might break on different pages or screen size 
            - This Means we should compare the new height for the previous height 
            - Extracting the initial height of the page , Wait the page to load the new content, Get another height of the page 
            after getting the height of the page is to scroll again using that variable and then repeat until 
            we reached the last page 
            - Another Problem is Adding Maximum Scroll Attempt limit to prevent infinite loops 

            
3. Why Would i care on this?
    - Page heights vary across websites
    - Same website may have different content lengths
    - Different screen resolutions affect render height
    - Websites update layouts/content over time

b) Lack of Dynamic Height Comparison
    Critical missing piece: Not comparing current vs previous height
    Result: Can't detect when new content stops loading

c) No Safety Mechanism
    Risk: Infinite loops if content keeps loading
    Result: Program hangs indefinitely
'''



# Getting Feedback Based on my Damn Shitty Code and MY Thought Proccess Involving Scrapping Things 