# Higher Order Function =   a function that either:
#                           1. accepts a function as an argument OR
#                           2. returns a function
#                           (In python, functions are also treated as objects)

#def loud(text):
#    return text.upper()

#def quiet(text):
#    return text.lower()

#def hello(func):
#    text = func("Hello")
#    print(text)

# hello(quiet)
# hello(loud)

def divisor(x):  #higher order function
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))
