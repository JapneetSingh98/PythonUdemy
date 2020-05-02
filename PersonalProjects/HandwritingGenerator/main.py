import os




def trainer():
    print("in trainer")

    input_char = ""
    while len(input_char) != 1:
        print("Input must be a single character.")
        input_char = input("Enter your character: ")

    path = os.getcwd()
    print ("The current working directory is %s" % path)
    directoryName = "./char_" + input_char + "_"
    print(directoryName)

    if os.path.exists(directoryName):
        print("The directory exists!")
        
    else:
        print("Does not exist. Creating directory.")
        try:
            os.mkdir(directoryName)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        




def printer():
    print("in printer")




while True:
    user_input = input("Train (T), Print (P), or Exit (end or exit): ").lower()
    print(user_input)
    if user_input == "t":
        print("Training")
        trainer()
    elif user_input == "p":
        print("Printing")
        printer()
    elif user_input == "end" or user_input == "exit":
        print("Exiting")
        break
    else:
        print("Response unclear")