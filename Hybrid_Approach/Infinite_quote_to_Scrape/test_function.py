def A():
    print("This is function A")

def B():
    print("This is function B")
    A()  # Calling A inside B

B()
print()
def B():
    def A():
        print("This is function A inside B")
    
    print("This is function B")
    A()

B()
