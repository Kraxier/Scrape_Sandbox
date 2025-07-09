# Explicit Waiting

r'''
Go Back to JS delayed to Implement All of this Stuff 
'''

r'''
Explicit Waiting means pausing the script until a certain conditions are met 

This Help ensure that your script interact with elemenets only when they are ready 

Avoiding Errors Due to Elements not being loaded or visible or enable yet

🔍 Why Use Explicit Waiting?
Web pages can be dynamic — elements might take time to:
    Load from the server
    Appear after animations
    Become enabled or clickable
Without waiting properly, your script might try to interact with something that’s not ready, leading to flaky tests.

🧠 What Is Explicit Waiting
    “Wait for a specific condition before moving on.”

1. Wait for an element to be visible:
page.locator("#submit-button").wait_for(state="visible")
page.locator("#submit-button").click()

2. Wait for a specific selector:
page.wait_for_selector("div.result")

3. Wait for a URL to change: # I can Implement this in Login State
page.click("text=Login")
page.wait_for_url("**/dashboard")

4. Wait for the page to load completely:
page.wait_for_load_state("networkidle")

🚫 Avoid This When Possible:
page.wait_for_timeout(3000)  # Waits 3 seconds regardless
Use condition-based waits instead — they are faster and more reliable.

'''

# How i can Implement this in Infinite Scrolling? 
r'''
Always put this part 
    page.wait_for_load_state("networkidle")

Wait for an element to be visible 
'''
# JS Delayed is the Proper Website for this as i study this part 
# It Wait the damn things before procceeding 

r'''
For Infinite Scrolling there are no lazy content 
I just needed to reach a certain point and then a new content will appear 
'''