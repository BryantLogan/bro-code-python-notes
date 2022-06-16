try:
    with open("C:\\Users\\bryan\\Desktop\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")