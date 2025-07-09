from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time

def human_scrolling(page):
    page.wait_for_selector(".quote", state="attached")
    initial_height_page = page.evaluate("document.body.scrollHeight")
    initial_scroll_pos = page.evaluate("window.scrollY")
    # print(f"Initial Scroll Positon of the Page is {initial_scroll_pos} and Initial Height Positon of the Page is {initial_height_page} ")
    print()

    scroll_pause_time = 2  
    scrolling_attempt_max = 20
    scrolling_attempt = 0

    # Understanding the Max Fails Accounts 
    r'''
    initial_count_quotes = len(page.locator(".quote .text").all()) 
    Initial Count Quotes will Always be 10

    I also Declare max and Fail Thing 

    Inside the Loop 
        # Declaring this so if the Loop keep looping or scrolling it will always get the update of the len of the Quotes
        counting_quotes = len(page.locator(".quote .text").all())

    # The Question is why this ? 

    if counting_quotes == initial_count_quotes:
        scrolling_fail += 1
        print(f"No new quotes found. Fail count: {scrolling_fail}")
        print(f"Observing the Updated Count of Quotes {counting_quotes} and the Initial {initial_count_quotes}")

    # After Observing the Relationship between counting_quotes and initial_count_quotes why the initial count quotes are still the same 
    Observing the Updated Count of Quotes 60 and the Initial 60 
    # This is because of Else Statement 
        In terms of While Loop The Variable or the memory inside the loop are changing things depends on the function of that variable 

    Basically in the "Else" Statement if counting_quotes == initial_count_quotes are not Equal which Mean "False" 
        The initial_count_quotes = counting_quotes So basically the Initial_count_quotes will keep up in the counting_quotes again 
            Like if there are 20 Quotes in Initial and there are new Update in Counting Quotes so basically declaring it to keep up for the condition of things

    The Determinator of Breaking Point is Scrolling Max and Fail like if there are no new quotes 
    '''
    scrolling_max = 5
    scrolling_fail = 0
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

        scrolling_attempt += 1
        # print(f"Scrolling Attempt are {scrolling_attempt}")
        counting_quotes = len(page.locator(".quote .text").all())
        # print(f"Updated Counting of Quotes : {counting_quotes}")
        # print(f"A Non Updated Counting of Quotes {initial_count_quotes}")

        
        if counting_quotes == initial_count_quotes:
            scrolling_fail += 1
            print(f"No new quotes found. Fail count: {scrolling_fail}")
            print(f"Observing the Updated Count of Quotes {counting_quotes} and the Initial {initial_count_quotes}")
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