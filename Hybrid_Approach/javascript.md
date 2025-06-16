
# 🕷️ Core Scraping Concepts

### Q1: Why does `test_1.py` use `urljoin()` for pagination instead of direct `href` values?  
**A1:** To correctly handle relative URLs by combining them with the base URL. This ensures reliable navigation even if the site's structure changes.

### Q2: When would you choose `.text_content()` over `.inner_text()` for element extraction?  
**A2:** Use `.text_content()` for raw data extraction, including hidden elements (e.g., metadata). Prefer `.inner_text()` when verifying content visible to users.

### Q3: What happens in `test_1.py` if the site has fewer than 5 pages?  
**A3:** `next_page.get_attribute('href')` returns `None`, so `urljoin()` defaults to the base URL, effectively reloading page 1.

---

# 🧱 Architecture & Anti-Detection

### Q4: According to `browser_context.py`, when should isolated contexts be used?  
**A4:** For handling logins, maintaining separate sessions, or evading bot detection on sites that track user behavior.

### Q5: What are 3 key differences between **multiple tabs** vs **multiple browsers**?  
**A5:**  
- Tabs share memory/cache (lightweight); browsers are fully isolated  
- Tabs share cookies/sessions; browsers use separate sessions  
- Browsers are more resource-heavy than tabs

### Q6: Why does the Advanced Scraper (Step 5) use both `context.route()` and user-agent rotation?  
**A6:**  
- `context.route()` disables caching to prevent stale data detection  
- User-agent rotation mimics diverse users to avoid fingerprinting

---

# ⚙️ Implementation Nuances

### Q7: Why is `next_page.count() == 0` used in `goal.py` instead of checking visibility?  
**A7:** The "Next" button might exist in the DOM but be hidden. `count()` checks for presence regardless of visibility.

### Q8: What cleanup risk exists in `test_1.py` during exceptions?  
**A8:** `page.close()` and `browser.close()` might not be called. **Best practice:** Use `try/finally` blocks or context managers.

---

# 🤔 Decision Making

### Q9: When to use **Step 2 (multi-tab)** over **Step 5 (advanced)**?  
**A9:** For small-scale jobs (dozens of pages) without serious bot detection. Step 5 is overkill for simple scraping tasks.

### Q10: What metric triggers concurrency scaling down in Step 5?  
**A10:**  
- Success rate < 70%  
- Average task time > 10s  
Helps prevent resource exhaustion and detection.

---

# 🌐 Browser Mechanics

### Q11: How do shared cookies between tabs pose scraping risks?  
**A11:** Identical sessions across tabs can flag unnatural behavior, leading to blocking. Use separate contexts to isolate sessions.

### Q12: Why disable cache via `context.route()` for dynamic content?  
**A12:** Ensures fresh responses and avoids serving stale/bot-specific content — essential for JavaScript-heavy sites.

---

# ❗ Error Handling

### Q13: What’s missing in `goal.py` for production-readiness?  
**A13:**  
- Network error handling  
- Retry mechanisms  
- Rate limiting  
- Guaranteed cleanup (close browser/pages)

---

# 🕵️ Anti-Detection

### Q14: Why combine random delays (1–3s) with user-agent rotation?  
**A14:**  
- Delays reduce request burst patterns  
- User-agent rotation prevents fingerprinting  
Together they simulate human browsing behavior.

### Q15: When should `bypass_csp=True` be enabled in context creation?  
**A15:** Only when Content Security Policies block needed resources. Use sparingly — it increases detection risk.

---

# 🚀 Optimization

### Q16: Why does Step 5 limit threads using `max_tabs`?  
**A16:**  
- Prevents memory overload  
- Avoids suspicious parallel requests  
Concurrency is scaled gradually based on success rate.

---

# 🔧 Practical Implementation

### Q17: How would you modify `test_1.py` to:  
#### a) Handle dynamic content loading?  
**A17a:** Add `page.wait_for_selector(".quote")` before scraping.

#### b) Rotate user agents?  
**A17b:** Pass `user_agent` to `browser.new_context()` and implement rotation logic.

---

# 🧠 Concept Integration

### Q18: What 4 learning principles from `test_1.py` apply to the Advanced Scraper?  
**A18:**  
1. **Active manipulation** (e.g., change `max_tabs`)  
2. **Verbalization** (explain context usage)  
3. **Prediction** (forecast memory usage)  
4. **Problem solving** (e.g., adding proxy support)

---

# 🧪 Debugging

### Q19: Why is Firefox faster in `goal.py` but Chromium preferred?  
**A19:** Chromium mimics most real users, making it less detectable. Firefox may trigger bot heuristics due to its optimized performance.

### Q20: If `page.locator(".text")` returns empty in `goal.py`, what could be the issue?  
**A20:**  
- JavaScript didn’t execute: use `page.wait_for_load_state('networkidle')`  
- Changed CSS selectors: inspect using DevTools  
- Content is inside an iframe: switch to the correct frame
