# Learning Javascript 

# Types of JavaScript Rendering (By Framework)

'''
Framework	            Rendering Approach	                                                Key Scraping Challenge
React	                Virtual DOM → Updates only changed elements	                        Dynamic class names, lazy-loaded components
Angular	                Two-way data binding → Real-time updates	                        Complex dependency injection, zone.js
Vue	                    Reactive components → Similar to React	                            Scoped CSS makes element targeting harder
Svelte	                Compiles to vanilla JS → No virtual DOM	                            Less common, but very fast updates
Next.js/Nuxt	        Server-side rendering (SSR) + client-side hydration 	            Mixed content (some HTML pre-rendered)
'''

# Fundamentals of Javascript 
# These core concepts work across all JavaScript frameworks:

'''
1. DOM Manipulation Basics
    All frameworks ultimately modify the HTML DOM.
    Learn to:
    Wait for elements to appear (WebDriverWait in Selenium).
    Interact with dynamic elements (buttons, forms).
'''

'''
2. Network Request Monitoring
    All frameworks fetch data via APIs (XHR/Fetch).
    Use Chrome DevTools → Network tab to:
        Identify API endpoints.
        Replicate requests in Python.
'''

'''
3. Event-Driven Interactions
    Frameworks trigger updates on:
        Clicks (onClick).
        Scrolls (IntersectionObserver).
        Form inputs (onChange).
'''
'''
4. Shadow DOM (Advanced)
    Some frameworks (especially Angular) use Shadow DOM for encapsulation.
'''
# Universal Skills for javascript 
'''
1. How to inspect dynamic elements (React DevTools/Angular Inspector help).
2. How to intercept network requests (Chrome DevTools → Network tab).
3. How to wait for dynamic content (explicit waits in Selenium/Playwright).
DOM inspection (how elements update).
Network monitoring (where data comes from).
Event simulation (clicks, scrolls, inputs).
'''

# Practical Coverage Sheet 
'''
Scenario	                            Solution
Content loads after button click	    Use Selenium/Playwright to click and wait
Data comes from API	                    Intercept the API call with requests
Elements have dynamic classes	        Use CSS selectors like [class*="prefix-"]
Infinite scroll	                        Simulate scrolling with JavaScript injection
Shadow DOM components	                Use .shadowRoot in Selenium/Playwright
'''