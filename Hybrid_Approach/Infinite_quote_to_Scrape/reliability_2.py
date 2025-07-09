from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time


r'''
Solving a Robust Termination 
    Triple Safety Net
        
        
        True bottom detection: scrollY + viewport >= pageHeight - 10px

        1. MAX_ATTEMPTS (15): Absolute scroll limit
        Understanding Why Max Attempt are Needed (Absolute Scroll Limit)
            - This is good so the code will not run forever in attempting things
            - Because Sometimes the Detection Logic fails 
            - how i can use This Information 
            - The Logic of this is putting it right to the bottom of while loop
            - putting it to While loop part  
        2. MAX_FAILS (3): Breaks after no new content
        What it is: A counter of consecutive “failed” scrolls—that is, 
        scrolls after which the page didn’t add any new items.

        Why it helps: Sometimes the site hits an actual end or hiccups: 
        if you scroll three times in a row and nothing new appears, you probably reached the real end.

        # based on My Understanding i needed a metric for this 
            1. Quote Tracking Things 
            2. a Certain Height or the Scroll Position Doesn't Change 
            3. 
            1. Content‑Count Fails (MAX_FAILS)
You’re already tracking .quote count and bailing after N “no‑new‑items” scrolls. This is by far the simplest, most universally applicable check.
Why it matters: Almost every site injects new DOM nodes for each batch of content. If your count doesn’t budge after 2–3 scrolls, you’re almost certainly done.

2. Bottom‑of‑Page Detection (±10 px)
A one‑liner JS check to know “I’m at the very end of the document”:


# Terms of Analyzing the Code There are Too Much Damn Text In Here 
''' 

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
    
    # Old Code While True: 
    # New code a Conditonal for While Loop
    initial_count_quotes = len(page.locator(".quote .text").all())
    while scrolling_attempt_max > scrolling_attempt:
        page.wait_for_load_state("networkidle", timeout=5000)
        prev_scroll_pos = page.evaluate("window.scrollY")
        prev_height_page = page.evaluate("document.body.scrollHeight")
        # print(f"Previous Scroll {prev_scroll_pos} Previous Height {prev_height_page}")
        print()

        page.mouse.wheel(0, 895)
        time.sleep(scroll_pause_time)
        new_scroll_pos = page.evaluate("window.scrollY")
        new_height_page = page.evaluate("document.body.scrollHeight")
        # print(f"New Scroll {new_scroll_pos} New Height {new_height_page}")
        print()

        

        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                print("We Reached the Last Page")
                # break
        # I can add if there are new Height + Content it means the Program will still run What is the stopping point ? 
        r'''
        If there are no new height and i needed a buffer of this 
        Also there are no more content it means we reached the last page 
        '''
        # To see the Results of how many attempt does it take to stop the code
        r'''
        It Certainly Work but the problem is 
        The Length of the Quote that i Currently Scraped: 80
        Previous Scroll 10485.599609375 Previous Height 12702
        New Scroll 11380.7998046875 New Height 12702

        Maybe Adjusting it for the better thing 
        Also i can just use the If Statement for this not in the while thing 
        but i understand the Absolute Limit Attempt
        '''

        # Goal Solve the Problem of Content‑Count Fails (MAX_FAILS)
        r'''
        Creating a Program where it Track if there are new Quotes that are coming in
        and after a 2 - 3 Scrolls and there are no new items it means there are no new content
        ''' 
        r'''
        Analyzing the Selectors 

        # This get all the Quotes from the Top to the Bottom 
        quotes = page.locator(".quote .text").all()
        # Maybe i needed to do this incrementally ? 

        🧠 Core Logic (Step-by-Step)
            1. Track number of .quote elements before and after each scroll.
            # Instead of Getting the Quote for Every While Loop which is very slow 
            # i will use only tracking the number of quotes if there are new 
            What is a good Implementation of this? 
                len() --> quotes = page.locator(".quote .text").all()
                if the number of the quotes doesn't increment it means a fail count 
                if the number of the quotes are loaded reset and fail_count to 0 
                if the fail_count reach the threshold it means max fail 
        It seems like it is outside of the Loop in previous counting 
        I needed to put the counting inside the loop man 
        I also need to reset if there are new quotes how i can do it 
                
        '''

        scrolling_attempt += 1
        # print(f"Scrolling Attempt are {scrolling_attempt}")
        counting_quotes = len(page.locator(".quote .text").all())
        print(f"Updated Counting of Quotes : {counting_quotes}")
        print(f"A Non Updated Counting of Quotes {initial_count_quotes}")

        
        if counting_quotes == initial_count_quotes:
            scrolling_fail += 1
            print(f"No new quotes found. Fail count: {scrolling_fail}")
            if scrolling_fail == scrolling_max:
                break
        else:
            # Resetting it to 0 If the Code is in the False Statement
            scrolling_fail = 0
            initial_count_quotes = counting_quotes
            r'''
            It updates your "reference" quote count to the current total number of quotes after a scroll — but only if new quotes were found.
            ✅ Why is it essential?
Because without it, you're always comparing to the very first quote count (like 10), even after loading more quotes. That means your "new content detection" logic will always say:

“Oh, we’ve got more quotes than before — great! Reset fail count!”

…even if nothing new actually loaded.

This line makes sure you’re always comparing the latest known quote count with the next one after a scroll, like this:
            
            '''
            print(f"There are New Quotes Found so It will Reset to: {scrolling_fail}")
            print(initial_count_quotes)
            
            # break
        # seen_quotes = set()
        # for quote in quotes: 
        #     seen_quotes.add(quote.text_content())
        # length_quote = len(seen_quotes)
        # print(f"The Length of the Quote that i Currently Scraped: {length_quote}") # Total Quote is 100 Thing Using the 100 As Condition seems Bad because it is a fixed Number to
        # print()
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