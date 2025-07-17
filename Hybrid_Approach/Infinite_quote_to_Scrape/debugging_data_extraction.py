# python debugging_data_extraction.py
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    context = browser.new_context(
        viewport={"width": 1366, "height": 768}  
    )
    page = context.new_page()
    page.goto(base_url)
    quotes = page.locator(".quote .text")
    # quotes_text = page.locator(".quote .text").text_content()
    quotes_text = page.locator(".quote .text").all_text_contents()
    print(f"This is the first one {quotes}")
    print(f"This is the all text content {quotes_text}")

    input()
    page.close() 
    browser.close()


with sync_playwright() as playwright:
    run(playwright)