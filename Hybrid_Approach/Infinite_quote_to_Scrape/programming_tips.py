# Programming Tips:
r'''
Problem: 
    As i code i quite notice that even if i write the code myself it is hard to debug things and understand my code
    So here are Some Things i needed to do in order the Future me and other Developer Understand the Code 

'''

# ======================
# Workflow 
# ======================

r'''
1. Intial Phase
    A. Before Writing any Code Think like a "Problem Solver"
    B. Write Comments First Outlining the Approach you Will need to take
    C. Write a Messy Code 
    D. Refactoring the Code 
        1. Using Meaninful names (Self-Documenting Code)
        2. Adding Comments focusing on "Why" not on "What"
        3. Breaking Down Complex Function 
            < 20 Lines is Ideal
            < 50 Lines are Acceptable 
            > 50 Lines Need refactoring 
        4. Adding Docstring
            What is Docstring?
                Docstring appear right after the Function method, Class or module used to describe
                what the code does, and it's accessible via introspection (like using the help() function in Python).
            Examples: 
            
            def greet(name):
                """
                This function takes a name as input and returns a greeting message.
                
                Parameters:
                name (str): The name of the person to greet.

                Returns:
                str: A greeting string.
                """
                return f"Hello, {name}!"
        5. Visual Organization
            Use whitespace and dividers:
            # ======================
            # SCROLLING OPERATIONS
            # ======================
            def scroll_to_bottom(page):
                # ...

            # ======================
            # DATA EXTRACTION
            # ======================
            def extract_quotes(page):
                # ...
'''
# ======================
# Realization
# ======================

r'''
Don't Get Stuck Too much in Doing like this but focus on just creating version first and then Edit Later so basically this is for Editing in terms of Writing 
Create Create Create First and then Edit Later for Finishing Touch of these basically make it Work First 
'''
