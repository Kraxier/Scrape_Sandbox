# This is for Scroll Stuff in Core 
# venv_PS_Toscrape\Scripts\activate

from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import time  # For demonstration purposes

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)  # Added slow_mo to see actions better
    page = browser.new_page()
    
    # Set viewport to a smaller size to make scrolling more noticeable
    page.set_viewport_size({"width": 800, "height": 600})
    
    page.goto(base_url)
    
    # Wait for page to load completely
    page.wait_for_selector(".quote", state="attached")
    
    # Verify scrolling works by checking positions before/after
    initial_pos = page.evaluate("window.scrollY")
    print(f"Initial scroll position: {initial_pos}")
    
    # Scroll down 100 pixels - now with visible feedback
    print("Scrolling down 100 pixels...")
    page.mouse.wheel(0, 100)
    # time.sleep(1)  # Pause to see the effect
    
    new_pos = page.evaluate("window.scrollY")
    print(f"New scroll position: {new_pos}")
    
    # # More dramatic scroll to see the effect clearly
    # print("Scrolling down 500 pixels...")
    # page.mouse.wheel(0, 500)
    # time.sleep(1)
    
    # # Scroll to specific element
    # target = page.locator(".quote").last
    # target.scroll_into_view_if_needed()
    # print("Scrolled to last quote element")
    # time.sleep(1)
    
    # # Your scraping code would go here
    # quotes = page.locator(".quote .text").all()
    # for i, quote in enumerate(quotes[:3]):  # Just show first 3 for demo
    #     print(f"Quote {i+1}: {quote.text_content()}")
    
    # # Answering your questions about page.evaluate() and DOM manipulation
    # print("\n=== JavaScript Execution Examples ===")
    
    # # 1. Execute JavaScript in page context
    # title = page.evaluate("document.title")
    # print(f"Page title via JS: {title}")
    
    # # 2. Manipulate the DOM - change background color temporarily
    # page.evaluate("""() => {
    #     document.body.style.backgroundColor = 'lightblue';
    #     setTimeout(() => {
    #         document.body.style.backgroundColor = '';
    #     }, 1000);
    # }""")
    # print("Changed background color for 1 second")
    # time.sleep(2)
    
    # # 3. More complex DOM manipulation
    # page.evaluate("""() => {
    #     const quotes = document.querySelectorAll('.quote');
    #     quotes.forEach(q => q.style.border = '2px solid red');
    # }""")
    # print("Added red borders to all quotes")
    # time.sleep(2)
    
    # input("Press Enter to close the browser...")
    # page.close()
    # browser.close()

with sync_playwright() as playwright:
    run(playwright)



r'''
Why my Code Doesn't work? 

1. View Port Size:
    Viewport size can be fullscreen or big that it barely noticeable 
Solution: Smaller viewport means the same scroll distance represents a larger percentage of the visible area

2. Explicit Waiting 
    I needed a verification whether the state of the website is fully loaded or not 
    for example: $ page.wait_for_selector(".quote", state="attached")
    I attempt to scroll the website without fully loaded 
3. Slow Motion mode:
    I needed to slowdown to see wether the action work or not additional 
    information for headless False or True
    $ browser = chromium.launch(headless=False, slow_mo=500)
4. Verifying whether the scroll position worked 
    $ initial_pos = page.evaluate("window.scrollY")
    # ... scroll happens ...
    $ new_pos = page.evaluate("window.scrollY")

'''


r'''
page.mouse.wheel() 80% Result for 10% Use Thing 

# 1. Scroll to trigger lazy-loaded content
page.mouse.wheel(0, 500)  # Scroll down 500px

# 2. Scroll to bottom in increments
for _ in range(5):
    page.mouse.wheel(0, 1000)
    page.wait_for_timeout(1000)  # Wait for content to load

# 3. Scroll specific element into view
element = page.query_selector('.target')
box = element.bounding_box()
page.mouse.wheel(0, box['y'] - 200)  # Scroll to position above element

# 4. Horizontal scrolling (for rare cases)
page.mouse.wheel(300, 0)  # Scroll right 300px
'''


r'''
page.wait_for_function() - The 10% that handles 90% of waiting needs
# 1. Wait for content to load after scroll
page.mouse.wheel(0, 1000)
page.wait_for_function('''() => {
   #  return document.querySelectorAll('.item').length > 10
}''')

# 2. Wait for AJAX completion
page.wait_for_function('''() => {
    # return window.dataLoaded === true
}''')

# 3. Wait for scroll position
page.mouse.wheel(0, 1500)
page.wait_for_function('window.scrollY > 1000')

# 4. Wait for element state change
page.wait_for_function('''() => {
   #  const el = document.querySelector('.status');
    # return el && el.innerText.includes('Complete');
}''')
'''
