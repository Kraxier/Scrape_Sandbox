# Learning to Data Exxtraction in terms of Position Based and Also Adding the Human Delay in the Proccess 
r'''
Extracting the Scroll
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
    # data_extraction(page)
    # data_extraction(page)
    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)