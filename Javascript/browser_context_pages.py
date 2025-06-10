r'''
Conclusion for 🔁 Sync (Synchronous) and ⚡Async (Asynchronous)

Start with Sync (e.g., requests + BeautifulSoup)
    Easier to understand (linear execution).
    Better for debugging (no async/await complexity).
Focus on core scraping skills:
    HTTP requests, HTML parsing, data extraction.
    Handling errors (404s, rate limits).
    Storing data (CSV, JSON, databases).
You’ll know you’re ready when:
    You can scrape 50+ pages without getting blocked.
    You’re comfortable with headers, sessions, and proxies.
    You’ve hit Sync’s speed limits (e.g., "This is too slow!").


Use Hybrid Learning
    Keep writing sync scripts for simple tasks.
    Rewrite a few sync scripts in async (requests → aiohttp).

Learn Core Async Concepts Early
    Understand async/await, event loops, and non-blocking I/O.
    Experiment with small async scripts (e.g., fetch 5 pages concurrently).


'''

# python browser_context_pages.py
# venv_PS_Toscrape\Scripts\activate


r'''🔁 Sync (Synchronous)'''
# from playwright.sync_api import sync_playwright, Playwright
# from urllib.parse import urljoin

# def run(playwright: Playwright):
#     base_url = "https://quotes.toscrape.com/js/"
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False) 
#     page = browser.new_page()
#     page.goto(base_url)
#     while True: 
#         next_page = page.locator('.next a')
#         quotes = page.locator(".quote .text").all()

#         for quote in quotes: 
#             print(quote.text_content())
#             print()

#         if next_page.count() == 0:
#             print("Reached last page. Stopping.")
#             break
#         next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
#         print(next_page_url)

#         page.goto(next_page_url)
#     page.close() 
#     browser.close()
# with sync_playwright() as playwright:
#     run(playwright)


r'''⚡Async (Asynchronous)'''

from playwright.async_api import async_playwright, Playwright
from urllib.parse import urljoin
import asyncio

async def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto(base_url)
    
    while True:
        next_page = page.locator('.next a')
        quotes = await page.locator(".quote .text").all()

        for quote in quotes:
            print(await quote.text_content())
            print()

        if await next_page.count() == 0:
            print("Reached last page. Stopping.")
            break
            
        next_page_url = urljoin(base_url, await next_page.get_attribute('href'))
        print(next_page_url)

        await page.goto(next_page_url)
    
    await page.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())

# How to make it Faster 
r'''
# How to make it faster 
async def scrape_page(page, url):
    await page.goto(url)
    quotes = await page.locator(".quote .text").all()
    return [await quote.text_content() for quote in quotes]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page1 = await browser.new_page()
        page2 = await browser.new_page()
        
        # Run two pages simultaneously!
        results = await asyncio.gather(
            scrape_page(page1, "https://quotes.toscrape.com/page/1"),
            scrape_page(page2, "https://quotes.toscrape.com/page/2")
        )
        
        print(results)
        await browser.close()

asyncio.run(main())
'''

r'''
⚠️ When is Sync Better?
Simple scripts (few pages, no need for speed).
Easier debugging (async stack traces can be complex).
Legacy codebases that don’t support async.
'''




##################################################################### Concepts ##################################################################### 

r'''
Key Differences
Import Statements:
    Sync: from playwright.sync_api import sync_playwright
    🚀Async: from playwright.async_api import async_playwright

Function Definitions:
    Sync: Regular def functions
    🚀Async: async def coroutine functions

What is Asynchronous I/O (Async IO)?
    My program can handle multiple different task at the same time without waiting 
    the one to finish and it called "rogram to perform non-blocking I/O operations"

What is Non-blocking (📦 I/O = Input/Output)?
    * Program doesn't stop when waiting for an I/O task to finish before moving on 
    * Let your program stay responsive and efficient when dealing with task that spend a lot of time waiting 

Common 📦 I/O = Input/Output Operations:
    Reading/writing files
    Making HTTP requests
    Waiting for user input
    Interacting with databases
    Browser automation (like Playwright)

Method Calls:
    Sync: Direct method calls (page.goto())
    🚀Async: await before method calls (await page.goto())

Context Managers:
    Sync: with sync_playwright() as playwright
    🚀Async: async with async_playwright() as playwright

Execution:
    Sync: Runs sequentially, blocking until each operation completes
    🚀Async: Allows other tasks to run while waiting for I/O operations

When to Use Each
    Use synchronous when:
        Writing simple scripts
        Prefer straightforward, linear execution
        Don't need to handle multiple concurrent operations
    Use asynchronous when:
        Need to handle multiple pages/browsers concurrently
        Want to improve performance by overlapping I/O operations

Working in an async framework (like FastAPI)
The async version is generally more efficient for web scraping as it can handle multiple operations concurrently, 
but it requires more careful programming to manage the async/await flow.

'''

r'''
The asynchronous version is faster because it efficiently handles I/O-bound operations like network requests, which is exactly what web scraping involves. Here's why:

🚀 Why Async is Faster for Web Scraping
    No Waiting Idle
    Synchronous: Your code stops (blocks) at every page.goto(), locator.click(), or network request, waiting for the server to respond. 
    Asynchronous: While waiting for a page to load, the event loop can switch to other tasks, like processing already fetched data or starting new requests.

Concurrency Without Multi-threading
    Async allows you to manage multiple pages/tabs at once without the overhead of threads.
    Example: You could scrape multiple pages in parallel with asyncio.gather().

Optimized for I/O Operations
Playwright's async API is designed to minimize delays when dealing with network requests, DOM interactions, and JavaScript execution.

⚡ Speed Comparison (Example Scenario)
Suppose you scrape 10 pages sequentially:

Sync Version	Async Version
1. Request Page 1 → Wait 500ms	1. Request Page 1 → Don’t Wait
2. Parse Page 1 → 100ms	2. Already Requesting Page 2
3. Request Page 2 → Wait 500ms	3. Parse Page 1 while Page 2 loads
Total: ~6,000ms	Total: ~2,000ms (3x faster!)

'''

r'''
When to use Sync 
1. Legacy or Synchronous Dependencies – If you're using libraries that don’t support async (e.g., requests instead of aiohttp/httpx).

2. Debugging & Simplicity – Sync code is easier to debug step-by-step (no event loops, await quirks).

3. Avoiding Rate Limiting Issues – If a site aggressively blocks bots, sync with delays (time.sleep()) may look more "human."Avoiding Rate Limiting Issues – If a site aggressively blocks bots, sync with delays (time.sleep()) may look more "human."Avoiding Rate Limiting Issues – If a site aggressively blocks bots, sync with delays (time.sleep()) may look more "human."


 When to Use Async for Avoidance?
If the site allows moderate concurrency (e.g., 5-10 requests at a time).
When using proxy rotation + delays to distribute load.
If you need speed but still want stealth (e.g., news sites, stock market data).
'''

r'''
✅ Knowing when i mastered the Sync and Should Switch to Async 
1. I can Write a Functional Scraper 
2. I understand the HTTP basic 
    Modifying User Agent and Referer can handle cookies and manage sessions
3. I can Implement retries (Try and Except and Backoff) can handle status code (402,429)
4. I can bypass Anti Scraping by Delays and rotating user agents 
5. I hit the sync Limitations 

Sign to Switch with ASync 
    1. Comfortable With Sync Pain Points 
    2. I Understand the Async Core Concepts 
    3. I can Debugg Async Code 
        You recognize common async pitfalls:
            Forgetting await → silent failures.
            Unclosed sessions → memory leaks.
            Too much concurrency → bans.
'''

r'''
⚡Async Core Concepts 
    1. async/await Basics
    async: Declares a function as a coroutine (can be paused/resumed).
    $ async def fetch_data():  # This is a coroutine
    $ ...
    await: Pauses execution until an async operation (e.g., HTTP request) completes.
    $ data = await fetch_data()  # Waits without blocking the entire program

    2. Event Loop
    The core of async—manages coroutines, schedules tasks.
    Created automatically with asyncio.run().

        $ import asyncio
        $ async def main():
            $ print("Hello async!")
        $ asyncio.run(main())  # Starts the event loop
    3. Non-Blocking I/O
        Async lets your program do other things while waiting (e.g., send multiple HTTP requests concurrently).

    4. Key Libraries
        HTTP: aiohttp, httpx (async alternatives to requests).
        Delays: asyncio.sleep() (async version of time.sleep()).
    5. Concurrency Control
        Semaphores: Limit concurrent tasks (avoid bans).
    
'''