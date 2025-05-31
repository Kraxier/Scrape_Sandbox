# Solving the Problem of Pagination in Playwright
# python test_1_pagination.py


# First Version of the Code and there are Problem here 

r'''
I'm Trying to get the .next a in this code next_page = page.locator('.next a').get_attribute('href')
but the problem is if it go to the last page it give "None" and Playwright crashes this is why we need to check 
the Element first before getting something
'''
# from playwright.sync_api import sync_playwright, Playwright
# from urllib.parse import urljoin

# def run(playwright: Playwright):
#     base_url = "https://quotes.toscrape.com/js/"
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False) 
#     page = browser.new_page()
#     page.goto(base_url)
#     while True: 
#         next_page = page.locator('.next a').get_attribute('href')

#         if next_page is None:
#             print("No more pages. Stopping.")
#             break  # Stop the loop if there's no next page
#         next_page_url = urljoin(base_url, next_page) 
#         print(next_page_url)
#         page.goto(next_page_url)
#     browser.close()

    

# with sync_playwright() as playwright:
#     run(playwright)

# This Work Perfectly Fine in terms of Paginations 
# The PRoblem is I don't Understand the Code 

r'''
This Part 
        # Check if the .next a element exists first
        next_link = page.locator('.next a')
        if next_link.count() == 0:
            print("No more pages.")
            break  # Exit loop safely

And This Part 
        # Now safe to get href
        next_href = next_link.get_attribute('href')
        next_page_url = urljoin(base_url, next_href)
        print(f"Going to: {next_page_url}")
        page.goto(next_page_url)

'''
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(base_url)

    while True:
        # Check if the .next a element exists first
        next_link = page.locator('.next a')
        if next_link.count() == 0:
            print("No more pages.")
            break  # Exit loop safely

        # Now safe to get href
        next_href = next_link.get_attribute('href')
        next_page_url = urljoin(base_url, next_href)
        print(f"Going to: {next_page_url}")
        page.goto(next_page_url)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
