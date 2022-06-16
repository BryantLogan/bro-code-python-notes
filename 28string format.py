#str.format() = optional method that gives users
#               more control when displaying output

#animal = "cow"
#item = "moon"

#print("The "+animal+" jumped over the "+item)

#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

#name = "Bryant"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you".format(name)) #10 spaces
#print("Hello, my name is {:<10}. Nice to meet you".format(name)) #left-alight
#print("Hello, my name is {:>10}. Nice to meet you".format(name)) #right-align
#print("Hello, my name is {:^10}. Nice to meet you".format(name)) #center-align

number = 1000

print("the number is {:,}".format(number)) #add comma to 1000th places
print("the number is {:b}".format(number)) #binary
print("the number is {:o}".format(number)) #octale
print("the number is {:X}".format(number)) #Hexadecimal
print("the number is {:e}".format(number)) #scientific notation