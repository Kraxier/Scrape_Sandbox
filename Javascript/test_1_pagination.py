# Solving the Problem of Pagination in Playwright
# python test_1_pagination.py


# First Version of the Code and there are Problem here 

r'''
I'm Trying to get the .next a in this code next_page = page.locator('.next a').get_attribute('href')
but the problem is if it go to the last page it give "None" and Playwright crashes this is why we need to check 
the Element first before getting something


'''

# Running the Code will not Stop 

# learning how to Debug
# What does it mean by Debugging? 
r'''
Debugging means fixing the errors so its means identifying the errors and analyzing the errors and solving the errors

Bug is called when a program behave unexpectedly or the software program crashes 


Debugging Techqniue 
    1. Print Statement 
    2. Debugger 
In terms of Debugging i quite notice because there are different types of errors 
based on the library or module but i ask this question to deepseek: 

"In terms of error why it give me "line 628" but my program is line 108 only ?"
But it shows that even in the library errors that over in my code which currently as writing is 108 
it show the line 628 (For Example) that the libraries itself have internal functions or deep internal logic
but it still show where i can focus based on the line of my code

In terms of Error it give me this part 
 File "C:\Users\klabi\OneDrive\Desktop\Scrape_Quotes_To_Scrape\Javascript\test_1_pagination.py", line 41, in run
    next_page = page.locator('.next a').get_attribute('href')

Which show my location of my files in program and it show the error 

The Deep Internal Logic or Internal Functions of the Playwright is this 
 File "C:\Users\klabi\OneDrive\Desktop\Scrape_Quotes_To_Scrape\venv_PS_Toscrape\Lib\site-packages\playwright\_impl\_locator.py", line 418, in get_attribute
    return await self._frame.get_attribute(

Which show the playwright libraries it self but i want to focus on my code because i think it is rarely the library is the problem


Feedback of Deepseek regarding of my Reflection on Debugging Stuff 
Library vs Code Traceback 
    1. Assume in the First Place that it's my fault because its 99% of the time the bug is in my code 
    2. Famous Libararies are Well Tested (This is Outside my Expertise)


Let's Go back Debugging the Error of my COde after the Introduction of Learning to Debug things 
Realize that I just Copy Paste the Error of my Code to Chatgpt or Deepseek in order to understand it but it just give me the conclusions
that i don't really understand what is currently happening 
    Cons on Depending on AI:
        1. Beginners might apply fixes without understanding them, leading to tech debt.
    Pros
        1. Instant Structured Explanations 
Think of AI as a 24/7 senior dev teammate—great for brainstorming, but not a substitute for critical thinking. 🛠️

Going back to my code 
next_page = page.locator('.next a').get_attribute('href') 
This is the problem - - waiting for locator(".next a")

This means Playwright are waiting for the "Next Button" but currently i'm at the last page 
so the problem is playwright should not wait but playwright is waiting so i need some catching things that if there are no next button 
the program will stop 

Identifying the Core Problem or Issue is really i needed to learn as a programmer 
'''

# Realize i can basically interact in the browser because i try to click it 
'''
The Thing is the Program will still run based on the Logic of my program
'''

# my Old Code where paginations is the problem 
# from playwright.sync_api import sync_playwright, Playwright
# from urllib.parse import urljoin

# def run(playwright: Playwright):
#     base_url = "https://quotes.toscrape.com/js/"
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False) 
#     page = browser.new_page()
#     page.goto(base_url)
#     while True: 
#         next_page = page.locator('.next a').get_attribute('href')
#         r'''
#         In this line of code deepseek said .get_attribute('href') that playwright will wait until 
#         the next button will appear so it will hang on the last page 

#         i needed a way to get the href attribute 
#         '''

#         # but i have a print statement regarding of this 
#         if next_page is None:
#             print("No more pages. Stopping.")
#             break  # Stop the loop if there's no next page
#         next_page_url = urljoin(base_url, next_page) 
#         print(next_page_url)

#         page.goto(next_page_url)
#     page.close() 
#     browser.close()

    

# with sync_playwright() as playwright:
#     run(playwright)



from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin

def run(playwright: Playwright):
    base_url = "https://quotes.toscrape.com/js/"
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto(base_url)
    while True: 
        next_page = page.locator('.next a')

        # .count() 
        r'''
        .count count the number of DOM elements that match my locator
        this also means i can find out the DOM elements numbers 

        but it will return 0 if no elements exist but it can return a "Number" if elements exist

        '''
        if next_page.count() == 0:
            print("Reached last page. Stopping.")
            break

        if next_page is None:
            print("No more pages. Stopping.")
            break 
        # next_page.get_attribute('href') which is after locating it i can modify it either by printing the content or 
        # getting the Attribute itself 
        # If the element doesn’t exist, .get_attribute() waits until timeout (default: 30s), then throws TimeoutError.
        # It doesn’t return None unless the attribute itself is missing (e.g., <a> has no href).
        next_page_url = urljoin(base_url, next_page.get_attribute('href')) 
        print(next_page_url)

        page.goto(next_page_url)
    page.close() 
    browser.close()

    

with sync_playwright() as playwright:
    run(playwright)









r'''
This Part 
        # Check if the .next a element exists first
        next_link = page.locator('.next a')
        if next_link.count() == 0:
            print("No more pages.")
            break  # Exit loop safely

And This Part 
        # Now safe to get href
        next_href = next_link.get_attribute('href')
        next_page_url = urljoin(base_url, next_href)
        print(f"Going to: {next_page_url}")
        page.goto(next_page_url)

'''
# from playwright.sync_api import sync_playwright, Playwright
# from urllib.parse import urljoin

# def run(playwright: Playwright):
#     base_url = "https://quotes.toscrape.com/js/"
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto(base_url)

#     while True:
#         # Check if the .next a element exists first
#         next_link = page.locator('.next a')
#         if next_link.count() == 0:
#             print("No more pages.")
#             break  # Exit loop safely

#         # Now safe to get href
#         next_href = next_link.get_attribute('href')
#         next_page_url = urljoin(base_url, next_href)
#         print(f"Going to: {next_page_url}")
#         page.goto(next_page_url)

#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
