# python browser_context.py
# venv_PS_Toscrape\Scripts\activate
r'''
I try to activate the venv in the different folder and it didn't work 
'''


r'''
Summary 
'''











# My Own Implementation: 
'''
Practical Implementation Roadmap
    Start Simple: Begin with Step 1 - basic single-page scraping
    Add Parallelism: Move to Step 2 when you need to scrape multiple pages
    Handle Sessions: Implement Step 3 when you need separate sessions/cookies
    Avoid Detection: Add Step 4 techniques when facing anti-bot measures
    Optimize Resources: Use Step 5 structure for larger projects
    Scale Intelligently: Implement Step 6 decisions to adapt to website behavior

Remember:
    Only add complexity when needed
    Monitor your scraper's success rate
    Start with conservative settings (2-3 tabs)
    Add features incrementally as requirements evolve
    Always clean up resources (close pages, contexts, browsers)
'''

# Decisions tree:
r'''
✅ Requirements & Decisions to Avoid Overengineering
1. How many pages do I need to scrape?
Few pages (1–5 total) →
✅ Use Step 1: Basic Single Tab Scraper.
❌ Don’t add threads or complexity yet.

Dozens of pages →
✅ Use Step 2: Multi-Tab with Threads.
❌ Avoid context/session management unless needed.

Hundreds to thousands →
✅ Move to Step 5: Advanced Scraper with concurrency.

2. Do I need session isolation (cookies, login, tracking)?
No login/cookie requirement →
✅ Use shared browser or shared tab model (Steps 1–2).
❌ Avoid isolated contexts.

Yes: site uses session cookies or login →
✅ Use Step 3: Isolated Contexts.
❌ Don’t share tabs or sessions across tasks.

3. Are websites blocking me or detecting bots?
No detection or blocking issues →
✅ Skip Step 4.
❌ Avoid rotating agents or adding delays.

Yes: Bot detection triggered (CAPTCHA, 403, rate limit) →
✅ Implement Step 4: Anti-detection (delays, rotation).

4. What’s my current success rate?
High success rate (≥ 90%) →
✅ Stay at current complexity.
❌ Don’t increase threads or tabs.

Low success rate (< 70%) →
✅ Consider reducing concurrency, or adding Step 4 or Step 3 features.

Use this logic programmatically:
✅ Refer to the should_scale_up() function from Step 6.

5. What’s the current system resource usage?
Low memory/CPU usage →
✅ Okay to use more tabs/threads.

High memory/CPU usage or crashes →
✅ Limit concurrent tabs with max_tabs.
✅ Use queue-based control (Step 5).
❌ Don’t increase thread count blindly.

6. Do I need real-time performance or can I process in batches?
Batch scraping (offline or delay-tolerant) →
✅ Use conservative concurrency.
✅ Run slower with fewer failures.

Real-time or speed-critical →
✅ Optimize with Step 5’s threading and parallelism.
✅ Scale max_tabs carefully based on success rate.
'''


r'''
Step 1: 
    Single browser instance
    Single page/tab
    Simple sequential execution

Step 2: 
    Multiple tabs in parallel
    Shared browser process
    Thread-based parallelism
    Shared memory/resources

from playwright.sync_api import sync_playwright
import threading

def tab_worker(url, results, index):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        results[index] = page.title()
        browser.close()

def multi_tab_scraper(urls):
    results = [None] * len(urls)
    threads = []
    
    for i, url in enumerate(urls):
        thread = threading.Thread(target=tab_worker, args=(url, results, i))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return results

# Test with multiple URLs
urls = [
    "https://example.com",
    "https://python.org",
    "https://playwright.dev"
]
titles = multi_tab_scraper(urls)
for url, title in zip(urls, titles):
    print(f"{url}: {title}")

'''

# Step 3 Isolated Contexts for Session Separation
#Context isolation
#Separate cookies/sessions
#Resource management


r'''
from playwright.sync_api import sync_playwright

def isolated_context_scraper(urls):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        results = []
        
        for url in urls:
            # Create a new context for each URL
            context = browser.new_context()
            page = context.new_page()
            
            page.goto(url)
            results.append(page.title())
            
            # Close context to free resources
            context.close()
        
        browser.close()
        return results

# Test with multiple URLs
urls = [
    "https://example.com",
    "https://httpbin.org/cookies/set/testcookie/value",
    "https://httpbin.org/cookies"
]
titles = isolated_context_scraper(urls)
for url, title in zip(urls, titles):
    print(f"{url}: {title}")

'''

# Step 4: Add Anti-Detection Measures
# Implement delays, user agent rotation, and cache control.
# Request delays
# User agent rotation
# Cache control
# Basic anti-detection
r'''
from playwright.sync_api import sync_playwright
import random
import time

def stealth_scraper(urls):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        results = []
        
        for i, url in enumerate(urls):
            # Random delay between requests
            if i > 0:
                delay = random.uniform(1.0, 3.0)
                time.sleep(delay)
            
            context = browser.new_context(
                # Rotate user agents
                user_agent=random.choice(user_agents),
                
                # Disable caching
                ignore_https_errors=True,
                bypass_csp=True
            )
            
            # Disable resource caching
            context.route("**/*", lambda route: route.continue_())
            
            page = context.new_page()
            page.goto(url)
            results.append(page.title())
            context.close()
        
        browser.close()
        return results

# Test with multiple URLs
urls = [
    "https://example.com",
    "https://python.org",
    "https://playwright.dev",
    "https://github.com"
]
titles = stealth_scraper(urls)
for url, title in zip(urls, titles):
    print(f"{url}: {title}")

'''
# Step 5: Advanced - Parallel Processing with Resource Management
# Key Concepts:
# Concurrency control
# Resource management
# Error handling
# Anti-detection techniques
# Queue-based task management


r'''
from playwright.sync_api import sync_playwright
import threading
import queue
import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdvancedScraper:
    def __init__(self, max_tabs=3, headless=True, request_delay=(1, 3)):
        self.max_tabs = max_tabs
        self.headless = headless
        self.request_delay = request_delay
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        ]
    
    def worker(self, url, result_queue):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            
            # Create isolated context
            context = browser.new_context(
                user_agent=random.choice(self.user_agents),
                ignore_https_errors=True,
                bypass_csp=True
            )
            
            # Disable caching
            context.route("**/*", lambda route: route.continue_())
            
            page = context.new_page()
            
            try:
                # Add random delay
                delay = random.uniform(*self.request_delay)
                time.sleep(delay)
                
                page.goto(url, timeout=60000)
                title = page.title()
                result_queue.put((url, title, None))
                logging.info(f"Successfully scraped: {url}")
            except Exception as e:
                result_queue.put((url, None, str(e)))
                logging.error(f"Error scraping {url}: {str(e)}")
            finally:
                # Clean up resources
                page.close()
                context.close()
                browser.close()
    
    def scrape(self, urls):
        result_queue = queue.Queue()
        threads = []
        
        # Create worker threads
        for url in urls:
            thread = threading.Thread(target=self.worker, args=(url, result_queue))
            threads.append(thread)
            
            # Limit concurrent tabs
            while len(threads) >= self.max_tabs:
                for t in threads:
                    if not t.is_alive():
                        t.join()
                        threads.remove(t)
                time.sleep(0.1)
            
            thread.start()
        
        # Wait for remaining threads
        for thread in threads:
            thread.join()
        
        # Collect results
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())
        
        return results

# Test the advanced scraper
scraper = AdvancedScraper(max_tabs=2)
urls = [
    "https://example.com",
    "https://python.org",
    "https://playwright.dev",
    "https://github.com",
    "https://httpbin.org/delay/2",  # Delayed response
    "https://invalid.url"  # Will cause error
]

results = scraper.scrape(urls)
print("\nScraping Results:")
for url, title, error in results:
    if error:
        print(f"❌ {url}: {error}")
    else:
        print(f"✅ {url}: {title}")

'''


# Prerequisite Concepts for Understanding Multiple Tabs and Browser

r'''
Fundamentals of Web Scrapping for Scrapping Architecture 
    1. What does it mean by Share Memory
    Tabs and Browser share the sane Ram for Allocation 
        Shared: more efficient, but riskier.
        Isolated: safer, but uses more memory. (This means Multiple Browser)
    Share Ram means : It allows the JavaScript engines, DOM objects, and other components of multiple tabs to share common memory structures.
    This means its already load on your browser that can reuse in multiple tabs like a template thing 

    2. Share Cache:
        Cache Files like image,JS and CSS are Share or reused across tabs 
        Scraping Tip: Disable cache when you need fresh requests:
    
    3. Cookies 
        Small pieces of data stored by websites (login sessions, tracking).
            * Same cookies across tabs = Same login session
            * Different cookies = Appear as different users
            * Critical for: Sites requiring login (e.g., scraping LinkedIn profiles)
    4. Sessions
        Server-side tracking of user activity (often cookie-based).
        One session = One "user" from the website's perspective
        Scraping Trick: Rotate sessions to avoid detection:
    5. Local Storage
        Persistent Browser Storage 
        Scraping Relevance:
            Stores user preferences/auth tokens
            Some sites save API keys here
    6. Cache (Browser Cache)
        Temporary storage of web assets (images, scripts).
        Enable cache → Faster but might get stale data
        Disable cache → Slower but fresh requests
    7. Proxy Configurations
        What it is: Routing traffic through intermediary IP addresses.
        Avoid IP bans by rotating proxies
        Geographic-specific scraping
    Practical Scraping Cheat Sheet
    Term	        When to Care About It	                        Playwright Control Method
    Memory	        Running many tabs on low-RAM servers	        Limit tabs per browser
    Cookies	        Logins, session persistence	                    browser.newContext() per session
    Cache	        Avoiding stale data/being detected as a bot	    ignoreHTTPSErrors: true
    **LocalStorage	Sites storing auth tokens here	                context.clearCookies() + context.clearStorage()
    Proxy	        Avoiding IP bans                                chromium.launch({ proxy: { ... } })
'''

r'''
Summary of Prerequisite 


'''


# Concepts in Multiple Tabs and Browser
r'''

🗒️ What is the Difference of Multiple Tab in Single Browser and Multiple Browser:

🗓️1. Multiple Tab in a Single Browser:
    * Tabs share the same " browser proccess " # What does it mean by Share Browser Proccess?
    * Share Memory/Cache means faster and less resource intensive i think in my own device
    * Share Cookies/ Local Storage: 
        What does it mean by Share Cookies?
        What does it mean by Local Storage?
🗓️2. Multiple Browser:
    Completely seperate proccess:
        A. Local Storage
        B. Share Cookies
        C. Cache 
    Heavier on Personal Computer 

🗂️What is Seperate Context Means:
    Each Context have it's own Cookies, Local Storage/Sessions, Cache and Browser Setting

🗂️When to Approrach it to avoid OverEngineering the Script
    1. Multiple Tabs: 
        Scrapping the Site with Same "Sessions"
        Lightweight Parallelism
        Task are Short lived 
        No Log in state Conflict 
    2. Multiple Context: 
        Need Different Sessions on Same Site
        Handling Multiple Log in Simultaneously
        Want to Isolate Cookies/Storage and resource Efficiency
    3. Multiple Browser (Rarely Need For Scrapping)
        Completely Seperate Browser Binaries, Proxy Configuration and GPU proccess 
    
Decision Flowchart 
    1. Start with Single Tab
    2. for Speed Add 2-5 Tabs
    3. If getting Blocked, Seperate the Context 
    4. Need Different Proxy use Multiple Browser

Over Engineering Things:
    1. Using Multiple Browser when site have no Anti Bot Protection 
    2. Using 10 Tabs but the machine can keep up 
    3. Managing Complex Tab Logic for a Sequential Scrapping 
        I think it means the next page here 
    4. Website is simple and rate limits aren't an issue 


📈 Pros of Multiple Tab and Browser: 
    🚀 Pararell Proccessing 
        1. I can scrape pages simultaneously 
        2. Different Tabs can handle Different Task
        Q(2): What is other Task i can do in terms of this because i didn't experience this
    Session Isolation: 
        1. Each Tab can maintain sessions like seperate cookies, LocalStorage and Session Storage 
        2. Useful for Scrapping site that require Different Login Sessions
        3. Maintaining the Sessions 
    Resource Efficiency:
        1. Multiple tabs are good than Multiple Browser
        2. What does it mean by context system efficiently manage tabs? 
        3. Keeping the Reference page 

📌 Cons for Multiple Tab/ Browser 
    1. Increase Complexity 
        * Challenge in Error Handling and Synchronization
        * Managing Tab Lifecycle like opening and closing it 
    2. Over Resource
        * Memory Issues and Throtlling 
        * You can be Detected in Parallel request
    3. Session Confusion Risk
        * Sharing the State betweeb tabs 
        * Careful management of Context 
    4. Anti botg System 
        * To Many Tabs is Suspicious 
        * Learning to Delay while also randomize Patterns 

Best Practice 
    1. Creating Seperate Context for each tabs
    2. Limit "Concurrency" start with 2-5 Tabs 
    3. Closing tabs for prevention of "Memory Leaks"
    4. Implement Always the Error Handling 
    5. Implement the Throttling limiting the request or delays 
'''







# Analyze this Text Properly 
r'''
1. Resource Sharing & Isolation
Shared Memory: All tabs in a browser share the same process memory
Shared Cache: Disabled in this implementation for fresh requests
Cookies & Sessions:
Same context = shared cookies/sessions
Different contexts = isolated sessions
Rotated automatically after failures

2. Scaling Strategy
Start conservative: 2 tabs, no contexts, single browser
Scale UP when:
Success rate > 90%
Average task time is low
Scale DOWN when:
Success rate < 70%
Average task time > 10s
Enable contexts when experiencing blocking

3. Anti-Detection Measures
Random delays between requests
User agent rotation
Session rotation after failures
Viewport randomization
Proxy rotation (if configured)

5. Resource Management
Page lifecycle: Each page closed immediately after use
Context rotation: Creates new contexts after failures
Proxy support: Optional proxy rotation
Memory safety: Pages always closed in finally block
When to Scale Up/Down - Practical Indicators
Scale UP When:
Queue processing is consistently slower than task arrival
Success rate > 90% with current configuration
System resources (CPU/RAM) underutilized (< 70%)
Task completion time is consistently low
Scale DOWN When:
Error rate exceeds 30%
Average task time > 10 seconds
System memory usage > 80%
CPU usage consistently > 90%
Switch to Contexts When:
Getting blocked despite random delays
Need different sessions for different tasks
Handling logins for multiple accounts
When simple tab-based scraping fails consistently
'''