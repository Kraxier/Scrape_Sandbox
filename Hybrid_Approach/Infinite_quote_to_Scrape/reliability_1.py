# From functionality_1 to Reliability_1

r'''
Problem with Previous Code 
1. Unreliable Termination
    Only breaks when page height and scroll position are unchanged, but:
        Page height might not change when new content loads dynamically
        Requires hitting the exact bottom (fragile with variable content)

2. Inefficient Quote Tracking
    Re-scans all quotes on every scroll → O(n²) complexity
        Processes same quotes repeatedly
        No mechanism to detect new content

3. Non-Human Scrolling
    Fixed scroll distance (895px) and pause time → easily detectable as bot

4. Missing Error Handling
    No fallbacks for edge cases (stale elements, network failures)
'''

r'''
Solve these Issues 1 - 4 
1. Robust Termination
    Triple safety net
        MAX_ATTEMPTS (15): Absolute scroll limit
        MAX_FAILS (3): Breaks after no new content
        True bottom detection: scrollY + viewport >= pageHeight - 10px
2. Efficient Content Tracking
    Tracks quotes in a set() for O(1) lookups
    Only processes new elements via :visible pseudo-selector
    Uses combined CSS selector (.quote:visible >> .text) for stability
3. Human-Like Behavior
    Dynamic scroll distances (70-120% of viewport)
    Random scroll ups (20% probability)
    Variable pauses (0.5-2.5 seconds)
    Network idle timeouts
4. Error Resilience
    Handles stale elements with try/except
    Tolerates network timeouts
    Viewport-based calculations work across devices
Diagnostic Output
Clear status messages with:

5. Scroll directions (↑↓)
    Quote counters
    Failure tracking
    Termination reason
'''

r'''
1. Robust Termination System
Why needed: Infinite scroll sites can be unpredictable. Some might never stop loading content, others might have hidden bottoms. We need multiple safeguards.
'''


# MAX_ATTEMPTS = 15  # Absolute scroll limit
# MAX_CONSECUTIVE_FAILS = 3  # Allowed empty scans
# VIEWPORT_HEIGHT = page.evaluate("window.innerHeight")

# # In scroll loop:
# attempt_count = 0
# consecutive_fails = 0

# while attempt_count < MAX_ATTEMPTS and consecutive_fails < MAX_CONSECUTIVE_FAILS:
#     attempt_count += 1
    
#     # ... scrolling logic ...
    
#     # Bottom detection (10px threshold accounts for rendering variances)
#     current_pos = page.evaluate("window.scrollY")
#     total_height = page.evaluate("document.body.scrollHeight")
#     if current_pos + VIEWPORT_HEIGHT >= total_height - 10:
#         print("✅ Reached page bottom")
#         break


r'''
2. Efficient Content Tracking
Why needed: Rescanning ALL quotes every time creates O(n²) complexity. With 100 quotes, that's 5,000 comparisons by the end!
'''

# seen_quotes = set()  # O(1) lookups

# # In scroll loop:
# try:
#     # Get ONLY new quotes using combined selector
#     new_quotes = page.query_selector_all(".quote:visible >> .text")
#     found_new = False
    
#     for quote in new_quotes:
#         text = quote.text_content().strip()
#         if text not in seen_quotes:
#             seen_quotes.add(text)
#             found_new = True
    
#     # Update fail counter
#     if found_new:
#         consecutive_fails = 0
#         print(f"📝 New: {len(seen_quotes)} quotes")
#     else:
#         consecutive_fails += 1
# except Exception as e:
#     print(f"⚠️ Stale element: {e}")
#     consecutive_fails += 1  # Count errors as fails

r'''
3. Human-Like Scrolling
Why needed: Fixed scroll distances and intervals are the #1 bot detector. Humans scroll variably.
'''

# # Get viewport once at start
# VIEWPORT_HEIGHT = page.evaluate("window.innerHeight")

# # In scroll loop:
# if random.random() < 0.8:  # 80% down scrolls
#     # Scroll 70-120% of viewport
#     scroll_dist = random.randint(
#         int(VIEWPORT_HEIGHT * 0.7), 
#         int(VIEWPORT_HEIGHT * 1.2)
#     )
#     page.mouse.wheel(0, scroll_dist)
#     print(f"↓ Scrolled down {scroll_dist}px")
# else:  # 20% up scrolls (human backtracking)
#     scroll_dist = random.randint(200, 500)
#     page.mouse.wheel(0, -scroll_dist)
#     print(f"↑ Scrolled up {scroll_dist}px")

# # Random wait (human reading time)
# time.sleep(random.uniform(0.5, 2.5))



r'''
4. Error Resilience
Why needed: Real-world scraping faces network hiccups, element staleness, and layout changes.
'''


# # Network resilience
# try:
#     page.wait_for_load_state("networkidle", timeout=3000)
# except TimeoutError:
#     print("⏳ Network idle timeout - continuing anyway")

# # Stale element handling (already shown in quote tracking)

# # Viewport-based calculations (works across devices)
# VIEWPORT_HEIGHT = page.evaluate("window.innerHeight")  # Get actual render height

r'''
5. Diagnostic Output
Why needed: Understand exactly why scraping stopped and monitor progress.
'''

# Regular status updates
# print(f"\nAttempt {attempt_count}/{MAX_ATTEMPTS}")
# print(f"Fails: {consecutive_fails}/{MAX_CONSECUTIVE_FAILS}")
# print(f"Position: {current_pos}/{total_height}")

# # Final termination report
# termination_reason = (
#     "Reached bottom" if bottom_reached else
#     "Max attempts" if attempt_count >= MAX_ATTEMPTS else
#     "Max consecutive fails"
# )
# print(f"\n⭐ Terminated: {termination_reason}")
# print(f"Total quotes: {len(seen_quotes)}")


r'''
🎯 1. Master Explicit Waiting (Non-Negotiable)
Why?

time.sleep() is the #1 cause of flaky scrapers (too slow when fast, too fast when slow)

Sites load content dynamically—you need to wait for specific conditions
Implementation:
'''
# INSTEAD OF THIS:
# time.sleep(3)

# # DO THIS:
# page.wait_for_selector(".new-content", state="visible", timeout=5000)  # Wait max 5s
# page.wait_for_function("""() => {
#     return document.querySelectorAll('.quote').length > 20
# }""")

# 🏆 Top 5 High-Impact Waiting Condition
r'''
Content-Ready Detection (Solves 50% of issues)

Why: Guarantees target content exists before interaction. Solves timing issues for dynamic content.
'''
# INSTEAD OF:
# time.sleep(3)

# # DO THIS:
# page.wait_for_selector(".quote", state="visible", timeout=10000)

r'''
Navigation Completion (Critical for page transitions)

Why: Handles redirects, SPA transitions, and delayed loading after clicks.
'''
# INSTEAD OF:
# page.click("a.next")
# time.sleep(5)

# DO THIS:
# with page.expect_navigation():
#     page.click("a.next")

r'''
AJAX Completion (For XHR/fetch requests)

Why: Catches 90% of dynamic content loading without complex detection.
'''
# page.wait_for_load_state("networkidle", timeout=8000)

r'''
Element State Changes (For interactive elements)

Element State Changes (For interactive elements)
'''
# page.wait_for_selector("button.submit:not([disabled])", timeout=5000)

r'''
Scroll Position Verification (For infinite scroll)

Why: Confirms scrolling actually occurred before checking for new content.
'''
# page.wait_for_function("""
#    () => window.scrollY > prevScrollPosition
# """, timeout=3000)



r'''
🔁 2. Retry Mechanisms (Essential)
Why?

30% of web scraping failures are temporary (network blips, ad blockers)

Automatic recovery saves hours of manual restarting
Minimal Implementation:
'''
# from tenacity import retry, stop_after_attempt, wait_exponential

# @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
# def scrape_page(url):
#     page.goto(url)
#     # ... scraping logic ...

r'''
🛠️ 3. Just-Enough Verification (Smart Investment)
Why?

Prevents storing garbage data (e.g., blank quotes, error pages)

5 lines of validation save 5 hours of data cleaning
Critical Checks:
'''
# # BEFORE PROCESSING:
# if "404" in page.title(): 
#     raise Exception("Page missing")

# # AFTER EXTRACTION:
# if not quote_text.strip() or len(quote_text) < 10:
#     continue  # Skip invalid quotes

r'''
⚠️ 4. Verification Checks (Add When Scaling)
Why Hold Off?

Over-verification early on slows prototyping

Only needed when:

Scraping >100 pages

Data quality is critical (e.g., financial data)
When to Add:
'''