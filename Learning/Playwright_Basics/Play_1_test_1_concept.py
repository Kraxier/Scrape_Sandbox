r'''
Concetps 

1. What is Sync?
🔁 Sync (Synchronous)
    Code runs line by line, one after another.
    You don't need async or await keywords.
    Easier for beginners to use.

2. What is Async?
⚡ Async (Asynchronous)
    Code uses async and await to handle tasks that can run in the background (non-blocking).
    More efficient for concurrent tasks (e.g. scraping multiple pages).
    You must run the code inside an async def function and use an event loop.


Question: Is there are Difference or Advantage and Disadvantage in Switching a Browser specifically Focus on Web Scrapping?

Browser	    
🛠️Chromium	
    - Fastest
    - Best compatibility
    - Most stable for automation	
    - Slightly heavier on memory
🛠️Firefox	
    - Good for sites that detect Chromium-based browsers
    - Different JS engine (Gecko)	
    - Slower than Chromium in some cases
🛠️WebKit (Safari's engine)	
    - Useful for testing Safari-specific behavior
    - Lightweight	
    - Least compatible with modern JS/CSS
    - Some sites may break

1. My Question is If the HTML and CSS are also same in terms of Different Browser? 
🧠 Use the same browser as the target audience — Most sites are optimized for Chrome.
APIs and JavaScript behavior are mostly the same across browsers — but not guaranteed to be identical.
HTML and CSS are mostly the same across different browsers, but not always in how they are rendered or interpreted.
'''


def run(playwright: Playwright):
# Defines a function called run that takes a Playwright instance as a parameter
# The type hint : Playwright indicates the parameter should be a Playwright object
r'''Question is What does it mean by "Playwright Object" '''
r'''Answer: 
    The Playwright object is the main entry point to control browsers in Playwright. It's essentially a "manager" that gives you access to:
        Different browser engines (chromium, firefox, webkit)
        Methods to launch and manage browsers
        Network emulation, device simulation, and other automation features
'''

    chromium = playwright.chromium # or "firefox" or "webkit".
    # Accesses the Chromium browser instance from the Playwright object
    # You could alternatively use playwright.firefox or playwright.webkit for other browsers
    # The comment shows you could use other browser engines if desired

    browser = chromium.launch() # Launches a new browser instance (Chromium in this case) and This starts up a headless browser by default (no visible UI)
    # browser = chromium.launch(headless=False)  # Opens a visible browser
    # browser = chromium.launch(headless=True)  # close a visible browser
    r'''Question: Is there are Difference in terms of Performance when running it with visible UI or is it easy to debug things if i can see it?'''
    r'''Answer: 
        ⚡Headless (Default) # browser = chromium.launch(headless=True) For Performance
            - Faster (no UI rendering)
            - Less RAM/CPU usage
            - Harder to debug (you don't see what's happening)
        ⚡Headful (Visible UI) # browser = chromium.launch(headless=False)
            - Slightly slower (renders graphics)
            - Easier to debug (you can see clicks, navigation, errors)
    '''
    page = browser.new_page() # Creates a new tab/page in the browser # This starts up a headless browser by default (no visible UI)
    r'''Question: Does this means i can multiple open new tab page so i can do "Async" '''
    r'''Answer: 
        Yes! Playwright allows multiple tabs (even across multiple browsers).
        Option 1: Multiple Tabs in Same Browser eg:
            page1 = browser.new_page()  # Tab 1
            page2 = browser.new_page()  # Tab 2
            page1.goto("https://example.com")
            page2.goto("https://google.com")
        * Pros: Lightweight (shares same browser process).
        * Cons: If one tab crashes, it may affect others.

        Option 2: Multiple Browsers (True Parallelism) eg:
            browser1 = chromium.launch()
            browser2 = chromium.launch()
            page1 = browser1.new_page()
            page2 = browser2.new_page()
        * Pros: Isolated sessions (more stable).
        * Cons: Higher RAM/CPU usage.

        Playwright supports async (playwright.async_api) for true concurrency. # What does it mean by Concurrency? 
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto("https://example.com")
        
        What does it mean by Concurrency? 
        In Playwright, concurrency refers to the ability to run multiple browser tasks at the same time, rather than one after the other (sequentially).
        When it says Playwright supports async_api for true concurrency, it means you can launch and control multiple browser contexts, pages, or actions at once — 
        without waiting for each one to finish before starting the next.

        Difference between Concurrency and Parallelism 
        Concurrency = Tasks start independently and progress together (e.g., async/await).
        Parallelism = Tasks run on multiple threads or CPUs at the exact same time (e.g., multiprocessing).


    '''
    page.goto("https://quotes.toscrape.com/")
    # other actions... or output of an actions 
    # A comment indicating where you might add additional actions like clicking elements, filling forms, etc.
    print(page.title()) # Print the Title of the website 

    browser.close() # Important for cleaning up resources, Closes the browser and all its pages (tabs)

# An Actual Execution from the Top 
with sync_playwright() as playwright:
    run(playwright)

# Screenshot things 
r'''Produce a Screenshot the Problem is the Scrolling Part So that is a Challenge Man but It Works '''
# from playwright.sync_api import sync_playwright

# playwright = sync_playwright().start()

# browser = playwright.chromium.launch()
# page = browser.new_page()
# page.goto("https://playwright.dev/")
# page.screenshot(path=r"C:\Users\klabi\OneDrive\Desktop\Learn_Dynamic_Jascript\Playwright\example.png")
# browser.close()

# playwright.stop()


r'''
                                                                        Fix This Part

😊 Positive Vibes:
🙌 🎉 😄 🥳 🤗 ✨ 💫 😎 💖 🌈

🔥 Cool & Energetic:
🔥 💥 ⚡ 🚀 🎯 🧠 💪 🕶️ 🌀 🎧

🌍 Nature & Mood:
🌞 🌙 🌊 🍃 🌸 🌻 🌈 🌎 🌟 ⛅

🎯 Productivity & Focus:
🧠 📚 🛠️ 🧰 🗂️ 📈 📝 💼 🧘‍♂️ ⏳

💬 Reactions & Support:
👍 👏 🤝 💯 ✅ 🤞 🫶 💬 🥰 🙏

'''

r'''
Concepts:

Getting Text:
.text_content() gets all text, including hidden text
.inner_text() gets only visible text
Examples:
    h1_inner = page.locator('h1').inner_text()
    h1_text = page.locator('h1').text_content()


Content Retrieval:
.text_content() - Gets all text (including hidden)
.inner_text() - Gets visible text only
.input_value() - For form inputs
Questions: 
    What does it mean by Hidden and Visible and why does it matter?

State Checking:
    .is_visible()
    .is_hidden()
    .is_enabled()
    .is_checked()
Questions:
    What does it mean by State Checking? 
    Can you Explain each of it and the functionality of it 

Action Methods:
    .click()
    .fill()
    .type()
    .press()
    .hover()
Questions
    For What Purpose is This 

What does it mean by Waiting Strategies?
Why does it we need to wait for the elements? 
What does it mean by not handling dynamic content that loads asynchronously

'''

r'''

1. Hidden vs Visible Text (Content Retrieval)

.text_content()
    Gets ALL text content, including:
        Text hidden with CSS (display: none, visibility: hidden)
        Text inside <script>, <style> tags
        Text in hidden input fields (<input type="hidden">)
    Questions: Why they need to hide things?
.inner_text()
    Gets only visible text (what a user actually sees on screen). 
    Respects CSS visibility rules.

Use .text_content() when you need raw data (e.g., scraping metadata).
Use .inner_text() when testing user-facing content (e.g., verifying UI text).

2. State Checking (Explained)
Method              Purpose                                                     Example Use Case
.is_visible()	    Checks if element is visible on the page	                Verify a modal appears
.is_hidden()	    Checks if element is not visible (or doesn't exist)	        Confirm a loading spinner disappears
.is_enabled()	Checks if element is clickable/editable (not disabled)	        Test if a submit button is active
.is_checked()	Checks if checkbox/radio is selected	Validate a "Terms & Conditions" checkbox



4. Waiting Strategies & Dynamic Content
Why Wait?
Modern web apps load content asynchronously (e.g., via AJAX/APIs).
If your script tries to interact with an element before it exists, it fails.
'''


r'''
Most Critical Web Scraping Concepts in Playwright

1. Content Retrieval (Essential)
.text_content() vs .inner_text()
.input_value() for forms.
Why? Extracting data is the core goal of scraping.
Your level: Learned (You understand visibility vs. hidden text and use cases.)
    Use .inner_text() for user-facing content (e.g., product titles).
    Use .text_content() for hidden data (e.g., metadata, SEO tags).

2. Waiting Strategies (Essential)
page.wait_for_selector(), page.wait_for_function().
Auto-waiting (Playwright waits for elements to be actionable by default).
Why? Dynamic content (e.g., AJAX, lazy loading) requires explicit waits.
Your level: Partial (You grasp the need for waits but need practice with dynamic content.)




3. Action Methods (High Utility)
.click(), .fill(), .press() for interaction (e.g., pagination, login).
Why? Many sites require interaction to expose data.
Your level: Learned (You know these methods but need projects to master them.)

4. State Checking (Situational)
.is_visible(), .is_enabled() for validation.
Why? Useful for ensuring reliability in complex scrapers.
Your level: Learned (You understand each method’s purpose.)

.is_visible(): Is the element in the DOM and rendered?
.is_hidden(): Opposite of is_visible() (or element doesn’t exist).
.is_enabled(): Can the element be interacted with (e.g., a non-disabled button)?
.is_checked(): For checkboxes/radio buttons.
Use case: Ensure UI consistency before interactions (e.g., wait for a button to be enabled before clicking).


Master Content Retrieval + Waiting Strategies
    Practice scraping sites with lazy loading (e.g., e-commerce product listings).

Projects to Reinforce Learning
    Scrape a paginated table with dynamic loading.
    Log into a site (using .fill() + .click()) and extract protected data.

Dynamic content (waiting strategies).
'''




r'''
Understanding Why the Playwright Works and HTML Parsing like Beautiful Soup and Request is not Working Against the Site 
# My Reflection is i overthink how javascript will be complex but after running the code it definitely working and it super easy for some reason and i just need understanding of why? 


Playwright vs Request + BeautifulSoup: Key Differences

What is Request and Beautiful Soup Fundamentally 
    * HTTP Request Only: Just fetches the initial HTML document from the server
        # What does it mean by HTTP Request Only?+
        # But it said that it goes right into the server 
    * No JavaScript Execution: Gets only static HTML content
    * Lightweight: Minimal resource usage
    * Fast: No browser overhead
    * Limited: Can't interact with dynamic content
    
What is Playwright Fundamentally? 
    * Full Browser Automation: Controls an actual browser (Chromium, Firefox, WebKit)
    * JavaScript Execution: Renders pages exactly like a real user would see them
    * Heavier: Requires browser instances
    * Slower: Has to load all page resources
    * Powerful: Can handle all modern web interactions

It give me a neat Diagram called "Sequence Diagram"

Basically a Beautiful Soup and Request are like this 
My Code -----> Server # Going Straight into the Server getting the HTML
# The Problem with this is there are no JS execution 

In Playwright 
My Code ----> Browser ----> Server 

My Code 
    1. Launch the Actual Browser
Browser 
    1. Execute the Javascript, Render the DOM, Load Dynamic Content
    2. Request top the Server With Full Headers 
    3. Getting the HTML AND JS AND CSS back to my Code a Fully Rendered Page

Each of this have their own Advantage and Disadvantage 
and i can combine Both of them 

'''


r'''
Determining my Proficiency and the Level of Playwright 

in This Deepseek Research and Break it Down 
https://chat.deepseek.com/a/chat/s/4c00b2f2-b0ed-434e-9992-d5e137c4e955

1. Fundamental Competence (Beginner)
Basic Usage: Launching browser, navigating pages, simple text extraction
    Uses basic selectors (CSS/XPath)
    Basic page navigation and content extraction
    Handling iframes and shadow DOM
    Managing multiple tabs/windows
    File downloads/uploads
    Taking screenshots/PDFs

    Dynamic Content Handling
        Waiting for elements to appear/disappear
        Handling infinite scroll
        Dealing with lazy-loaded content
        Processing WebSocket data
        Intercepting and modifying network requests

2. Intermediate Proficiency
Complex Interactions: Form filling, dropdown selection, pagination
    Indicators:
        * Implements explicit waits (wait_for_selector, wait_for_timeout)
        * Handles common anti-bot techniques (basic ones)
        * Can scrape multi-page dynamic content
        * Uses more advanced selectors (>> chaining, :has-text())
3. Advanced Mastery
Stealth Techniques: Full browser fingerprint masking
    Indicators:
        Implements proxy rotation
        Handles Cloudflare and other advanced anti-bot systems
        Can reverse-engineer complex API calls
        Builds custom browser automation patterns




'''