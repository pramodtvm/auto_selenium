from excersise1 import parentclass

class child(parentclass):

    def __init__(self, newVar,kidage =10):
        print("initialization started Boys")
        self.brand = None
        #self.momage = None
        self.kidage = kidage
        self.dude = newVar

    def chilfunc(self):
        self.kidage = self.kidage + 1
        self.brand = "Puma"
        self.trnd = 66
        print("reached new plans", self.kidage)

    def calculateparent(self):
        value = super().varint
        totalage = value + self.kidage
        print("printing total age",totalage )


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()
