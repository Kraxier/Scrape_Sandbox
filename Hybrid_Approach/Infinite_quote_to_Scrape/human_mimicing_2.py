import time 
import random 

r'''
Relearning the Import Module of "Time" and Observe the Randomness of Thing the seconds it take to do the Stuff 
'''

base_times = {
    "click": (0.2, 0.8),
    "navigate": (1.5, 3.0),
    "scroll": (0.1, 0.5),
    "think": (2.0, 5.0)
}

# print("Start")
# time.sleep(2)  # Sleep for 2 seconds
# print("End after 2 seconds")



# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Go!")

# r'''
# Mostly i will use time.sleep(2) or Randomize it Man 
# '''

# print("Start")
# print(f"Bot are Currently Thinking")
# min_time, max_time = base_times["think"]
# random_num = random.uniform(min_time, max_time)
# print(f"Printing the Random Number Between the Data in Keys {random_num}")
# time.sleep(random_num)
# print(f"Bot are Done Thinking")

r'''
Based on the basics Stuff the I Currently Learning i needed to randomize the Stuff that i needed to do so I needed to do this properly 

Click
Think
Navigate
scroll 

Create a Loop where in those 5 times is it a random thing where just going with the loop and mimicing action of the website 
'''
for x in range(1,5):
    # Picking a Random Keys
    random_key = random.choice(list(base_times.keys()))
    min_time, max_time = base_times[random_key]
    random_num = random.uniform(min_time, max_time)
    r'''
    Problem with here is the ration between think,navigate,think and scrolling but later is that for optimization thing 
    '''
    print("Start")
    print(f"Bot are currently Doing {random_key}")
    print(f"Printing the Random Number Between the Data in Keys {random_num}")
    # Randomize the Time it Will Take
    time.sleep(random_num)
    print("Stop")



# Critisizing the Code
r'''
1. The Problem is 
    1. The Ratio between the 4 Movements which i can certainly fix 
    2. I don't need to randomly pick one of the action keys in here 
    3. Randomly Selecting Delay Types without performing the actual action
    4. Ratio Mismatch for example is spending more time thinking than clicking 
    5. Missing Action 

Let's Implement this part 
'''

# Evaluating the Human Interactions depending on the website 
# Basically a Framework that maps Common Human Interaction on Website to integrage Stealth Behaviours 

r'''
Context 
    1. Slowing Down on Night Hours 
    2. Initial page load {Scanning and Reading}
    3. Pre action Hesitation {Decisions}
    4. Clicking near the Target 
    5. error in blicking 
    6. Natural Click Movement 

Variable Scroll Patterns: Combine small scrolls (reading) with large jumps
Error Injection: Simulate natural mistakes (misclicks, typos)
Time-of-Day Awareness: Slower interactions during night hours
Non-Linear Navigation: Random back/forward/refresh actions
Action Sequencing: Combine mouse movements, delays, and keyboard actions

Implementation
    1. Error Chance 
    2. 
'''

# Focusing in 20% Effort for 80% Results in terms of Human Mimicing Behaviour 
r'''
1. Pre-Action Delays (The 50% Solution)
    Insert before EVERY interaction (click, type, etc.)
    Why it matters: Bots act instantly, humans hesitate
    Implementation: pre_action_delay() before every action
2. Human-Like Mouse Movements (30% Solution)
    Curved paths instead of straight lines
    Variable speed during movement
    Why it matters: Straight-line movement is #1 bot indicator
3. Chunked Scrolling with Variable Pauses (20% Solution)
    Never scroll full page at once
    Vary scroll distance and speed
    Exponential pauses between chunks

    
Add a Short Random Delay
Simulate Curve Movement 
Scroll in parts with Pauses 

'''

# To Do List
r'''
1. Add the Short Random Delay in playwright 
2. Simulate the Curve Movement of the Mouse 
3. Scroll in parts with Pauses 

and I'm Done with Human Mimicing Behaviours 



'''

# Additioal Info for Login State
r'''
🔑 3. Type Like a Human 
    Why it matters: page.fill() is too fast and robotic.
    def type_like_human(element, text):
    for char in text:
        element.type(char)
        time.sleep(random.uniform(0.05, 0.25))  # Human typing delay

type_like_human(page.locator("#username"), "realUser123")

🔑 1. Use a Real Browser Context with Persistent Session
Why it matters: Headless browsers and ephemeral sessions are strong bot signals.

What to do:
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(user_agent="your-custom-UA", viewport={"width": 1280, "height": 720})
    page = context.new_page()

'''