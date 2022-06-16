# return statement = functions send Python values/object back to the caller.
#                    These values/objects are known as the function's return value

number1 = input("What is number1?: ")
number2 = input("What is number2?: ")

def multiply(number1,number2):
    return number1 * number2

x = multiply(int(number1),int(number2))

print(x)

def multiply(number1,number2):
    return number1 * number2
x = multiply(6,8)

print(x)