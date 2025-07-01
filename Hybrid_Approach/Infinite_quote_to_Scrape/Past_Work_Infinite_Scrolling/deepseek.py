from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import time

def get_true_height(page):
    """Check multiple possible container elements for the real height"""
    containers = [
        "document.body.scrollHeight",
        "document.documentElement.scrollHeight",
        "document.querySelector('.infinite-scroll-container')?.scrollHeight || 0",
        "document.querySelector('.quotes')?.scrollHeight || 0"  # Specific to quotes.toscrape
    ]
    for js in containers:
        height = page.evaluate(js)
        if height > 0:
            return height
    return page.evaluate("document.body.scrollHeight")

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/scroll"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)  # Changed to False for debugging
    page = browser.new_page()
    
    # Enable request interception to monitor network activity
    # page.route('**', lambda route: route.continue_())
    
    page.goto(base_url)
    page.wait_for_selector(".quote", state="attached")
    
    print("🛠️ Starting infinite scroll detection...")
    last_height = get_true_height(page)
    print(f"🚀 Initial page height: {last_height}px")
    
    loop_count = 0
    max_attempts = 3
    current_attempts = 0
    collected_quotes = set()

    while current_attempts < max_attempts:
        loop_count += 1
        print(f"\n🔄 Loop #{loop_count}")
        
        # Scroll with smooth behavior
        page.evaluate("""
            window.scrollBy({
                top: document.body.scrollHeight - window.scrollY,
                behavior: 'smooth'
            })
        """)
        
        # Dynamic wait with element monitoring
        start_time = time.time()
        while time.time() - start_time < 5:  # Max 5 second wait
            # Check for new quotes as primary indicator
            current_quotes = page.query_selector_all(".quote")
            if len(current_quotes) > len(collected_quotes):
                collected_quotes = set(current_quotes)
                break
                
            # Fallback to height check
            new_height = get_true_height(page)
            if new_height > last_height:
                break
                
            page.wait_for_timeout(500)  # Check every 0.5 seconds
        
        # Update height after waiting
        new_height = get_true_height(page)
        print(f"📏 New page height: {new_height}px")
        print(f"📊 Quotes collected: {len(collected_quotes)}")
        
        if new_height == last_height:
            current_attempts += 1
            print(f"⚠️ No change detected (Attempt {current_attempts}/{max_attempts})")
            # Try scrolling again before giving up
            page.evaluate("window.scrollBy(0, 100)")  # Small nudge
            page.wait_for_timeout(1000)
        else:
            current_attempts = 0  # Reset counter on success
            print(f"📈 Height increased by {new_height - last_height}px")
            last_height = new_height

    if current_attempts >= max_attempts:
        print("🛑 Stopping - No new content after multiple attempts")
    else:
        print("✨ All available content loaded!")

    print(f"\n📝 Final Statistics:")
    print(f"• Total loops: {loop_count}")
    print(f"• Final height: {last_height}px")
    print(f"• Unique quotes collected: {len(collected_quotes)}")
    
    # Save screenshot for verification
    page.screenshot(path="final_page.png")
    print("📸 Saved screenshot as 'final_page.png'")
    
    page.close() 
    browser.close()

with sync_playwright() as playwright:
    run(playwright)