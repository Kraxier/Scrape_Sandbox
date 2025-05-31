
# Integrated Playwright Guide: From Basics to Advanced

## Core Concepts (from the Playwright file)

- **Browser launch**: `browser.launch()`
- **Page navigation**: `page.goto()`
- **Content extraction**: `page.inner_text()`, `locator()`
- **Selectors**: CSS, XPath, text-based selectors
- **Waiting mechanisms**: `page.wait_for_selector()`, `page.wait_for_timeout()`
- **Form interaction**: `page.fill()`, `page.click()`
- **Session management**: `storage_state()`
- **Network control**: `page.route()`, `page.expect_response()`
- **Debugging**: `slow_mo`, `PWDEBUG=1`

## Practical Implementation (from your text)

Real-world scraping tasks involving login handling, infinite scroll, pagination, AJAX data, retry logic, and session reuse.

## Example Code (in Python, aligned with the Playwright file)

---

### 1. Foundational Skills

**Goals**: Launch browsers, navigate pages, extract static content.

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://toscrape.com/default")

    quotes = page.locator(".quote").all()
    for quote in quotes:
        print(quote.inner_text())
    browser.close()
```

---

### 2. Dynamic Content Handling

**Goals**: Wait for AJAX/JS content, handle delays.

```python
page.goto("http://toscrape.com/delayed?delay=5000")
page.wait_for_selector(".quote", timeout=10000)
quotes = page.locator(".quote").all()
print([q.inner_text() for q in quotes])
```

---

### 3. Pagination & Infinite Scroll

**Goals**: Scrape multi-page data or infinite scroll.

```python
page.goto("http://toscrape.com/scroll")
prev_height = page.evaluate("document.body.scrollHeight")

while True:
    page.mouse.wheel(0, 10000)
    page.wait_for_timeout(2000)
    new_height = page.evaluate("document.body.scrollHeight")
    if new_height == prev_height:
        break
    prev_height = new_height

quotes = page.locator(".quote").all()
print([q.inner_text() for q in quotes])
```

---

### 4. Form Interactions & Logins

**Goals**: Submit forms, handle CSRF/sessions.

```python
page.goto("http://toscrape.com/login")
page.fill("#username", "fakeuser")
page.fill("#password", "fakepass")
page.click("button[type='submit']")
page.wait_for_url("**/logged-in")

page.context.storage_state(path="auth.json")
context = browser.new_context(storage_state="auth.json")
```

---

### 5. Messy HTML & Advanced Selectors

**Goals**: Parse tables, nested elements.

```python
page.goto("http://toscrape.com/tableful")

table_data = page.locator("table tr").evaluate_all("""
rows => rows.map(row =>
    Array.from(row.querySelectorAll("td")).map(cell => cell.textContent)
)
""")
print(table_data)
```

---

### 6. Advanced: AJAX & Network Control

**Goals**: Mock APIs, handle ViewState.

```python
def handle_route(route):
    route.fulfill(json={"data": "mocked"})

page.route("**/api/data", handle_route)
page.goto("http://toscrape.com/viewstate")
page.select_option("#author-filter", "Albert Einstein")
quotes = page.locator(".quote").all()
print([q.inner_text() for q in quotes])
```

---

### 7. Edge Cases & Debugging

**Goals**: Retry logic, randomization.

```python
page.goto("http://toscrape.com/random")
max_retries = 3
quote = None
for _ in range(max_retries):
    try:
        quote = page.locator(".quote").inner_text(timeout=1000)
        break
    except:
        page.wait_for_timeout(1000)
print(quote or "Not found")
```

---

## Progression Summary

| Level             | Key Skills                        | Playwright Features Used |
|------------------|----------------------------------|---------------------------|
| Foundational     | Basic extraction, selectors       | `launch()`, `goto()`, `inner_text()` |
| Dynamic Content  | Waits, AJAX handling              | `wait_for_selector()`, `expect_response()` |
| Pagination/Scroll| Multi-page scraping               | `click()`, `mouse.wheel()`, loops |
| Forms & Logins   | CSRF, session reuse               | `fill()`, `storage_state()` |
| Messy HTML       | Table parsing, nested selectors   | `evaluate_all()`, chained locators |
| Advanced (AJAX)  | API mocking, network control      | `route()`, `fulfill()` |
| Edge Cases       | Retry logic, debugging            | try/catch, `slow_mo`, `PWDEBUG` |

---

## Final Implementation Plan

1. Start with foundational skills (simple scraping).
2. Progress to dynamic content (waits, AJAX).
3. Handle multi-page data (pagination/infinite scroll).
4. Automate logins/forms (sessions, CSRF).
5. Tackle messy HTML (tables, unconventional layouts).
6. Mock APIs for testing/blocking.
7. Add robustness (retries, debugging).

### Example Workflow

```python
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 1. Login
    page.goto("http://toscrape.com/login")
    page.fill("#username", "user")
    page.fill("#password", "pass")
    page.click("button[type='submit']")
    page.wait_for_url("**/dashboard")

    # 2. Scrape paginated data
    while True:
        quotes = page.locator(".quote").all()
        print([q.inner_text() for q in quotes])
        if not page.is_visible("text=Next"): 
            break
        page.click("text=Next")
        page.wait_for_selector(".quote")

    # 3. Save session
    context.storage_state(path="auth.json")
    browser.close()
```
