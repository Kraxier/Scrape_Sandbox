# Anti Detection for my Bot in Python Focusing on PLAYWRIGHT AND BS4 and REQUEST

# Note 80% human-like detection avoidance with 20% effort 
r'''
1. IP & Proxy Management
    Why: 50%+ of detections start at IP level
    Solution:
        Use residential proxies (BrightData, Oxylabs)
        Rotate IPs every 3-5 requests
        Avoid datacenter IPs (AWS, Google Cloud)
2. Header Perfection
    Why: Mismatched headers trigger instant flags
        Use real browser headers (copy from Chrome DevTools → Network tab)
        Always include Sec-* and Accept-* headers
3. Basic Behavior Timing # My Current Focus as a Playwrigther and i needed to master 
    Why: Robots act at machine speed
    Solution: 
        Add randomized delays between actions:
        Vary scroll/dwell times (humans don't scroll at constant speed)
4. Browser Fingerprint Basics
    Why: Headless browsers leak telltale signs
    Disable navigator.webdriver flag
    Set realistic viewport sizes (1366x768, 1920x1080)

🚫 What You Can SKIP (For Now)
    Advanced behavioral biometrics (mouse acceleration curves, keystroke dynamics)
    Canvas fingerprint spoofing
    WebGL/video card emulation
    Complex cookie management
    Sensor API emulation (gyroscope, battery status)

Testing Area for Bots: https://botscan.com/

'''

# Implementing Things 

# Implementation IP and Proxy Management 
from playwright.sync_api import sync_playwright

proxies = cycle([
    # This is BullShit IP but this 
    'http://user:pass@geo.iproyal.com:12321',
    'http://user:pass@geo.iproyal.com:12322'
])

def run():
    with sync_playwright() as p:
        proxy = next(proxies)
        browser = p.chromium.launch(
            proxy={"server": proxy},
            headless=False
        )
        context = browser.new_context()
        page = context.new_page()
        
        # Rotate every 3 pages
        for _ in range(3):
            page.goto("https://example.com")
            # ... your actions ...
        
        browser.close()

while True:
    run()

# Still Proxy for Request 
import requests
from itertools import cycle

proxies = cycle([
    'http://user:pass@geo.iproyal.com:12321',
    'http://user:pass@geo.iproyal.com:12322'
])

session = requests.Session()

for i in range(10):
    proxy = next(proxies)
    response = session.get(
        "https://example.com",
        proxies={"http": proxy, "https": proxy}
    )
    # Rotate every 3 requests
    if i % 3 == 0:
        session = requests.Session()  # New session

# Headers for Playwright 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1"
}

context = browser.new_context(
    user_agent=headers["User-Agent"],
    extra_http_headers=headers
)

# Headers for Request 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Accept": "text/html,application/xhtml+xml...",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin"
}

response = requests.get(url, headers=headers)

# Note for Headers i needed to learn that User Agent Thing where the heck 
# i can get that thing and how it works similar to IP thing 

# Basic Behavior Timing Playwright Human Interactions:
import random
import time
from math import sin

def human_delay(action_type):
    """Randomized delays based on action type"""
    base_times = {
        "click": (0.2, 0.8),
        "navigate": (1.5, 3.0),
        "scroll": (0.1, 0.5),
        "think": (2.0, 5.0)
    }
    min_time, max_time = base_times[action_type]
    return random.uniform(min_time, max_time)

def human_scroll(page, scroll_amount):
    """Human-like scrolling with acceleration"""
    scrolled = 0
    while scrolled < scroll_amount:
        # Vary scroll speed with sinusoidal pattern
        progress = scrolled / scroll_amount
        speed_factor = 0.5 + 0.5 * sin(progress * 3.14)  # Bell curve
        
        step = int(random.uniform(80, 250) * speed_factor
        step = min(step, scroll_amount - scrolled)
        
        # Add slight horizontal variation
        h_offset = random.randint(-5, 5)
        
        page.mouse.wheel(h_offset, step)
        scrolled += step
        
        # Vary wait time based on scroll speed
        wait = max(0.05, 0.3 / speed_factor) * random.uniform(0.8, 1.2)
        time.sleep(wait)

# Usage
page.click("button", delay=human_delay("click") * 1000)  # milliseconds
time.sleep(human_delay("think"))
human_scroll(page, 1200)


# Browser Fingerprint Basics for Playwright 

browser = p.chromium.launch(
    headless=False,
    args=[
        "--disable-blink-features=AutomationControlled",
        "--window-size=1366,768"
    ]
)

context = browser.new_context(
    viewport={"width": 1366, "height": 768},
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
)

# Disable webdriver flag
page.add_init_script("""
    delete Object.getPrototypeOf(navigator).webdriver;
    window.navigator.chrome = { runtime: {}, };
""")

r'''
Timing is Crucial:
    Use different delay profiles for different actions
    Implement acceleration/deceleration in scrolling
    Add random micro-variations (±10%) to all timings
    Include "thinking time" before critical actions

Proxy Best Practices:
    Use session rotation with requests
    For Playwright, rotate entire browser instances
    Always pair proxies with matching geo-located headers

'''


