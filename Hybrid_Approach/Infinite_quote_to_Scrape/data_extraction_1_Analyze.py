
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time


r'''
To Do List
1. Analyze the Third Terminations [Done]
2. Analyze the data_extraction of Quotes [Done]
    3. Position Based Extracting 
        - Extracting Content Based on current scroll position 
        - It focuses on content currently in view or just loaded after a scroll action
4. Saving data in CSV Files 
5. Creating and Mimicing Human Behaviour 
    * Pausing 
    * Scrolling 
6. Done
        
'''

r'''
Understanding Position Based Extracting: 
Extracting based on the current Scroll Position of the Page:
    Content currently in the viewport (visible area of the browser).
    Dynamically loaded content after a scroll action (common in infinite-scroll pages). # This Check the Current Practice of Mine 

This is the Best Way for Ifinite Scrolling 
    In terms of Efficiency 
        A. Proccess only Visible Content 
        B. Avoid Storing Thousands of off-screen Elements 
    Realistic Simulation by passing Anti bot Detection 
    Work with Dynamics Sites like React and Angular where content loads on scroll

Challenges:
    1. Scroll Timing 
        - Require Precise wait_for_selector() or wait_for_function() calls after scrolling to ensure content loads.
        - Elements may unload/reload during scrolling (common in virtualization).
        - Logic to track scroll depth/break conditions is needed.
    2. Elements May Unload or Reload During scrolling (Not a Case of Mine)
    3. Position Trackig Logic to Track Scroll Depth/Break Condition is Needed 

Conclusion: Basically as i scroll i also extracting the quotes of it


1. Mimicing Human Behaviour 
    A. Chunked Scrolling with Variable Pauses (20% Solution)
        Never scroll full page at once
        Vary scroll distance and speed
        Exponential pauses between chunks
    B. Pre-Action Delays (The 50% Solution)
        Insert before EVERY interaction (click, type, etc.)
        Why it matters: Bots act instantly, humans hesitate
        Implementation: pre_action_delay() before every action
    C. Human-Like Mouse Movements (30% Solution)
        Curved paths instead of straight lines
        Variable speed during movement
        Why it matters: Straight-line movement is #1 bot indicator 

   
Let's Go To Mimicing Human Behaviour First Because it Depends on the Scrolling Behaviour
And then i needed to do Scroll Timing and Position Tracking which is very quote nice because i will also learn 
Waititing and Expect 

'''







# |||||||||| Mimicing Human Behaviour Through Pausing |||||||||||
r'''
Recommendation 
Combine with Playwright Waits:
Always use Playwright's built-in waits (wait_for_selector(), wait_for_load_state()) BEFORE human delays to ensure page readiness.
'''

# Why I put This Code?
r'''
This is Basically Storing the strategic pause of mimicing human behaviour 
basically i can select what are things i can do and how many seconds in between in doing that thing 

Each value is a tuple representing the minimum and maximum delay time for that context.
'''
delay_profiles = {
    "pre_click": (1.2, 3.5),    # Decision-making before action
    "post_click": (0.1, 0.4),   # Natural reaction after click
    "scroll": (0.2, 1.5),       # Reading time during scroll
    "typing": (0.08, 0.15),     # Per-key typing speed
    "page_load": (0.8, 4.0),    # "Reading" after navigation
    "think": (3.0, 8.0)         # Strategic pauses
}

# Why I Put this Code?
r'''
human_delay can pick any of the delay profile the problem of that is i can randomize the 
behaviour like the "keys" in order to do things or also i can just pick something in delay profile and let the 
function do the strategic and picking the seconds in between into doing things 
'''
def human_delay(context: str) -> None:
    """Delay based on behavioral context"""
    min_time, max_time = delay_profiles[context]
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)
r'''
How to Put Things 
# 🎲 Randomize the context:
random_context = random.choice(list(delay_profiles.keys()))
human_delay(random_context)

# Or Specific Context 
human_delay("scroll")
'''

# Understanding the "def human_delay(context: str) -> None:"
r'''
🔹context: str 
This defines the parameter of the function:
    🔹context is the name of the argument passed into the function (like "typing" or "scroll").
    🔹: str is a type hint, which tells readers (and tools like linters or IDEs) that context should be a string.
Examples: human_delay("typing")
Here, "typing" is a string, and it's passed as the context.

🔹 -> None [This is the return type hint.]
    🔹-> None means the function does not return any value.
    🔹It performs an action (like causing a delay), but doesn’t give you anything back.

If you removed the type hints, it would still work in Python:
eg: def human_delay(context):

…but type hints are helpful for:
    Code readability
    Better autocomplete in editors
    Static analysis (like with mypy)
'''

#||||||||||| Analyze Data Extraction |||||||||||
# Second Version of data_extraction(page):
def data_extraction(page):
    quote_item = []
    page.wait_for_selector(".quote .text")  # Wait for quotes to be present first
    quotes = page.locator(".quote .text").all() # Locating the Quotes getting Everything 
    print(f"🎯 Found {len(quotes)} quote elements in current DOM")  # Getting How many Locator Found 
    for quote in quotes: # Iterating for Every Quotes 
        text_content = quote.text_content().strip()  # Get cleaned text
        if text_content and text_content not in quote_item:  # Check for non-empty and unique
            quote_item.append(text_content) 
            print(text_content)  # Print the actual text
    print(f"📦 Returning {len(quote_item)} unique quotes from current extraction")
    return quote_item  # Return the collected data for further use


def human_scrolling(page):
    all_quotes = []  # Master collection list
    page.wait_for_selector(".quote", state="attached") #  Wait for the first Quote to Attached in the Page 
    initial_height_page = page.evaluate("document.body.scrollHeight") # Getting the Initial Height of the Page 
    initial_scroll_pos = page.evaluate("window.scrollY") # Getting the Initial Scroll Position of the Page 
    print(f"Initial Scroll Positon of the Page is {initial_scroll_pos} and Initial Height Positon of the Page is {initial_height_page} ") # Printing Things 
    print()
    print()


    # |||||||||| Mimicing Human Behaviour Through Scrolling |||||||||||

    # Why? For 80% Maximum Scrolling Thing 
    viewport_height = page.viewport_size["height"]
    print(f"Viewport height: {viewport_height}px")
    


    #||||||||||| Maximum Attempt First Termination |||||||||||
    # Used in While Loop for the Condition to be True {Scrolling_attempt_max and scrolling_attempt}
    # Why: We Used Scrolling Attempt Max to not keep Scrolling Forever so we terminate the program once it reaches the maximum attempt
    # Problem: It Will Always Increment at the end of the Loop the Problem is, it will not go back to 0 so Just a Maximum Attempt of Scroll only

    #||||||||||| Maximum Attempt First Termination |||||||||||
    scrolling_attempt_max = 20 # How many are the Max Scrolling 
    scrolling_attempt = 0 # How many Attempts that it Scrolls 
    scroll_pause_time = 2  
    #||||||||||| Second Termination: Counting The Quotes |||||||||
    # Description: Counting the Quotes for Every Scroll, If the Quotes are not incrementally adding a new found quotes the program will terminate itself 
    # Description: 
    r'''
    Why:
        * Another Termination program to make it more robust, this program will keep counting the quotes if there are new quotes been found in the infinite scrolling
        But if there are no new Quotes are found it will terminate the program 
        * Caveat: 
            - There are Buffer like scrolling_max and scrolling_fail to not terminate the program if there are no new quotes because the content can load sometimes and 
            take a while to load so it is very important to put some buffering
    '''
    #||||||||||| Second Termination: Counting The Quotes |||||||||
    initial_count_quotes = len(page.locator(".quote .text").all()) # Initial Counting of the Quotes 
    scrolling_max_termination = 5
    scrolling_fail_buffer = 0

    while scrolling_attempt_max > scrolling_attempt:
        # |||||||||||  Third Termination |||||||||||
        page.wait_for_load_state("networkidle", timeout=5000) # Waits until the network is idle (i.e. no more network requests are ongoing), indicating the page has finished loading.
        # Storing the Current Height and Scrolling Position 
        prev_scroll_pos = page.evaluate("window.scrollY")
        prev_height_page = page.evaluate("document.body.scrollHeight")
        print()

        # Scrolling down to 895 Pixels 
        page.mouse.wheel(0, 895)
        time.sleep(scroll_pause_time)

        # |||||||||||  Third Termination |||||||||||
        # Getting the New Scrolling Position and New Height After it Scroll 
        new_scroll_pos = page.evaluate("window.scrollY")
        new_height_page = page.evaluate("document.body.scrollHeight")
        # 2 Condition to Work if after Scrolling and there are no new heights and no new Scroll posiition 
        # It Will Break the While Loop means i'm at the End 
        # This only Work if there are an End in the Things 
        r'''
        It’s Heuristic-Based (Not Foolproof)
        You're assuming that:
            * If scrollHeight doesn't increase and scrollY doesn't change after scrolling, the page has no more content.
        But:
            * Some pages load content in a delayed or batched manner — there may still be more data if you wait longer.
            * JavaScript-heavy pages might not update scrollHeight correctly until some time has passed.
        '''
        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                print("We Reached the Last Page")
                # break

        #||||||||||| Analyze Data Extraction |||||||||||
        current_quotes = data_extraction(page)  # Store return value # Why It Store in a Variable not in a list? 
        print(f"🔄 Received {len(current_quotes)} quotes from extraction") # Counting the Length of the Quotes 

        # Track new unique quotes
        new_count = 0
        for quote in current_quotes:
            if quote not in all_quotes:  # Check against master list
                all_quotes.append(quote)
                new_count += 1
        print(f"🌟 Added {new_count} new quotes | Total: {len(all_quotes)}")
        print()


        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        counting_quotes = len(page.locator(".quote .text").all())
        print(f"Updated Counting of Quotes : {counting_quotes}")
        # print(f"A Non Updated Counting of Quotes {initial_count_quotes}") # I should not Put it Here  


        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        # Understanding These Conditions 
        r'''
        intial_count_quotes are outside of function so it just count the intial Count 
        and if counting_quotes(Inside the While Loop) (Means It Keep Counting at things)

        IF they have the same X amount of Number it means there are no quotes are found 
        What is a good name scrolling_fail --> scrolling_fail_buffer  

        Explaining the If Statement
            if counting_quotes == initial_count_quotes: # If They have the same Number 
                scrolling_fail_buffer += 1 # Adding the Buffering
                print(f"No new quotes found. Fail count: {scrolling_fail_buffer}") # There are no New Quotes are Found 
                if scrolling_fail_buffer == scrolling_max_termination: # if they have the same number of scrolling_max which is 5 after not getting any quotes 
                    break # It will Simply Stop 
            else: # If counting_quotes and initial_count_quotes are not the same number which means there are New Quotes that found 
                scrolling_fail_buffer = 0 # It will Reset the Buffering 
                initial_count_quotes = counting_quotes # Adding a initial_count_quotes # Which means incrementally adding a new quotes in it's memory 
        Basically the code will break or terminate itself if there are no new Quotes are found after 5 retry of getting that Quotes 
        '''
        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        if counting_quotes == initial_count_quotes:
            scrolling_fail_buffer += 1
            print(f"No new quotes found. Fail count: {scrolling_fail_buffer}")
            if scrolling_fail_buffer == scrolling_max_termination:
                break
        else:
            scrolling_fail_buffer = 0
            initial_count_quotes = counting_quotes
            print(f"There are New Quotes Found so It will Reset to: {scrolling_fail_buffer}")
            print(f" New Number for the Comparison counting_quotes and initial_count_quotes not 10 anymore: {initial_count_quotes}")
    
    #||||||||||| Maximum Attempt First Termination |||||||||||
    scrolling_attempt += 1 # Incrementing the Scroll Attempt to 20 Only Maybe i should change the Condition of this 
    
    print("Function: Human_Scrolling_Done")
    print(f"🏁 Finished scrolling. Total unique quotes: {len(all_quotes)}")
    return all_quotes  # Return accumulated results


def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    context = browser.new_context(
        viewport={"width": 1366, "height": 768}  
    )
    page = context.new_page()
    page.goto(base_url)
    # human_scrolling(page)
    # data_extraction(page)
    # data_extraction(page)
    final_quotes = human_scrolling(page)
    print("\n" + "="*50)
    print(f"🔥 FINAL RESULT: Collected {len(final_quotes)} unique quotes")
    print("="*50 + "\n")
    
    # Optional: Save to file
    # with open("quotes.txt", "w", encoding="utf-8") as f:
    #     for i, quote in enumerate(final_quotes, 1):
    #         f.write(f"{i}. {quote}\n")

    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
