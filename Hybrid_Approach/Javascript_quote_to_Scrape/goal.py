# This is the Goal for Javascript Website

r'''
Hybrid Approach Gradually Implement Things

To Do List 
1. Launching a browser (chromium.launch())
    Chrome
    Firefox
    Websocket (WebKit (Safari's engine)
    Multiple Tabs 
    Multiple Browser
2. Data Extraction 
    Getting the elements Safety
    Content Retrieval 
    State Checking 
    Basic CSS/XPath selectors
    Extracting text (page.textContent(), page.$$eval())
. Navigating URL 
    Paginations 
    Paginations on Multiple Tabs 
    Pagination on Multiple Browser 
__________________________________________________
2. Hidden vs Visible Text (Content Retrieval)
.text_content()
    Gets ALL text content, including:
        Text hidden with CSS (display: none, visibility: hidden)
        Text inside <script>, <style> tags
        Text in hidden input fields (<input type="hidden">)
    Questions: Why they need to hide things?
.inner_text()
    Gets only visible text (what a user actually sees on screen). 
    Respects CSS visibility rules.

Use .text_content() when you need raw data (e.g., scraping metadata).
Use .inner_text() when testing user-facing content (e.g., verifying UI text).

2. State Checking (Explained)
Method              Purpose                                                     Example Use Case
.is_visible()	    Checks if element is visible on the page	                Verify a modal appears
.is_hidden()	    Checks if element is not visible (or doesn't exist)	        Confirm a loading spinner disappears
.is_enabled()	Checks if element is clickable/editable (not disabled)	        Test if a submit button is active
.is_checked()	Checks if checkbox/radio is selected	Validate a "Terms & Conditions" checkbox
'''