# ✅ Case 1: Calling one function from another (both top-level)
# This is most common and recommended unless you need special scoping.


def A():
    print("This is function A")

def B():
    print("This is function B")
    A()  # Calling A inside B

B()
print()
# ✅ Case 2: Defining a function inside another function
r'''
This is valid Python and useful when:

The inner function is only needed inside the outer one

You want to encapsulate logic or limit scope

You’re preparing for advanced features like closures
'''
def B():
    def A():
        print("This is function A inside B")
    
    print("This is function B")
    A()

B()
