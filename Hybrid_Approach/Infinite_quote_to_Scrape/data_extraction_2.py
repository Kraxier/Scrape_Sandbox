
# ======================
# Goal of data_extraction_2.py 
# ======================
r'''
Refactoring the Code 
    1. Breaking the Code in More Readable Format Using the "programming_tips.py" thing 
    2. Understanding the Code While doing it 

To Do List 
1. Focusing in Human Scrolling thing 
2. Fully Breaking Down Data_extraction_1.py Of What things it can do to work on data_extraction_2.py
'''

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time


def extracting_quotes(page):
    r"""
    
    """
    # Collecting the Quotes to store it for saving things 
    collected_quote = []
    # Wait for quotes to be present first to avoid error in terms of loading 
    page.wait_for_selector(".quote .text")
    # Locating the Quotes to Extract it
    quotes = page.locator(".quote .text").all()
    print(f"🎯 Found {len(quotes)} quote elements in current DOM")  # DEBUG
    # For Every Quotes that are Located it will Go to "collected_quote" but it needs to be a strip content first
    for quote in quotes:
        text_content = quote.text_content().strip()  # Get cleaned text

        # In this Code 
        r'''
        ✅ Why this double condition?
            1. It Check 2 conditions 
                * First Condition is if the text_content is not empty to skip the blank quotes that failed to extract properly 
                * Second Conditions is if text_content not in collected_quote which means to avoid duplicate so it check in the list 
        '''
        if text_content and text_content not in collected_quote:  # Check for non-empty and unique
            collected_quote.append(text_content)
            print(text_content)  # Print the actual text
    print(f"📦 Returning {len(collected_quote)} unique quotes from current extraction")
    return collected_quote  # Return the collected data for further use
    # 🔁 What is the return statement? (Going Back to Basics)
    r'''
    The return statement in Python is used to send data back from a function to wherever it was called.

    🧠 Why is it needed?
    Without return, your function might do something, like print to the screen, but it won’t give you any value you can use later.
    '''

# I Wonder if i should Nested the Functions 
#
# ======================
r'''
🔍 What is a nested function?
    A nested function is simply a function defined inside another function.
'''

r'''
💡 Why Use Nested Functions?
    1. Encapsulation (Hiding Logic)
        If the inner fuction is only needed inside the outer fuction nesting keep it hidden from the rest of your 
        program 
        ✅ Cleaner, more readable code
        ✅ Less chance of name conflicts or accidental use elsewhere
    2. Reusability Within a Scope
        If you need to do a small task multiple times inside a bigger task, it makes sense to define a helper function locally.
    3. Closure and Remembering State
        A nested function can "remember" values from the outer function even after the outer function has finished running. This is called a closure.
'''

r'''
⚠️ When Not to Use Nested Functions
    * If the inner function is used in multiple places, define it at the top level instead.
    * Don’t nest too deeply — it can hurt readability.
'''
# ======================

# ======================
r'''
My Reflection in Using a Nested Fuction: 
    I needed to use it because in terms of Scrolling there are things that i needed to do to make it more readable

    1. Position Based Extracting 
        - Extracting Content Based on current scroll position 
        - It focuses on content currently in view or just loaded after a scroll action
        A. Viewport-Centric Extraction:
            * Only extract elements currently visible in the viewport
            * Ignore elements outside the visible area
            * Mimics human reading behavior

    last_position = 0
    while scrolling:
        current_position = get_scroll_position()
        if current_position > last_position:
            extract_new_items_since(last_position)
            last_position = current_position
        
    2. There are Multiple Terminations 
        * If there are no New Quotes that the Locator gather 
        1. Maximum Attempt Termination
            Trigger: Reaching the predefined maximum scroll attempts (scrolling_attempt_max = 20).
        2. Stagnant Content Termination
            : Failing to detect new quotes for 5 consecutive scrolls (scrolling_max = 5).
            Terminates when: No new quotes appear in 5 consecutive scroll cycles
    4. Chunked Scrolling with Variable Pauses (20% Solution)
        Never scroll full page at once
        Vary scroll distance and speed
        Exponential pauses between chunks
    5. Pre-Action Delays (The 50% Solution) (This is Outside in scrolling function)
    Insert before EVERY interaction (click, type, etc.)
    Why it matters: Bots act instantly, humans hesitate
    Implementation: pre_action_delay() before every action
'''

r'''
Practising the Habit of 
    1. Code for Readability and Maintanability 
        - Using Meaninful Names
        - Keep Functions Small and Focused (Applying Single Responsibility of Function)
        - Avoding Deep Nesting 
        - Consistent Formating 
        - Comment Why, Not What 

Workflow and Proccess Habits 
    1. Break Down the Task 
    2. Estimate Realisticlly 
        Provide Rational Behind Estimates
    3. DocumentProactively - •	Maintain clear README
    4. Master your Tools Learning IDE, Debugger, Terminal, And Profiler
        - Picking an IDE 

Personal Development and Habits
    1. Continous Learning 
        - Dedicating Time Learning 
        - Read Watch Build and Experiment 
    2. Embrace Feedback and Failure 
        - Mistake as Learning Opportuintes 
    3. Know when to ASk for Help 
        - Try on your Own 
        - Ask with Context showing what you tried 
    4. Taking a Break and Step Away 
        - To Solve Tough Problems a Pomodoro Technique Optimizing for Focused and Difuse Mode
    5. 


        
'''

# ======================
def scrolling(page):
    r'''
    How the Bot Scroll 
        1. 
    '''
    page.wait_for_selector(".quote", state="attached") # Wait for the Content to Load 
    # Debugging Purposes Finding the Initial Height of Things 
    # initial_height_page = page.evaluate("document.body.scrollHeight")
    # initial_scroll_pos = page.evaluate("window.scrollY")
    # print(f"Initial Scroll Positon of the Page is {initial_scroll_pos} and Initial Height Positon of the Page is {initial_height_page} ")
    # initial_count_quotes = len(page.locator(".quote .text").all())


    # Max Scrolling Attempt 
    r'''
    Why i Put Max Scrolling Attempt? 
        To stop the Program in Scrolling if it Reach a 10 Maximum 
        When will it return to 0 when Scrolling Attempt keeps counting ? 
            If There are no Quotes 
    '''
    scrolling_attempt_max = 10 # For a Function maximum_termination
    scrolling_attempt = 0 # For a Function maximum Termination 


    def position_based_extracting(page):
        pass
    # def maximum_termination(page):
    #     r'''
    #     In This Part i want to Return False if the Page is Reach 10 Attempt Scrolling at Things the Maximum Part
    #     Abondoinig the Idea of Putting a function for a maximum attempt because i can just put it in the while loop Part 
    #     '''
    #     pass
    def stagnant_content_termination(page):
        pass
    pass