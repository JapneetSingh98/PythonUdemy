def getStatement():
    statement = input("Say something: ")
    return statement

questionID = ["Who", "What", "Where", "When", "How", "Why"]

def isQuestion(statement):
    for id in questionID:
        if statement.startswith(id):
            return True
    return False

output = ""

while True:
    statement = getStatement()
    if statement == "/end":
        break
    else:
        statement = statement.capitalize()
        if isQuestion(statement):
            statement = statement + "?"
        else:
            statement = statement + "."
    
    output = output + " " + statement

print(output[1:])
