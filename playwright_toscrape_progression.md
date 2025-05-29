# Playwright Progression Plan using toscrape.com

A structured progression plan to implement and master Playwright skills using the `toscrape.com` endpoints, from beginner to advanced. Each step builds on the previous one, with practical examples.

---

## 1. Foundational Skills (Basic Playwright)

**Goals:** Launch browser, navigate pages, extract static content  
**Endpoints:** Default, Random

### Skills to Practice
- Launching a browser (`chromium.launch()`)
- Navigating to a URL (`page.goto()`)
- Extracting text (`page.textContent()`, `page.$$eval()`)
- Basic CSS/XPath selectors

### Example (Default Endpoint)
```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto('http://toscrape.com/default');

  // Extract all quotes
  const quotes = await page.$$eval('.quote', elements =>
    elements.map(el => el.textContent.trim())
  );
  console.log(quotes);

  await browser.close();
})();
```

---

## 2. Dynamic Content Handling

**Goals:** Wait for JavaScript/AJAX content, handle delays  
**Endpoints:** JavaScript, Delayed

### Skills to Practice
- Explicit waits (`page.waitForSelector()`)
- Timeout handling (`page.waitForTimeout()`)
- Debugging dynamic DOM changes

### Example (Delayed Endpoint)
```javascript
await page.goto('http://toscrape.com/delayed?delay=5000'); // 5-second delay

// Wait for content to load
await page.waitForSelector('.quote', { timeout: 10000 });
const quotes = await page.$$eval('.quote', els =>
  els.map(e => e.textContent)
);
```

---

## 3. Pagination & Infinite Scroll

**Goals:** Scrape multi-page data, handle infinite scroll  
**Endpoints:** Scroll, Default (pagination)

### Skills to Practice
- Clicking "Next" buttons (`page.click()`)
- Detecting scroll end (loop + `window.scrollTo`)
- Combining waits with actions

### Example (Infinite Scroll)
```javascript
await page.goto('http://toscrape.com/scroll');
let previousHeight = 0;

while (true) {
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(2000);
  const newHeight = await page.evaluate(() => document.body.scrollHeight);
  if (newHeight === previousHeight) break;
  previousHeight = newHeight;
}

const quotes = await page.$$eval('.quote', els => els.map(e => e.textContent));
```

---

## 4. Form Interactions & Logins

**Goals:** Submit forms, handle CSRF tokens  
**Endpoints:** Login, ViewState

### Skills to Practice
- Filling inputs (`page.fill()`)
- Submitting forms (`page.click()`)
- Extracting hidden tokens (e.g., `csrf_token`)

### Example (Login Endpoint)
```javascript
await page.goto('http://toscrape.com/login');

await page.fill('#username', 'fakeuser');
await page.fill('#password', 'fakepass');
await page.click('button[type="submit"]');

// Wait for post-login redirect
await page.waitForURL('http://toscrape.com/logged-in');
console.log('Logged in!');
```

---

## 5. Messy HTML & Advanced Selectors

**Goals:** Parse tables, nested elements, unconventional layouts  
**Endpoints:** Tableful

### Skills to Practice
- Chained selectors (`:has-text()`, `>>`)
- Table scraping (`<table>` to JSON)
- Handling malformed HTML

### Example (Tableful Endpoint)
```javascript
await page.goto('http://toscrape.com/tableful');

const tableData = await page.$$eval('table tr', rows =>
  rows.map(row =>
    Array.from(row.querySelectorAll('td')).map(cell => cell.textContent)
  )
);
console.log(tableData);
```

---

## 6. Advanced: AJAX & ViewState

**Goals:** Handle AJAX filters, stateful forms  
**Endpoints:** ViewState

### Skills to Practice
- Intercepting network requests (`page.route()`)
- Modifying form data before submission
- Handling `__VIEWSTATE` (common in ASP.NET)

### Example (ViewState Endpoint)
```javascript
await page.goto('http://toscrape.com/viewstate');

await page.waitForSelector('#filter-results');

await page.selectOption('#author-filter', 'Albert Einstein');
await page.waitForSelector('.quote');

const quotes = await page.$$eval('.quote', els =>
  els.map(e => e.textContent)
);
```

---

## 7. Randomization & Edge Cases

**Goals:** Handle non-deterministic behavior  
**Endpoints:** Random

### Skills to Practice
- Retry logic (e.g., if element disappears)
- Random delays (`page.waitForTimeout(Math.random() * 3000)`)

### Example (Random Endpoint)
```javascript
await page.goto('http://toscrape.com/random');

const maxRetries = 3;
let quote;
for (let i = 0; i < maxRetries; i++) {
  quote = await page.$eval('.quote', el => el.textContent).catch(() => null);
  if (quote) break;
  await page.waitForTimeout(1000);
}
console.log(quote || 'Not found');
```

---

## 📊 Progression Summary

| Level        | Endpoints            | Key Skills                          |
|--------------|----------------------|-------------------------------------|
| Foundational | Default, Random      | Basic extraction, selectors         |
| Dynamic      | JavaScript, Delayed  | Waits, timeout handling             |
| Pagination   | Scroll, Default      | Infinite scroll, multi-page scraping|
| Forms        | Login, ViewState     | CSRF, AJAX forms                    |
| Messy HTML   | Tableful             | Advanced selectors, table parsing  |
| Edge Cases   | Random               | Retry logic, randomization         |

---

## 🔧 Next Steps
- **Combine Techniques**: Scrape Login + ViewState together.
- **Add Error Handling**: Use `try/catch` for robustness.
- **Optimize Speed**: Parallelize tasks (e.g., `Promise.all`).
- **Mock Anti-Bot**: Simulate human-like delays/mouse movements (optional).