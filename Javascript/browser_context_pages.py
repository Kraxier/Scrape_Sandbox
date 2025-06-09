r'''
Implementations:
1. Implementing ⚡Async (Asynchronous) vs 🔁 Sync (Synchronous) in Playwright and observe the difference 
2. Implementing Multiple Pages and Browser in terms of Opening a stuffs 
3. Implementing Concurrency 
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
r'''
My Own Reflection: 

Damn this is Really Fast and very Rapid 
To Dolist 
1. Compare the Syntax between Asynchrounous and Sync

'''

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


r'''
Key Differences
Import Statements:

Sync: from playwright.sync_api import sync_playwright

Async: from playwright.async_api import async_playwright

Function Definitions:

Sync: Regular def functions

Async: async def coroutine functions

Method Calls:

Sync: Direct method calls (page.goto())

Async: await before method calls (await page.goto())

Context Managers:

Sync: with sync_playwright() as playwright

Async: async with async_playwright() as playwright

Execution:

Sync: Runs sequentially, blocking until each operation completes

Async: Allows other tasks to run while waiting for I/O operations

When to Use Each
Use synchronous when:

Writing simple scripts

Prefer straightforward, linear execution

Don't need to handle multiple concurrent operations

Use asynchronous when:

Need to handle multiple pages/browsers concurrently

Want to improve performance by overlapping I/O operations

Working in an async framework (like FastAPI)

The async version is generally more efficient for web scraping as it can handle multiple operations concurrently, but it requires more careful programming to manage the async/await flow.


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