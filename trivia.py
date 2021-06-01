#Organizing the Questions
def organization(filename):
    openedFile = open(filename)
    readFile = openedFile.read()
    openedFile.close()

    return readFile