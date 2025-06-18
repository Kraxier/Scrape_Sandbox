# python implement_pareto_2.py

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin


def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=True) 
    page = browser.new_page()
    page.goto(base_url)

    # _________________________ Old Version of Code _________________________
    # i = 1 
    # page.wait_for_selector(".quote", state="attached")
    # full_height = page.evaluate('document.body.scrollHeight')
    # print(f"First Height of the page:{full_height}")
    # for _ in range(25):
    #     print(i)
    #     i += 1
    #     updating_height = page.evaluate('document.body.scrollHeight')
    #     print(f"Updating the Height:{updating_height}")
    #     page.mouse.wheel(0, full_height)
    #     page.wait_for_timeout(2000)


    # _________________________ New Version of Code  V1 _________________________

    page.wait_for_selector(".quote", state="attached") # Wait the Page to Load 
    quote_count = len(page.query_selector_all(".quote")) # Counting the Quotes
    print(f"New Count for the Quote of the Page:{quote_count}")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
   

    # I need Detection for the New Content 
    new_height = page.evaluate("document.body.scrollHeight")
    page.wait_for_selector(".quote", state="attached")
    print(f"New Height of the Page:{new_height}")
    # ____________________ First Version of Waiting ____________________ 
    page.wait_for_timeout(3000) # brief pause for content to load

    # ____________________ Second Version of Waiting ____________________
    # page.wait_for_function("""() => {
    # const count = document.querySelectorAll('.quote').length;
    # return count > 10;  // wait until count increases
    # }""") 

    quote_count = len(page.query_selector_all(".quote")) # Counting the Quotes
    print(f"New Count for the Quote of the Page:{quote_count}")
    r'''
    Improved Drastically in Counting Quotes  
    New Count for the Quote of the Page:10
    New Height of the Page:1616
    New Count for the Quote of the Page:100

    '''



    input("Press Enter to Stop the Program ")
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



# Scroll Mechanism
# Use page.evaluate() to scroll to absolute bottom:
# $ page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
# Why better than mouse wheel? Guarantees reaching bottom regardless of screen size


# Content Loading Detection

# Option A: Height comparison
# new_height = page.evaluate("document.body.scrollHeight")
# if new_height == last_height:
#     break

# Option B: Wait for new elements (more precise)
# quote_count = len(page.query_selector_all(".quote"))
# page.wait_for_function(
#     f"{quote_count} < document.querySelectorAll('.quote').length",
#     timeout=5000
# )

# Dynamic Waiting
# Hybrid approach (recommended):
# try:
#     page.wait_for_selector(".quote >> nth=-1", state="attached", timeout=3000)
# except:
#     # Fallback to height check
#     if page.evaluate("document.body.scrollHeight") == last_height:
#         break
# Termination Conditions
# Exit when:
# Content stops loading (height stabilizes)
# Maximum attempts reached (safety net)
# New elements fail to appear




# Notes:

r'''
page.wait_for_selector(".quote", state="attached")
Waits until at least one element with class "quote" is present in the DOM

len(page.query_selector_all(".quote"))
Counts how many elements with class "quote" exist on the page

.query_selector_all() is similar to JavaScript's 
document.querySelectorAll() - it finds all elements matching the CSS selector
It's a Playwright/Puppeteer method that finds all elements matching a CSS selector (like .quote)
Returns a list of elements, and len() count


page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
this uses the document's full height rather than fixed pixels


Does counting and scrolling mean another page like a next button?
Deepseek: said no because this is infinite scrolling thing 
    Counting quotes on the same page that expand as you scroll so basically it should increase

My Code both count 10 becayse 
    No Content Loaded Yet and i needed to wait 
    Or needed to scroll Multiple Times to trigger loading 
'''


#______________________ Comparison in Terms of Waiting Part  ______________________

# page.wait_for_timeout(1000)
r'''
What it does: Pauses execution for exactly 1000 milliseconds (1 second)
PROS: Quick to Use and Simple for Debugging Things 
CONS: Fixed Wait Time (Might be Too short or too long)
        Can Waste Time if the Content Load Faster
        Might Fail if it take Longer than 1 Seconds 
'''
# page.wait_for_function()

r'''
What it does: Actively polls the page until the JavaScript function returns true
Pros: 
    Wait as long exactly are needed
    More Reliable if your Condition are met but won't proceed until condition ismet 
    Efficient 
    Better for Dynamic Content 
Cons:
    Complex to Write 
    Might Timeout if Condition never met
'''
# page.wait_for_function("""() => {
#     const quotes = document.querySelectorAll('.quote');
#     return quotes.length > 10;  // Only continue when we have >10 quotes
# }""")


# Test Result Between wait_for_timeout(3000): vs wait_for_function():


r'''
wait_for_timeout(3000)
First count: 10 quotes
After scroll + 3 second wait: 100 quotes
This worked better in your case because:
    The page needed a full 3 seconds to load all content
    The fixed wait allowed all background API calls/rendering to complete

wait_for_function():
First count: 10 quotes
After scroll + conditional wait: Only 20 quotes
This underperformed because:
    The condition quotes.length > 10 was satisfied too early (at 20 quotes)
    The function stopped waiting as soon as ANY new content appeared

wait_for_function() exits at the first truthy result
wait_for_timeout() gives the page full time to load everything

You Can Combine Both for Testing Thing 


wait_for_function() is better for:
    Ensuring minimum content exists
    Stable DOM elements
wait_for_timeout() is better for:
    Allowing background processes to complete
    When you know approximate load times
For infinite scroll:
    First verify new content exists (conditional wait)
    Then allow time for full batch loading (timeout)
    May need multiple scroll+wait cycles for all content

'''