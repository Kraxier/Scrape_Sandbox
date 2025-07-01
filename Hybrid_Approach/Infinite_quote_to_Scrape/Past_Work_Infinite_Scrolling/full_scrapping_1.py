# python full_scrapping_1.py

r'''Goal: Scrape the Infinte Scrolling Finishing it Up'''
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin


def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=True) 
    page = browser.new_page()
    page.goto(base_url)
    page.wait_for_selector(".quote", state="attached")

    # Extracting the Quote
    # quotes = page.locator(".quote .text").all()
    # quote_count = 0 
    # for quote in quotes: 
    #     print(quote.text_content())
    #     quote_count += 1
    #     print(f"Quote Count: {quote_count}")
    #     print()

    # Alternative for For Loops is while loop but it works so For Optimization maybe there are better way for this but right now i want to get it done 
    # count_loops = 0 
    
    # for x in range(15):
    #     height_page = 0 
    #     count_loops += 1
    #     print(f"Loops Count:{count_loops}")
    #     # Maybe this is where it go wrong 
    #     page.evaluate("window.scrollTo(0, document.body.scrollHeight)") 
    #     # x = page.evaluate("window.scrollTo(0, document.body.scrollHeight)") 
    #     #👉 x will always be None because window.scrollTo() doesn't return anything meaningful (it returns undefined in JavaScript).


    #     new_height = height_page + add_height
    #     page.evaluate("window.scrollTo(new_height, document.body.scrollHeight)")
    #     scroll_height = page.evaluate("document.body.scrollHeight")
    #     page.wait_for_timeout(3000)
    #     print(f"Scroll of the Page Height{scroll_height}")
    # count_loops = 0
    # # This is Basically Scrolling and Storing the Height of the Page
    # scroll_height = page.evaluate("""
    #     () => {
    #             window.scrollTo(0, document.body.scrollHeight);
    #             return document.body.scrollHeight;
    #         }
    # """)
    # page.wait_for_timeout(3000)
    

    # count_loops = 0 
    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    # for x in range(15):
    #     count_loops += 1
    #     scroll_height = page.evaluate("document.body.scrollHeight")
    #     page.evaluate("(scrollPos) => window.scrollTo(scrollPos, document.body.scrollHeight)", scroll_height)
    #     print(f"New Scroll Height{scroll_height}")
    #     print(f"Loops Count:{count_loops}")
    #     page.wait_for_timeout(3000)
    # count_loops = 0
    # initial_height = page.evaluate("document.body.scrollHeight")
    # print(f"Height {initial_height}")
    # while count_loops < 15: # Prevent infinite loops with a max of 15 attempts
    #     count_loops += 1
    #     # Scroll to the bottom
    #     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    #     # Wait for content to load
    #     page.wait_for_timeout(3000)
    
    #     # Get new scroll height
    #     new_height = page.evaluate("document.body.scrollHeight")
    #     print(f"New Scroll Height: {new_height}")
    #     print(f"Loops Count: {count_loops}")

    #     # Stop if no new content loaded (height didn't change)
    #     if new_height == initial_height:
    #         break
            
    #     last_height = new_height
    last_height = page.evaluate("document.body.scrollHeight")
    print(f"🚀 Starting scroll - Initial height: {last_height}px")

    loop_count = 0
    while True:
        loop_count += 1
        print(f"\n🔄 Loop #{loop_count}")
        
        # Scroll to bottom
        print(f"⬇️ Scrolling to current bottom: {last_height}px")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Wait for content
        print("⏳ Waiting 3 seconds for new content...")
        page.wait_for_timeout(3000)  
        
        # Get new height
        new_height = page.evaluate("document.body.scrollHeight")
        print(f"📏 New page height detected: {new_height}px")
        
        # Check if we should stop
        if new_height == last_height:
            print(f"🛑 No height change ({new_height}px == {last_height}px)")
            print("💯 All content loaded - Stopping infinite scroll")
            break
        
        print(f"📈 Height increased by {new_height - last_height}px")
        last_height = new_height

    print("\n✨ Infinite scroll complete!")



    # quotes = page.locator(".quote .text").all()
    # quote_count = 0 
    # for quote in quotes: 
    #     print(quote.text_content())
    #     quote_count += 1
    #     print(f"Quote Count: {quote_count}")
    #     print() 

    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


# Analyzing this 

