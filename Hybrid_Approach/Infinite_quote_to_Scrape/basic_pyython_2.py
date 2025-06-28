# To Do list Implementation 
r'''
1. Step by Step Implementation 
    A. Printing the Dictionary Stuff (Done)
    B. Combining the Concept of Time and also the Dictionary for the Randomness printing the output stuff 
    C. Creating a Set of Function into Implementing the Simulation of Human Behavior 
    D. Combining all of the Concept of it to Mouse Movement, Mouse Click, Mouse Scrolling Stuff 
'''



# I understand the Concept of Human Behaviour but i want to break down the code to really understand it 

# This is for Playwright only 
from playwright.sync_api import sync_playwright, Playwright

# What is "import random" relevance?
import random
r'''
random is one of the human behaviour because in terms of computer/bot 
it is a fixed time in doing things so i needed a variety of time in terms of executing the actions
'''
import time
r'''
time is the one that i needed to implement to create the delay of executing the action
Purpose: Pause execution (create delays) to mimic human interaction speed.
Implementation: time.sleep(delay)  # Pauses the bot for 'delay' second
    Because if you didn't put it that way: Without time.sleep(), actions would fire instantly (like a spammy bot).

'''

# This is Dictionary
base_times = {
    "click": (0.2, 0.8),
    "navigate": (1.5, 3.0),
    "scroll": (0.1, 0.5),
    "think": (2.0, 5.0)
}
# Dictionaries store key-value pairs.
# The key is a string like "click", "navigate", etc.
# The value is a tuple like (0.2, 0.8), which represents a range of time (minimum and maximum delay in seconds).
# "click": (0.2, 0.8) means a click delay will randomly be chosen between 0.2 and 0.8 seconds.

r'''

1. Why Use Dictionary what is the alternative?
    - I think because in terms of categories like click, navigate, scroll, and think

2. Why it uses a tuple?
    - What is tuple anyway?
        - tuple is immutable (doesn't change once you created it means you can't add or remove)
        - useful when i don't need to change the data 
    * Syntax: 
        mytuple = (item1, item2, item3)
    * Note: A tuple can contain elements of different types.
        coordinates = (10, 20)
        person = ("Alice", 30, "Engineer")
    * 📌 Special case – Single element tuple:
        single = (5,)  # You need the comma to make it a tuple!
        not_a_tuple = (5)  # This is just an integer
    * 🔁 Tuple Packing and Unpacking
        # Packing
        data = ("Alice", 30)

        # Unpacking
        name, age = data
        print(name)  # Alice
        print(age)   # 30
3. Conclusions:
    We Use Dictionary for Different types of action to Mimic Behaviour 
    and we use tuples for things because it doesn't really matter anyway what we use 

✅ Yes! Dictionary values are not limited to tuples. You can use:
example_dict = {
    "integer": 42,                    # int
    "string": "hello",                # str
    "list": [1, 2, 3],               # list (mutable)
    "another_dict": {"key": "value"}, # nested dict
    "tuple": (4, 5),                 # tuple (immutable)
    "function": len                  # even a function!
}
'''

# Alternative of the code and why we don't use it 
r'''
Alternatives:
- We could use a list of lists or a list of tuples, but then we would have to remember the index of each action or search by the first element.
Example: [["click", (0.2, 0.8)], ["navigate", (1.5, 3.0)], ...] 
Then to get the time for "click", we would have to loop through the list until we find the list where the first element is "click".
- We could use separate variables for each action, e.g., `click_time = (0.2, 0.8)`, but that becomes messy when we have many actions and we want to pass them around or look up by string.
'''