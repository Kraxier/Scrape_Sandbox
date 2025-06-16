# The Pareto Principle for Playwright: 10% Features for 90% Results in Web Scraping



# page.evaluate() - The 10% that gives 90% of data extraction power
r''' Essential Use Cases (80% of scraping needs):
# 1. Extract page metadata
title = page.evaluate('document.title')
url = page.evaluate('window.location.href')

# 2. Get text content from elements
heading = page.evaluate('document.querySelector("h1").innerText')

# 3. Extract lists of data
quotes = page.evaluate('''() => {
    # return Array.from(document.querySelectorAll('.quote'))
        # .map(el => el.innerText)
}''')

# 4. Extract attribute values
links = page.evaluate('''() => {
    # return Array.from(document.querySelectorAll('a'))
        # .map(a => a.href)
}''')

# 5. Get page dimensions
scroll_y = page.evaluate('window.scrollY')
full_height = page.evaluate('document.body.scrollHeight')
'''

# 2. page.mouse.wheel() - The 10% that solves 90% of scrolling needs
r'''
# 1. Scroll to trigger lazy-loaded content
page.mouse.wheel(0, 500)  # Scroll down 500px

# 2. Scroll to bottom in increments
for _ in range(5):
    page.mouse.wheel(0, 1000)
    page.wait_for_timeout(1000)  # Wait for content to load

# 3. Scroll specific element into view
element = page.query_selector('.target')
box = element.bounding_box()
page.mouse.wheel(0, box['y'] - 200)  # Scroll to position above element

# 4. Horizontal scrolling (for rare cases)
page.mouse.wheel(300, 0)  # Scroll right 300px
'''

# 3. page.wait_for_function() - The 10% that handles 90% of waiting needs
r'''
# 1. Wait for content to load after scroll
page.mouse.wheel(0, 1000)
page.wait_for_function('''() => {
    # return document.querySelectorAll('.item').length > 10
}''')

# 2. Wait for AJAX completion
page.wait_for_function('''() => {
    # return window.dataLoaded === true
}''')

# 3. Wait for scroll position
page.mouse.wheel(0, 1500)
page.wait_for_function('window.scrollY > 1000')

# 4. Wait for element state change
page.wait_for_function('''() => {
    # const el = document.querySelector('.status');
    # return el && el.innerText.includes('Complete');
}''')
'''