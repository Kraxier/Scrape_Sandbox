
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time


delay_profiles = {
    "pre_click": (1.2, 3.5),    # Decision-making before action
    "post_click": (0.1, 0.4),   # Natural reaction after click
    "scroll": (0.2, 1.5),       # Reading time during scroll
    "typing": (0.08, 0.15),     # Per-key typing speed
    "page_load": (0.8, 4.0),    # "Reading" after navigation
    "think": (3.0, 8.0)         # Strategic pauses
}


def human_delay(context: str) -> None:
    """Delay based on behavioral context"""
    min_time, max_time = delay_profiles[context]
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

def data_extraction(page):
    quote_item = []
    page.wait_for_selector(".quote .text")  
    quotes = page.locator(".quote .text").all() 
    # print(f"🎯 Found {len(quotes)} quote elements in current DOM")  
    for quote in quotes: 
        text_content = quote.text_content().strip()  
        if text_content and text_content not in quote_item: 
            quote_item.append(text_content) 
            # print(text_content) 
    # print(f"📦 Returning {len(quote_item)} unique quotes from current extraction")
    return quote_item 


def human_scrolling(page):
    all_quotes = []  # Master collection list
    page.wait_for_selector(".quote", state="attached") #  Wait for the first Quote to Attached in the Page 
    initial_height_page = page.evaluate("document.body.scrollHeight") # Getting the Initial Height of the Page 
    initial_scroll_pos = page.evaluate("window.scrollY") # Getting the Initial Scroll Position of the Page 
    # print(f"Initial Scroll Positon of the Page is {initial_scroll_pos} and Initial Height Positon of the Page is {initial_height_page} ") # Printing Things 
    print()
    print()

    #||||||||||| Maximum Attempt First Termination |||||||||||
    scrolling_attempt_max = 20 
    scrolling_attempt = 0 
    scroll_pause_time = 2  


    #||||||||||| Second Termination: Counting The Quotes |||||||||
    initial_count_quotes = len(page.locator(".quote .text").all()) 
    scrolling_max_termination = 5
    scrolling_fail_buffer = 0

    while scrolling_attempt_max > scrolling_attempt:
        # |||||||||||  Third Termination |||||||||||
        page.wait_for_load_state("networkidle", timeout=5000) 

        # |||||||||| Mimicing Human Behaviour Through Scrolling |||||||||||

        # ||||||||||| Scroll Amount |||||||||||
        # Creating a Range for scrolling
        scrolling_profiles = {
        "scroll_magnitude":(200.0, 768.0), # Scroll Magnitude right to the max for range
        "scroll_timing": (0.2, 1.5),
        "scroll_think": (3.0, 8.0)
        }
        # Why? For 80% Maximum Scrolling Thing 
        viewport_height = page.viewport_size["height"] 
        r'''
        Results of Debug is Always at 768px
        '''
        min_px, max_px = scrolling_profiles["scroll_magnitude"]
        scroll_amount_px = random.uniform(min_px, max_px)
        max_scroll = viewport_height * 0.8
        # scroll_amount_px is randomize between 200 - 768 but 769 is the maximum
        # Changing the Dictionary part relative to the viewport
        scroll_amount = min(scroll_amount_px, max_scroll) # The min() function ensures the actual scroll distance (scroll_amount) never exceeds max_scroll.
        page.mouse.wheel(0, scroll_amount)  # Correct: (delta_x=0, delta_y=scroll_amount)
        print(f"Viewport height: {viewport_height}px") # Viewport height: 768px

        # ||||||||||| Time Delay for Every Scroll |||||||||||
        min_scroll_delay, max__scroll_delay = scrolling_profiles["scroll_timing"] # For Short Term Scrolling 
        min_scroll_think, max_scroll_think = scrolling_profiles["scroll_think"] # For Longer Interval of Thinking 
        time_delay = random.uniform(min_scroll_delay, max__scroll_delay)
        print(f"Time Delay: {time_delay}secods")
        time.sleep(time_delay)
        # 25% Chance a Long Pause for Thinking 
        if random.random() < 0.25:  # 25% chance
            think_min, think_max = scrolling_profiles["scroll_think"]
            time_delay_long = random.uniform(think_min, think_max)
            print(f"Long Thinking Scrolling {time_delay_long}seconds")
            time.sleep(time_delay_long)
            # time.sleep(random.uniform(think_min, think_max))

        # ||||||||||| Scroll Amount Going up for 30% Chance |||||||||||
        direction = 1  # Default down
        if random.random() < 0.3:  # 30% chance to scroll up
            direction = -1
            print(f"Scrolling Up (30% Chance)")
        scroll_amount *= direction
        page.mouse.wheel(0, scroll_amount)

        # |||||||||| Mimicing Human Behaviour Through Scrolling |||||||||||


        prev_scroll_pos = page.evaluate("window.scrollY")
        prev_height_page = page.evaluate("document.body.scrollHeight")
        # print()


        # |||||||||||  Third Termination |||||||||||

        new_scroll_pos = page.evaluate("window.scrollY")
        new_height_page = page.evaluate("document.body.scrollHeight")

        if new_height_page == prev_height_page:
            if new_scroll_pos == prev_scroll_pos:
                # print("We Reached the Last Page")
                # break
                pass

        #||||||||||| Analyze Data Extraction |||||||||||
        current_quotes = data_extraction(page)  
        # print(f"🔄 Received {len(current_quotes)} quotes from extraction") 


        new_count = 0
        for quote in current_quotes:
            if quote not in all_quotes: 
                all_quotes.append(quote)
                new_count += 1
        # print(f"🌟 Added {new_count} new quotes | Total: {len(all_quotes)}")
        # print()


        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        counting_quotes = len(page.locator(".quote .text").all())
        # print(f"Updated Counting of Quotes : {counting_quotes}")
        # print(f"A Non Updated Counting of Quotes {initial_count_quotes}") # I should not Put it Here  


        #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        if counting_quotes == initial_count_quotes:
            scrolling_fail_buffer += 1
            # print(f"No new quotes found. Fail count: {scrolling_fail_buffer}")
            if scrolling_fail_buffer == scrolling_max_termination:
                break
        else:
            scrolling_fail_buffer = 0
            initial_count_quotes = counting_quotes
            # print(f"There are New Quotes Found so It will Reset to: {scrolling_fail_buffer}")
            # print(f" New Number for the Comparison counting_quotes and initial_count_quotes not 10 anymore: {initial_count_quotes}")
    
    #||||||||||| Maximum Attempt First Termination |||||||||||
    scrolling_attempt += 1 # Incrementing the Scroll Attempt to 20 Only Maybe i should change the Condition of this 
    
    # print("Function: Human_Scrolling_Done")
    # print(f"🏁 Finished scrolling. Total unique quotes: {len(all_quotes)}")
    return all_quotes  


def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    context = browser.new_context(
        viewport={"width": 1366, "height": 768}  
    )
    page = context.new_page()
    page.goto(base_url)

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
