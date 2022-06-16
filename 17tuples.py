# tuple = collection which is ordered an unchangeable
#         used to group together related data

student =("Bryant",21,"male")

print(student.count("Bryant"))
student.index("male")
print(student.index("male"))

for x in student:
    print(x)

if "Bryant" in student:
    print("Bryant is here!")