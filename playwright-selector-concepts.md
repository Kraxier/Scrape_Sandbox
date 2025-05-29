# Essential Playwright Selector Concepts

Beyond the basics you've encountered, here are several important selector concepts in Playwright that will help you write more robust and flexible automation scripts:

## 1. Locator vs. ElementHandle

**Locator** (what you should use most of the time):

- Represents a way to find elements on the page
- Lazy evaluation (doesn't immediately search the DOM)
- Retries automatically when the page changes
- Preferred method in modern Playwright

```python
locator = page.locator('.quote')
```

**ElementHandle** (older approach, less recommended):

- Represents an actual DOM element
- Stale if page changes
- More direct but less resilient

## 2. Common Locator Methods

**Content Retrieval:**
- `.text_content()` - Gets all text (including hidden)
- `.inner_text()` - Gets visible text only
- `.input_value()` - For form inputs

**State Checking:**
- `.is_visible()`
- `.is_hidden()`
- `.is_enabled()`
- `.is_checked()`

**Action Methods:**
- `.click()`
- `.fill()`
- `.type()`
- `.press()`
- `.hover()`

## 3. Advanced Locator Strategies

**Filtering Locators:**
```python
# Get the third quote
third_quote = page.locator('.quote').nth(2)

# Get last matching element
last_item = page.locator('.item').last
```

**Chaining Locators:**
```python
# Find element with class 'text' inside element with class 'quote'
quote_text = page.locator('.quote').locator('.text')
```

**Combining Selectors:**
```python
# Element that has both classes
page.locator('.btn.primary')

# OR condition
page.locator('button:has-text("Log in"), button:has-text("Sign in")')
```

## 4. Waiting Strategies
```python
# Wait for element to appear
locator.wait_for()

# Custom timeout
locator.click(timeout=10000)  # 10 seconds

# Wait for element state
locator.wait_for(state="visible")
```

## 5. Best Practices for Selectors

**Prioritize user-visible attributes:**
```python
# Better
page.locator('button:has-text("Submit")')

# Less robust
page.locator('button[data-testid="submit-btn"]')
```

**Use text selectors wisely:**
```python
# Exact text
page.locator('text="Login"')

# Contains text (case insensitive)
page.locator('text=/login/i')
```

**CSS vs XPath:**

- Prefer CSS selectors when possible
- Use XPath for complex relationships

```python
# CSS
page.locator('div.item > h3.title')

# XPath
page.locator('xpath=//div[@class="item"]/h3[contains(@class, "title")]')
```

**Test selectors in DevTools:**
- Use `$$()` in browser console to test CSS selectors
- `$x()` for XPath testing

## 6. Common Pitfalls

- Overly specific selectors that break with small UI changes
- Race conditions - not waiting for elements properly
- Assuming single matches when multiple elements exist (your original error)
- Not handling dynamic content that loads asynchronously

---

## Hidden vs Visible Text (Content Retrieval)

**.text_content()**

Gets **ALL** text content, including:
- Text hidden with CSS (`display: none`, `visibility: hidden`)
- Text inside `<script>`, `<style>` tags
- Text in hidden input fields (`<input type="hidden">`)

Example:
```html
<div style="display: none">Secret Text</div>
```
```python
print(element.text_content())  # Output: "Secret Text"
print(element.inner_text())   # Output: ""
```

**.inner_text()**

Gets **only visible** text (what a user actually sees on screen).

Example:
```html
<div>Hello <span style="display:none">World</span></div>
```
```python
print(element.text_content())  # "Hello World"
print(element.inner_text())    # "Hello"
```

**Why It Matters?**
- Use `.text_content()` when you need raw data (e.g., scraping metadata).
- Use `.inner_text()` when testing user-facing content (e.g., verifying UI text).

---

## State Checking (Explained)

State checking helps verify an element's condition before interacting with it.

| Method         | Purpose                                 | Example Use Case                        |
|----------------|------------------------------------------|------------------------------------------|
| `.is_visible()` | Checks if element is visible on the page | Verify a modal appears                   |
| `.is_hidden()`  | Checks if element is not visible         | Confirm a loading spinner disappears     |
| `.is_enabled()` | Checks if element is clickable/editable | Test if a submit button is active        |
| `.is_checked()` | Checks if checkbox/radio is selected     | Validate a "Terms & Conditions" checkbox |

Example:
```python
submit_button = page.locator("#submit-btn")

if submit_button.is_enabled():
    submit_button.click()
else:
    print("Button is disabled!")
```

---

## Action Methods (Purpose & Usage)

These simulate user interactions:

| Method    | Purpose                                     | Example           |
|-----------|---------------------------------------------|-------------------|
| `.click()`| Clicks an element (buttons, links)          | `button.click()`  |
| `.fill()` | Sets entire input value (clears existing text)| `input.fill("Hello")` |
| `.type()` | Simulates key-by-key typing (slower, like a user) | `input.type("slow text")` |
| `.press()`| Presses a single key (Enter, Tab, etc.)     | `input.press("Enter")` |
| `.hover()`| Moves mouse over element (for dropdowns/tooltips)| `menu.hover()`  |

**When to use which?**
- `fill()` → Fast form filling.
- `type()` → Testing keyboard interactions.
- `press()` → Shortcut keys (e.g., "Control+A").

---

## Waiting Strategies & Dynamic Content

### Why Wait?

Modern web apps load content asynchronously (e.g., via AJAX/APIs).

If your script tries to interact with an element before it exists, it fails.

**Common Waiting Methods:**

**Implicit Waits** (Playwright does this automatically):
```python
# Playwright retries for up to 30s (default)
page.locator(".dynamic-element").click()
```

**Explicit Waits** (manual control):
```python
# Wait for element to appear
element = page.locator(".loading-message")
element.wait_for(state="hidden")  # Wait until it disappears
```

**Network Events:**
```python
# Wait for API response before proceeding
page.wait_for_response("https://api.example.com/data")
```

**What Happens If You Don’t Wait?**
- **Race Conditions**: Your script might try to click a button before it’s loaded.
- **Flaky Tests**: Tests pass sometimes but fail randomly.

**Dynamic Content Example**
```html
<div id="results">
    <!-- Loaded via JavaScript after 2 seconds -->
</div>
```

**Bad Approach (Fails):**
```python
page.click("#load-data")  # Triggers API call
print(page.locator("#results").inner_text())  # EMPTY! Too fast!
```

**Good Approach (Waits):**
```python
page.click("#load-data")
page.locator("#results").wait_for()  # Waits until content appears
print(page.locator("#results").inner_text())  # Correct output
```

---

## Key Takeaways

- `.text_content()` vs `.inner_text()` → Hidden vs visible text.
- **State Checking** → Verify elements are ready for interaction.
- **Actions** → Simulate real user behavior (clicks, typing).
- **Waiting** → Essential for modern web apps. Always assume content loads dynamically.
