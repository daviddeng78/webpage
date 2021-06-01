#Organizing the questions into a dictionary
def createDictionary(filename):
    openedFile = open(filename)
    readFile = openedFile.read()
    openedFile.close()

    lines = readFile.split('\n')