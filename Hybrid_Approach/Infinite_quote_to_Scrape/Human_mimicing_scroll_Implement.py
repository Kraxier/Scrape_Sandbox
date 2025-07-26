from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
# 

# I think i did a good Work and Now the Integrating Part of this 

# I think I should not put the "scrolling pixel"
delay_profiles = {
    "pre_click": (1.2, 3.5),    # Decision-making before action
    "post_click": (0.1, 0.4),   # Natural reaction after click
    "scroll": (0.2, 1.5),       # Reading time during scroll
    "typing": (0.08, 0.15),     # Per-key typing speed
    "page_load": (0.8, 4.0),    # "Reading" after navigation
    "think": (3.0, 8.0),         # Strategic pauses
    "scrolling_pixel": (200.0, 895.0)
}

def human_scrolling(page):
    # Get the Viewport Size: 
    # Why: it Will Depend on that in Overscrolling and the "px" in term of scroll
    # page.set_viewport_size({"width": 1280, "height": 720})
    viewport_height = page.viewport_size["height"]
    print(f"Viewport height: {viewport_height}px")

    # Creating a Range for scrolling
    scrolling_profiles = {
        "scroll_magnitude":(200.0, 895.0),
        "scroll_timing": (0.2, 1.5),
        "scroll_think": (3.0, 8.0)
        }
    min_px, max_px = scrolling_profiles["scroll_magnitude"]
    min_scroll_delay, max__scroll_delay = scrolling_profiles["scroll_timing"]
    min_scroll_think, max_scroll_think = scrolling_profiles["scroll_think"]
    scroll_amount = random.uniform(min_px, max_px)

    # Debugging 
    # print(f"")
    # print(f"Minimum Scroll Amount: {min_px} and Maximum Scroll Amount: {max_px}") # No need to Print this, it is in the dictionary "Random Uniform is the Key a Single Value"
    print(f"Scroll Amount {scroll_amount}")
    # print(f"Mininum Scroll Delay: {min_scroll_delay} and Maximum Scroll Delay: {max__scroll_delay}")# No need to Print this, it is in the dictionary "Random Uniform is the Key a Single Value"
    print(f"")

    # page.mouse.wheel Should be a random stuff
    page.mouse.wheel(viewport_height, scroll_amount)
    # 
    time_delay = random.uniform(min_scroll_delay, max__scroll_delay)
    print(f"Time Delay: {time_delay}secods")
    time.sleep(time_delay)
    r'''
    Results are: 
    Scroll Amount 726.1178674183867
    Viewport height: 768px
    Does this means that i will not overscroll? 
    '''

    # in terms of Percent Chance of Getting things through 
    r'''
    🔄 Phase 4: Human-like Patterns
    Implement random direction (up/down)
    '''
    r'''
    direction = 1 Code Explanation
    This sets the initial scroll direction to 1, which typically represents scrolling downward
    '''
    direction = 1  # Default down

    r'''
    if random.random() < 0.3:  # 30% chance to scroll up
        direction = -1
    
    random.random() returns a random float between 0.0 and 1.0.

    This line introduces a 30% chance that direction will be changed to -1, which usually represents scrolling upward.

    So, there’s a random decision:
        70% of the time → direction stays as 1 (scroll down)
        30% of the time → direction changes to -1 (scroll up)
    '''
    if random.random() < 0.3:  # 30% chance to scroll up
        direction = -1
        print(f"There are 30% Scrolling Up")
    
    r'''
    This multiplies the value of scroll_amount by direction.

    If direction == 1, the scroll amount remains positive → scrolls down.

    If direction == -1, the scroll amount becomes negative → scrolls up.
    '''
    scroll_amount *= direction
    # Scroll Amount has Been Used in the Very Top 
    page.mouse.wheel(0, scroll_amount)

    r'''
    Notes for "page.mouse.wheel" 
    The page.mouse.wheel(x, y) method scrolls both vertically (y) and horizontally (x)
        * A positive y value scrolls down
        * A negative y value scrolls up
    Think of y as the direction your mouse wheel is turned:
        * Scrolling down with the mouse → y is positive
        * Scrolling up with the mouse → y is negative

    ✅ Example
    page.mouse.wheel(0, 300)   # Scrolls down 300px
    page.mouse.wheel(0, -300)  # Scrolls up 300px

    scroll_amount = 300
    scroll_amount *= direction  # Now scroll_amount = -300
    page.mouse.wheel(0, scroll_amount)

    '''
    # 25% Chance a Long Pause for Thinking 
    if random.random() < 0.25:  # 25% chance
        think_min, think_max = delay_profiles["think"]
        time.sleep(random.uniform(think_min, think_max))

    # Next Step is 🚀 Phase 6: Optimization and 📊 Phase 7: Final Polish

    # Phase 6 Optimization: 
    
    # Limit max scroll to 80% of viewport
    # Get the "view_portheight" and times the 0.8 which is 80% of the viewport thing 
    # that 80% is the Max Scrolling i should do this earlier part of my stuff stupid me
    max_scroll = viewport_height * 0.8
    scroll_amount = min(scroll_amount, max_scroll)

    # Jumping to 📊 Phase 7: Final Polish
    # Adding Logging for Debugging


    # Next Step is Integrate it at Data Extraction Part 

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

    # quotes = page.locator(".quote .text")
    # quotes_text = page.locator(".quote .text").text_content()
    #quotes_text = page.locator(".quote .text").all_text_contents()
    #print(f"This is the first one {quotes}")
    #print(f"This is the all text content {quotes_text}")

    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



# Concept of Debugging and Logging for Software Engineering and Programming 

# What is Debugging? 

r'''
🔍 Debugging
Debugging is the process of finding and fixing bugs (errors or flaws) in software code. It usually involves:
    Identifying where and why something is going wrong.
    Inspecting variable values, execution flow, and logic.
    Correcting the code to remove the problem.

🛠 How Debugging is Done:
Using a debugger tool (like those in Visual Studio, PyCharm, or Chrome DevTools) to:
    Set breakpoints (pause the program at a specific line).
    Step through code line by line.
    Inspect variables and memory.
    Check the call stack (history of function calls).
'''

# What is Logging? 
r'''
📜 Logging
Logging is the process of recording events or messages that happen while a program runs, usually to a file, console, or logging service.

📋 Why Logging is Useful:
    * Helps track the behavior of the application in real time or after a crash.
    * Useful in production environments where debugging tools are not available.
    * Helps in monitoring and troubleshooting without interrupting the running program.

🧩 Typical Logging Information:
    * Errors and exceptions.
    * Start/finish of operations.
    * User actions.
    * System events (e.g., database connections).
'''

# My Reflection: 
r'''
I can do Debugging if i want to integrate it in "data_extraction_analyzing"

But i can do Logoging 
    just by "print()" and i been doing that to see whether my program is working 

Basically to Monitor Things out 
'''