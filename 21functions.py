# function = a block of code which is executed only when it is called.

from unicodedata import name


def hello(first_name, last_name, age):
    print("hello, " +first_name +last_name)
    print("you are " +str(age) +" years old")
    print("have a nice day!")


hello("Bryant ","Logan", 21)