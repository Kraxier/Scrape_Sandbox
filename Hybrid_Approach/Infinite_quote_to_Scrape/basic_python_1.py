# Back to the Basic for Building the Human Bot


import random

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

# Getting the Dictionary 
# Storing the value of min_time and max_time 
min_time, max_time = base_times["click"]
random_num = random.uniform(min_time, max_time)
print(f"Printing the Random Number Between the Data in Keys {random_num}")

# The Goal is to randomize the Behaviour of my Human thing based on the Random Number of stuff 

# Learning this is also require getting the random keys and random data inside that time thing 
random_key = random.choice(list(base_times.keys()))
print(f"Printing the random Keys in the Dictionary itself which is: {random_key}")

min_time, max_time = base_times["think"]
random_num = random.uniform(min_time, max_time)
print(f"Printing the Random Number Between the Data in Keys {random_num}")

# Basically i can randomize the Human Bot that i'm Creating thing but this is based only on time thing


