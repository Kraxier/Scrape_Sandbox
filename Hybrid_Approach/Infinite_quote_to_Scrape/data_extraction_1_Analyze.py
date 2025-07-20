
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time


# Second Version of data_extraction(page):
def data_extraction(page):
    quote_item = []
    # Wait for quotes to be present first
    page.wait_for_selector(".quote .text")
    
    quotes = page.locator(".quote .text").all()
    print(f"🎯 Found {len(quotes)} quote elements in current DOM")  # DEBUG
    for quote in quotes:
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


    #||||||||||| Maximum Attempt First Termination |||||||||||
    # Used in While Loop for the Condition to be True {Scrolling_attempt_max and scrolling_attempt}
    # Why: We Used Scrolling Attempt Max to not keep Scrolling Forever so we terminate the program once it reaches the maximum attempt
    # Problem: It Will Always Increment at the end of the Loop the Problem is, it will not go back to 0 so Just a Maximum Attempt of Scroll only

    #||||||||||| Maximum Attempt First Termination |||||||||||
    scrolling_attempt_max = 20 # How many are the Max Scrolling 
    scrolling_attempt = 0 # How many Attempts that it Scrolls 

    
    
    scroll_pause_time = 2  
    scrolling_max = 5
    scrolling_fail = 0

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
        current_quotes = data_extraction(page)  # Store return value
        print(f"🔄 Received {len(current_quotes)} quotes from extraction")

        # Track new unique quotes
        # new_count = 0
        # for quote in current_quotes:
        #     if quote not in all_quotes:  # Check against master list
        #         all_quotes.append(quote)
        #         new_count += 1
        # print(f"🌟 Added {new_count} new quotes | Total: {len(all_quotes)}")
        # print()

        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                print("We Reached the Last Page")
                # break
        
        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        counting_quotes = len(page.locator(".quote .text").all())
        print(f"Updated Counting of Quotes : {counting_quotes}")
        # print(f"A Non Updated Counting of Quotes {initial_count_quotes}") # I should not Put it Here  


        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        # Understanding These Conditions 
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
