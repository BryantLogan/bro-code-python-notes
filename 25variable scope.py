# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Logan" #global scope = available inside & outside of functions

def display_name():
    name = "Bryant"    #local scope (available only inside this function)
    print(name)

display_name()
print(name)

#L = Local
#E = Enclosing
#G = Global
#B = Built-in