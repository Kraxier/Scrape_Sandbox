# Concepts 

# Data Extraction 
    # Sub Parts
        # 🛡️ Getting the Elements Safely
r'''
        Try/except blocks to catch errors:
        Goal: Ensure your script doesn't break when an element is missing or late to load.
        try:
            element = page.locator('.quote')
        except:
            print("Element not found.")

'''

        # 🧾 Content Retrieval
r'''
        Goal: Once you've located an element, get its content.

        element.text_content(): Gets the visible text inside an element.

        element.get_attribute('href'): Gets a specific HTML attribute.

        page.content(): Gets the entire page's HTML.

        element.inner_text(): Get the Visible Thing 
'''
        # 🔍 State Checking
r'''
Method              Purpose                                                     Example Use Case
.is_visible()	    Checks if element is visible on the page	                Verify a modal appears
.is_hidden()	    Checks if element is not visible (or doesn't exist)	        Confirm a loading spinner disappears
.is_enabled()	    Checks if element is clickable/editable (not disabled)	    Test if a submit button is active
.is_checked()	    Checks if checkbox/radio is selected	                    Validate a "Terms & Conditions" checkbox
'''
        # 🎯 Basic CSS/XPath Selectors This should be Done 

        # Extracting text (page.textContent(), page.$$eval())



# Conclusion inner_text() vs text_content()
r'''
Try First the text_content if it is cleaned go for it 
But if it is not cleaned data go to inner_text() and look for the Challenge there
'''

# ✅ inner_text()
r'''
Returned the Text what i can currently see in the browser 
'''
# ✅ text_content()
r'''
Returns: the raw text inside the element, regardless of visibility or layout. and Includes: hidden text, and preserves all whitespace and newlines as in the HTML source
Faster: Doesn't wait for rendering or visibility.
'''

# ✅ inner_text() ✔️ Advantages (for web scraping)
r'''
1. Clean output: Gives you only the visible, user-facing text, which is usually what scrapers want.
2. Whitespace is normalized: Easier to work with programmatically.
3. Ignores hidden elements: Avoids accidental capture of unwanted or misleading data (like hidden SEO text or JavaScript-generated labels).
4. Ideal for user-facing content: Great when scraping articles, reviews, or product descriptions.
'''
# ✅ inner_text() ❌ Disadvantages
r'''
1. Slower: It waits for the page to fully render and the element to become visible.
2. Might miss data: If important content is hidden (e.g. behind tabs, accordions, or for screen readers), it won’t be included.
3. JavaScript dependency: Requires the browser to fully execute scripts — if rendering fails, text may be missing.
'''

# ✅ text_content() ✔️ Advantages (for web scraping)
r'''
1. Faster: Does not wait for visibility/rendering — great for large-scale scraping where speed matters.
2. Full HTML text: Useful for capturing all content, including hidden text, comments, or dynamic placeholders.
3. Better for debugging: You can see everything the DOM contains.
'''
# ✅ text_content() ❌ Disadvantages
r'''
1. Includes hidden text: Might capture text that’s not actually shown to users, which can pollute your data.
2. Messier output: Whitespace, line breaks, and formatting can be inconsistent or excessive.
3. More cleanup needed: Often needs post-processing or regex to get usable results.
'''
# ✅ Rule of Thumb
r'''
1. Use inner_text() when you're scraping visible user content like articles, 
headlines, reviews, or prices.

2. Use text_content() when you're scraping for raw or technical data, 
or you want to capture everything including hidden fields (e.g., for analysis or reverse engineering).
'''