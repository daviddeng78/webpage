#Organizing the questions into a dictionary
def createDictionary(filename):

    openedFile = open(filename, errors='ignore')
    readFile = openedFile.read()
    openedFile.close()

    qna = readFile.split('\n\n')

    categoryDictionary = {}

    for aqna in qna:
        unstrippedQuestion = aqna[:aqna.index('\n')]
        unstrippedAnswer = aqna[aqna.index('\n') + 1:]

        strippedQuestion = unstrippedQuestion[unstrippedQuestion.index(':') + 2:]
        strippedAnswer = unstrippedAnswer[unstrippedAnswer.index(':') + 2:]

        categoryDictionary[strippedQuestion] = strippedAnswer

    return categoryDictionary
    


    
