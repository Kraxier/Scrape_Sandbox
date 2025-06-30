# Goal For Delayed Javascript quotetoscrape ToScrape.Com 
r'''

Apply the Version for the First one Here [Waiting And Auto Retry]
    Waiting for elements to appear/disappear [Concepts]
    * Implements explicit waits (wait_for_selector, wait_for_timeout)
    * Explicit waits (page.waitForSelector())
	* Timeout handling (page.waitForTimeout())
    * Applying the Asynchronous part 

Autowaiting and Explicit Waiting Part Learn that 


'''

# 🎯 1. MASTER EXPLICIT WAITING (Core Skill)
# ✅ 2. VERIFICATION CHECKS (Add Gradually)
# 🔁 3-4. RETRY MECHANISMS (Essential Safety Net)
# 🛠️ 5. JUST-ENOUGH VERIFICATION (Smart Checks)


# quotes_locator.first.wait_for() 

#         page.wait_for_function(
#     """(selector, minCount) => {
#         return document.querySelectorAll(selector).length >= minCount;
#     }""",
#     args=[".quote", 5]  # Wait for at least 5 quotes
# )
#         quotes = page.locator(".quote").all()

# 1. Basic presence
# page.wait_for_selector(".target-element")
    # Wait for the elements to appear in the DOM part 
    # Use Case is when you need to confirm if the elemenet are loaded 

# 2. Visibility check (rendered & not hidden)
# page.wait_for_selector(".target-element", state="visible")
    # Wait for the element to load in the DOM and "visibly rendered" or not hidden
    # Testing interactive elements that must be visible to user 

# 3. Combined check (Modern Playwright)
# expect(page.locator(".quote")).to_be_visible()
    # A Modern approach to verify if elements are visible and it have an own retry mechanism

# 4. Quantity verification
# expect(page.locator(".quote")).to_have_count(10)
    # Basically to count at things if there are 10 matching elements 
    # Use case is when you know the exact thing in there 

# 5. Custom logic waiting
# page.wait_for_function("""
#   () => {
#     const el = document.querySelector('.price');
#     return el && parseFloat(el.textContent) > 100;
#   }
# """)

# Concepts
r'''
        1. Considering the Challenge off 
            Content loads unevenly (some elements appear faster than others).
            Lazy-loading/AJAX fetches data in chunks (e.g., infinite scroll).
            Dynamic pages render elements at different times.
'''
r'''
✅ 2. VERIFICATION CHECKS (Add Gradually)

# Presence (Is the element in DOM?)
assert page.locator(".target").count() > 0

Visibility (Can users see it?)
assert page.locator(".target").first.is_visible()

Content (Has real data loaded?)
assert "Expected Text" in page.locator(".target").first.text_content()

Count (Are all items loaded?)
assert page.locator(".items").count() == expected_count

'''

r'''
🔁 3-4. RETRY MECHANISMS (Essential Safety Net)

from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), 
       wait=wait_exponential(multiplier=1, min=2, max=10))
def safe_click(selector):
    page.wait_for_selector(selector, state="visible")
    page.click(selector)

# Usage example:
safe_click("button.submit")

Progression Exercises:
    Wrap your most common failure points
    Add basic logging to retries:

@retry(...)
def safe_action():
    try:
        # action
    except Exception as e:
        print(f"Attempt failed: {str(e)}")
        raise

'''

r'''
🛠️ 5. JUST-ENOUGH VERIFICATION (Smart Checks)

def verify_critical_elements():
    """Check only the most important indicators"""
    critical_selectors = {
        ".main-content": "visible",  # Key container
        "[data-loaded='true']": "attached",  # Data attribute
        "text='Loading'": "hidden"  # Loading spinner gone
    }
    
    for selector, state in critical_selectors.items():
        if state == "count":
            assert page.locator(selector).count() > 0
        else:
            page.wait_for_selector(selector, state=state)
'''


# "Expect" vs wait_for_* methods 
# xpect is generally preferred for most scenarios due to its modern, concise syntax and built-in retry logic.
# however, both have valid use cases. Here's a breakdown:


# "Expect" vs Explicit wait_for_* Methods

# "expect" benefits 
r'''
1. Automatic Retry Logic: Retries checks until timeout (default: 5s) without manual loops.
2. Cleaner Syntax: Readable and declarative.
3. Rich Assertions: Supports text, visibility, count, state, etc. (e.g., to_have_text(), to_be_enabled()).
4. Consistency: Integrates seamlessly with Playwright's locators

'''

# When to Use Explicit wait_for_* Methods
r'''
1. Basic Presence (No Visibility Needed)
page.wait_for_selector(".hidden-element")  # Exists but not visible

2. Custom JavaScript Conditions
    Use for complex logic not covered by expect:
    page.wait_for_function("""
    () => {
        const price = document.querySelector('.price');
        return price && parseFloat(price.innerText) > 100;
    }
    """)
# In this terms having a skill for javascript conditions 
# so what are the conditions ican look for ? 

3. Non-UI Checks
Use for non-rendering events (e.g., network requests):
page.wait_for_url("**/checkout-complete")  # Wait for navigation

Scenario	                                    Tool	                        Example
Waiting for visible/renderable elements	        expect	                        expect(locator).to_be_visible()
Verifying quantities (e.g., 10 items)	        expect	                        expect(locator).to_have_count(10)
Element existence (ignoring visibility)	        wait_for_selector	            page.wait_for_selector(".element")
Custom JS logic (e.g., price > $100)	        wait_for_function	            Custom JS snippet
Waiting for navigation/network events	        wait_for_url/wait_for_event	    page.wait_for_url("**/success")

'''


# Critical Considerations

r'''

1. Avoid Implicit Waits:
Playwright operations (e.g., click(), fill()) auto-wait for elements. Use explicit waits only for additional conditions.
# Note: I don't understand this parts 

2. Timeouts:
Both approaches accept timeouts:
expect(locator).to_be_visible(timeout=10_000)  # 10 seconds
page.wait_for_selector(".element", timeout=10_000)

3. Hybrid Approach: # Note i don't have much experience on this case 
page.wait_for_selector(".container")  # Fast DOM check
expect(page.locator(".data-row")).to_have_count(20)  # Verify rendered data


'''

# Conclusions expect vs wait in methods
# Default to expect for visibility, counts, or text checks (90% of cases).

# Use wait_for_* for DOM presence without visibility, custom JS, or non-rendering events.

# Never use raw time.sleep() – Playwright's built-in waits are faster and more reliable.



# FUTURE CASES Yes, 
# there are differences between using expect in synchronous vs. asynchronous
# So that is NEAT TO LEARN 