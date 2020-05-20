with open("original.txt") as myfile:
    content = myfile.read()

print(content)


with open("./files/veegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")

