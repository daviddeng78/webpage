#Organizing the questions into a dictionary
def createDictionary(filename):
    openedFile = open(filename, errors='ignore')
    readFile = openedFile.read()
    openedFile.close()

    strippedFile = readFile.strip()