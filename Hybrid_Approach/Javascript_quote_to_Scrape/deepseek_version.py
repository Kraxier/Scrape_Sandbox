from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import time

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        current_url = base_url
        
        while True:
            # Navigate with auto-wait
            page.goto(current_url, wait_until="domcontentloaded")
            
            # Wait for dynamic content
            page.wait_for_selector('.quote', state="visible", timeout=10000)
            
            # Extract quotes (visible text only)
            quotes = page.locator(".quote .text").all()
            for quote in quotes:
                print(quote.inner_text().strip())
                print()
            
            # Robust pagination check
            next_page = page.locator('.next a')
            if not next_page.is_visible(timeout=3000):
                print("Reached last page. Stopping.")
                break
                
            # Get next URL
            next_url = urljoin(
                current_url, 
                next_page.get_attribute('href')
            )
            print(f"Navigating to: {next_url}")
            current_url = next_url
            
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        page.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)