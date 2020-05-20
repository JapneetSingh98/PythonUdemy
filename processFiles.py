with open("original.txt") as myfile:
    content = myfile.read()

print(content)


with open("./files/fruits.txt") as myfile:
    thisContent = myfile.read()

print(thisContent)