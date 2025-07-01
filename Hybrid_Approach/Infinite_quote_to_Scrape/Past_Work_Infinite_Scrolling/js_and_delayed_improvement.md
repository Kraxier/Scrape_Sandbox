# Key Improvements for Your Current Script

## Replace Fixed Waits with Dynamic Conditions

```python
# Instead of:
page.wait_for_selector(".quote .text", timeout=12000)

# Use:
page.wait_for_function("""() => {
    return document.querySelectorAll('.quote .text').length > 0
}""", timeout=12000)
```

## Add Navigation Waits

```python
# After each page.goto(), add:
page.wait_for_load_state("networkidle")  # Wait for AJAX calls
page.wait_for_function("""() => {
    return document.readyState === 'complete'
}""")
```

## Implement Robust Pagination Handling

```python
# Instead of assuming next page exists:
if page.locator('.next a').count() > 0:
    next_page = page.locator('.next a').first
    # ... proceed with navigation
else:
    print("No more pages")
    break
```

## Add Error Recovery

```python
from playwright.sync_api import TimeoutError

try:
    page.wait_for_selector(".quote .text", timeout=10000)
except TimeoutError:
    print("Quotes didn't load, refreshing...")
    page.reload()
    # Retry logic
```

---

# Core Playwright Skills to Master (20% Effort → 80% Results)

| Skill Category         | Key Methods                                   | Why It's Essential                                               |
|------------------------|-----------------------------------------------|------------------------------------------------------------------|
| Smart Waiting          | `wait_for_function()`, `wait_for_selector()`, `wait_for_url()` | Crucial for JS sites where content loads asynchronously          |
| Element State Checks   | `is_visible()`, `is_enabled()`, `is_checked()` | Prevents errors before interacting with elements                 |
| Network Control        | `route()`, `unroute()`, `wait_for_response()` | Essential for AJAX-heavy sites and API scraping                  |
| Frame Handling         | `frame()`, `frame_locator()`                   | Mandatory for iframes and shadow DOM content                     |
| Execution Context      | `evaluate()`, `evaluate_handle()`             | Core technique for extracting complex JS data                    |

---

# The 5 Critical Methods to Master First

## 1. `page.wait_for_function()`

The single most important method for JS sites:

```python
# Wait for specific data to be available
page.wait_for_function("""() => {
    return window.__INITIAL_STATE__?.quotes?.length > 10
}""")
```

## 2. `page.route()`

Intercept and mock network requests:

```python
def handle_route(route):
    if "/api/quotes" in route.request.url:
        route.fulfill(json=mock_data)

page.route("**/api/*", handle_route)
```

## 3. `frame_locator()`

Handle iframes and shadow DOM:

```python
quote_frame = page.frame_locator("iframe.quote-container")
text = quote_frame.locator(".text").inner_text()
```

## 4. `evaluate()`

Extract complex JS data structures:

```python
initial_state = page.evaluate("""() => {
    return window.__INITIAL_STATE__ || {}
}""")
```

## 5. `expect()`

Professional validation (not just for tests):

```python
from playwright.sync_api import expect

quotes_locator = page.locator(".quote")
expect(quotes_locator).to_have_count(10, timeout=15000)
```

---

# Practice Roadmap

### Week 1: Waiting Strategies
- Master `wait_for_function` with different DOM states  
- Practice on: [https://quotes.toscrape.com/js-delayed/](https://quotes.toscrape.com/js-delayed/)

### Week 2: Network Interception
- Learn to mock API responses  
- Practice on: [https://demo.playwright.dev/api-mocking](https://demo.playwright.dev/api-mocking)

### Week 3: JS Execution
- Extract data from JS objects  
- Practice on: [https://react-redux.realworld.io](https://react-redux.realworld.io)

### Week 4: Frame Handling
- Work with iframes and shadow DOM  
- Practice on: [https://the-internet.herokuapp.com/iframe](https://the-internet.herokuapp.com/iframe)

---

# Progression Checklist

- [x] Can wait for dynamic content without `time.sleep()`
- [x] Can intercept and modify network requests
- [x] Can extract data from JS variables
- [x] Can handle iframe-based content
- [x] Can recover from loading errors

---

These skills will give you **80% coverage** for modern web scraping. Once mastered, you'll be able to handle:

- React/Vue/Angular SPAs  
- Lazy-loaded content  
- Authentication-protected sites  
- Real-time data dashboards  
- Complex e-commerce sites
