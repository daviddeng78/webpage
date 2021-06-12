import random
import matplotlib.pyplot as plt
#work on a fail safe to repeat the question if not valid answer is given
#seperate list
#set the reading to utf-8

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

Science = createDictionary("ScienceQuestions.txt")
History = createDictionary("HistoryQuestions.txt")
Sport = createDictionary("SportQuestions.txt")
Math = createDictionary("MathQuestions.txt")

MasterDictionary = {}
MasterDictionary['Science'] = Science
MasterDictionary['History'] = History
MasterDictionary['Sport'] = Sport
MasterDictionary['Math'] = Math

def failsafe():
    guess =  input('Type 1, 2, 3, or 4:')
    if guess == '1' or guess == '2' or guess == '3' or guess == '4':
        return guess
    else:
        print('Sorry, that was not an option, please enter 1, 2, 3, or 4.')
def failsafe1():
    question =  input('Type Y or N:')
    if question == 'N' or question == 'Y':
        return question
    else:
        print('Sorry, that was not an option, please enter Y or N.')
        
def AlexTrebek(possible_questions, possible_answers):
    QuestionNumber = random.randint(0,len(possible_questions) -  1)
    AnswerNumber = random.randint(1, 5)
    seperate = ('=' * 100)
    fail = False
    print(seperate)
    print(possible_questions[QuestionNumber])
    if AnswerNumber == 1:
        print('1.', possible_answers[QuestionNumber])
        print('2.', possible_answers[random.randint(0,len(possible_questions) - 1)])
        print('3.', possible_answers[random.randint(0,len(possible_questions) - 1)])
        print('4.', possible_answers[random.randint(0,len(possible_questions) - 1)])
        print(seperate)
        g = failsafe()
        if g == '1' or g == '2' or g == '3' or g == '4':
            fail = False
        else:
            fail = True
        while fail == True:
            g = failsafe()
            if g == '1' or g == '2' or g == '3' or g == '4':
                fail = False
        if g == '1':
            return 1
        else:
            return possible_answers[QuestionNumber]
    if AnswerNumber == 2:
        print('1.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('2.', possible_answers[QuestionNumber])
        print('3.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('4.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print(seperate)
        g = failsafe()
        if g == '1' or g == '2' or g == '3' or g == '4':
            fail = False
        else:
            fail = True
        while fail == True:
            g = failsafe()
            if g == '1' or g == '2' or g == '3' or g == '4':
                fail = False
        if g == '2':
            return 1
        else:
            return possible_answers[QuestionNumber]
    if AnswerNumber == 3:
        print('1.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('2.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('3.', possible_answers[QuestionNumber])
        print('4.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print(seperate)
        g = failsafe()
        if g == '1' or g == '2' or g == '3' or g == '4':
            fail = False
        else:
            fail = True
        while fail == True:
            g = failsafe()
            if g == '1' or g == '2' or g == '3' or g == '4':
                fail = False
        if g == '3':
            return 1
        else:
            return possible_answers[QuestionNumber]
    if AnswerNumber == 4:
        print('1.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('2.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('3.', possible_answers[random.randint(0,len(possible_questions) -  1)])
        print('4.', possible_answers[QuestionNumber])
        print(seperate)
        g = failsafe()
        if g == '1' or g == '2' or g == '3' or g == '4':
            fail = False
        else:
            fail = True
        while fail == True:
            g = failsafe()
            if g == '1' or g == '2' or g == '3' or g == '4':
                fail = False
        if g == '4':
            return 1
        else:
            return possible_answers[QuestionNumber]

print('To start the game type Trivia() in the shell')


def Trivia():
    MasterDictionary = {}
    MasterDictionary['Science'] = Science
    MasterDictionary['History'] = History
    MasterDictionary['Sport'] = Sport
    MasterDictionary['Math'] = Math
    turn = 0
    score = 0
    history_score = 0
    science_score = 0
    math_score = 0
    sport_score = 0
    state = True
    fail1 = True
    if turn == 0:
        print('''
Welcome to the Python-based Trivia Game!
In this game you will be given a random category and a question from that category.
Let's begin! :) ''')
    while state == True:
        print('Would you like to spin?')
        Go = failsafe1()
        if Go == 'N' or Go == 'Y':
            fail1 = False
        else:
            fail1 = True
        while fail1 == True:
            Go = failsafe1()
            if Go == 'N' or Go == 'Y':
                fail1 = False
        if Go == 'Y':
            g = random.randint(1, 4)
            if g == 1:
                print('You spun History')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['History'].keys()) 
                possible_answers = list(MasterDictionary['History'].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    history_score += 1
                    score += 100
                    print('score:' + str(score))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
            elif g == 2:
                print('You spun Science')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['Science'].keys()) 
                possible_answers = list(MasterDictionary['Science'].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    science_score += 1
                    score += 100
                    print('score:' + str(score))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
            elif g == 3:
                print('You spun Math')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['Math'].keys()) 
                possible_answers = list(MasterDictionary['Math'].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    math_score += 1
                    score += 100
                    print('score:' + str(score))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
            else:
                print('You spun Sport')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['Sport'].keys()) 
                possible_answers = list(MasterDictionary['Sport'].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    sport_score += 1
                    score += 100
                    print('score:' + str(score))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
        else:
            state = False
            plt.bar(['History', 'Science', 'Math', 'Sport'], [history_score, science_score, math_score, sport_score])
            plt.title('How did you do?')
            plt.xlabel('Number of Questions Correct')
            plt.ylabel('Category')
            plt.show()



    
