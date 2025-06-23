r'''
Q1: What's the core challenge when scraping quotes.toscrape.com/js-delayed/?
<details> <summary>Click for answer</summary>
A: The quotes are loaded asynchronously via JavaScript after the initial page load. Traditional scraping would fail because the content isn't immediately available in the DOM when page.goto() completes.

</details>
Q2: Why is time.sleep() a suboptimal solution for JS-delayed content?
<details> <summary>Click for answer</summary>
A:

Fixed delays waste time (waiting longer than needed) or fail (if delays are too short)

No adaptability to network speed or content load times

Inefficient for large-scale scraping

</details>
Q3: How does page.wait_for_selector() solve the JS delay problem?
<details> <summary>Click for answer</summary>
A: It uses explicit waits that:

Poll the DOM until elements appear

Respect the timeout setting (12s in the code)

Proceed immediately when content loads

Throw actionable errors on failure

</details>
Q4: What's the critical mistake in this implementation?
python
quotes = page.wait_for_selector(".quote .text", timeout=12000)
for quote in quotes: ...
<details> <summary>Click for answer</summary>
A: wait_for_selector() returns a single ElementHandle, not a list. The correct approach is:

python
page.wait_for_selector(".quote .text", timeout=12000)  # Wait for FIRST quote
quotes = page.locator(".quote .text").all()  # Then get ALL quotes
</details>
Q5: Why is expect(locator).to_have_count() better than wait_for_selector()?
<details> <summary>Click for answer</summary>
A: While both work:

expect() automatically retries and handles flaky networks

Can assert on element count (e.g., wait for 10 quotes)

More readable for complex conditions

python
expect(page.locator(".quote")).to_have_count(10, timeout=12000)
</details>
Q6: When would you use page.wait_for_function()?
<details> <summary>Click for answer</summary>
A: For custom JS conditions like:

python
page.wait_for_function(
    "document.querySelectorAll('.quote').length > 5",
    timeout=12000
)
Use cases:

Waiting for specific number of items

Checking complex DOM states

Content depending on JS calculations

</details>
Q7: What's wrong with this navigation approach?
python
page.goto(next_page_url)
print(f"Scraping {page.url}")
quotes = page.locator(".quote .text").all()
<details> <summary>Click for answer</summary>
A: It lacks a wait after navigation. Fix by:

python
page.goto(next_page_url)
page.wait_for_selector(".quote .text", timeout=12000)  # CRITICAL!
quotes = page.locator(".quote .text").all()
Every navigation requires re-waiting for dynamic content.

</details>
Q8: Why avoid page.wait_for_timeout(5000)?
<details> <summary>Click for answer</summary>
A: It's a fixed delay that:

Wastes time (if content loads in 1s)

Fails unpredictably (if content takes 6s)

Makes scripts slower and flaky

</details>
Q9: How does the expect() method benefit web scraping?
<details> <summary>Click for answer</summary>
A:

Built-in retries handle transient failures

Concise assertions (visibility, count, text)

Avoids manual wait implementations

Synchronizes with Playwright's auto-waiting

python
expect(page.locator(".quote")).to_be_visible(timeout=10000)
</details>
Q10: What's the key takeaway for scraping JS-heavy sites?
<details> <summary>Click for answer</summary>
A: Always combine:

Navigation triggers (goto(), click())

Explicit waits for dynamic content

Locator operations only AFTER waits

python
page.goto(url)
page.wait_for_selector(content_selector)  # WAIT FIRST!
content = page.locator(content_selector).all()  # THEN EXTRACT
</details>
Debugging Insights from Errors:
AttributeError: 'list' object has no attribute 'is_visible'
→ You called is_visible() on a list of elements. Call it on individual elements instead.

UnboundLocalError: cannot access local variable 'quote'
→ The quotes list was empty. Always check if elements exist before iteration.

TypeError: 'ElementHandle' object is not iterable
→ Treated a single element handle as a list. Use .all() for collections.
'''