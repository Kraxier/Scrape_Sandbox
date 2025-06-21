# ✅ Proper Functional Scraper Checklist

Elevate your scraping game from basic to production-ready with human-like behavior, error resilience, stealth tactics, and robust data handling.

---

## 🧍 1. Human-Like Interaction Patterns

```python
from random import uniform, randint

def human_like_interaction(page):
    # Randomized mouse movements
    page.mouse.move(
        x=randint(100, 500),
        y=randint(100, 300),
        steps=randint(5, 20)
    )
    
    # Natural scrolling
    for _ in range(randint(2, 5)):
        page.mouse.wheel(0, randint(300, 800))
        page.wait_for_timeout(uniform(0.8, 2.5))  # Random delay
    
    # Random browsing patterns
    if randint(1, 10) > 7:  # 30% chance to visit random page element
        random_link = page.locator("a").nth(randint(0, 10))
        if random_link.is_visible():
            random_link.click()
            page.wait_for_timeout(uniform(1, 3))
            page.go_back()
```

---

## 🕵️ 2. Stealth Configuration

```python
def launch_stealth_browser(playwright):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...",
        # Add 5+ real user agents
    ]
    
    return playwright.chromium.launch(
        headless=False,
        args=[
            f"--user-agent={random.choice(user_agents)}",
            "--disable-blink-features=AutomationControlled",
            f"--window-size={randint(1200,1400)},{randint(800,1000)}"
        ]
    )
```

---

## 🧱 3. Error Handling & Recovery

```python
def scrape_with_retry(page, max_retries=3):
    for attempt in range(max_retries):
        try:
            page.wait_for_selector(".quote", state="attached", timeout=15000)
            return page.locator(".quote").all()
        except TimeoutError:
            print(f"Attempt {attempt+1} failed. Refreshing...")
            page.reload()
            page.wait_for_load_state("networkidle")
    raise Exception("Content loading failed after retries")

def handle_captcha(page):
    if page.locator("#captcha").is_visible():
        print("CAPTCHA detected - pausing for manual solve")
        page.pause()  # Manual intervention
```

---

## 💾 4. Data Pipeline Integration

```python
import json
from datetime import datetime

def save_data(quotes, filename="quotes.json"):
    output = {
        "scraped_at": datetime.utcnow().isoformat(),
        "source": page.url,
        "quotes": [{
            "text": quote.locator(".text").inner_text(),
            "author": quote.locator(".author").inner_text(),
            "tags": quote.locator(".tag").all_inner_texts()
        } for quote in quotes]
    }
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(output) + "\n")  # JSON Lines format
```

---

## 📈 5. Performance Monitoring

```python
import time
import psutil

def monitor_performance():
    start_time = time.time()
    # ... scraping operations ...
    print(f"Scraped {len(quotes)} quotes in {time.time()-start_time:.2f}s")
    
    # Memory usage check
    if psutil.Process().memory_info().rss > 100 * 1024 * 1024:  # 100MB
        print("High memory usage - restarting browser")
        restart_browser()
```

---

## 🧩 Complete Production-Ready Template

```python
from playwright.sync_api import sync_playwright
import random
import time
import json
import psutil
from datetime import datetime

# Insert previously defined helper functions here

def run_scraper():
    with sync_playwright() as playwright:
        browser = launch_stealth_browser(playwright)
        context = browser.new_context(
            viewport={"width": random.randint(1200,1400), "height": random.randint(800,1000)}
        )
        page = context.new_page()
        
        try:
            page.goto("https://quotes.toscrape.com/js-delayed/", wait_until="networkidle")
            
            # Main scraping loop
            for page_num in range(1, 6):
                handle_captcha(page)
                human_like_interaction(page)
                
                quotes = scrape_with_retry(page)
                save_data(quotes, f"page_{page_num}.json")
                
                # Human-like navigation
                if page.locator('.next a').is_visible():
                    with page.expect_navigation():
                        page.locator('.next a').click(delay=random.randint(100, 800))
                else:
                    break
                    
                monitor_performance()
                
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    run_scraper()
```

---

## 🔑 Key Features of a Proper Scraper

### ✅ Behavioral Obfuscation
- Randomized interaction patterns  
- Natural mouse movements  
- Variable timing between actions  
- Viewport size changes  

### ✅ Resilience Systems
- Automatic retry mechanisms  
- CAPTCHA detection and handling  
- Memory/performance monitoring  
- Graceful failure recovery  

### ✅ Data Integrity
- Structured JSON output  
- Metadata tracking (timestamps, source)  
- Atomic writes (prevent data loss)  
- Schema validation  

### ✅ Stealth Enhancements
- User agent rotation  
- Browser fingerprint masking  
- Headless detection evasion  
- Realistic browser environments  

### ✅ Operational Visibility
- Performance metrics  
- Error logging  
- Progress tracking  
- Resource monitoring  

---

## 📚 Next-Level Skills to Develop

### 🔄 Proxy Rotation

```python
proxies = ["http://user:pass@proxy1:port", ...]
browser = chromium.launch(proxy={"server": random.choice(proxies)})
```

### 🕶️ Browser Fingerprint Spoofing

```python
context = browser.new_context(
    user_agent=random.choice(user_agents),
    locale='en-US,en;q=0.9',
    timezone_id="America/New_York",
    color_scheme="dark"
)
```

### ☁️ Distributed Scraping
- Use Redis task queues  
- Deploy via Docker containers  
- Scale with Cloud Functions or Lambda  

### 🤖 AI-Powered Bypasses
- CAPTCHA Solving (via services or models)  
- Detecting behavioral traps  
- Adapting to site structure changes with ML  

---

## 💡 Pro Tip:
**Start small.** Integrate human-like behaviors and retry mechanisms first. Add stealth, then scale out as the target complexity grows.