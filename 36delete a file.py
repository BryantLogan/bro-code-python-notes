import os

path = "C:\\Users\\bryan\\Desktop\\AWS\\AWS Certifications\\Solutions Architect Associate\\code\\test.txt"

os.remove(path)

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")


