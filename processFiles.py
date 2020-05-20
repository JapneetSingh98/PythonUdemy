with open("original.txt") as myfile:
    content = myfile.read()

print(content)


with open("./files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")


'''    this will return error because vegetables.txt already exists

with open("./files/vegetables.txt", "x") as myfile:
    myfile.write("Okra")
'''


with open("./files/vegetables.txt", "a+") as myfile:
    myfile.write("\nSpinach")
    myfile.seek(0)
    newContent = myfile.read()

print(newContent)