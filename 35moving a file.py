import os

source = "C:\\Users\\bryan\\Desktop\\AWS\\AWS Certifications\\Solutions Architect Associate\\code\\test.txt"
destination = "C:\\Users\\bryan\\Desktop\\Photography"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
