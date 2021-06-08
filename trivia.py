import random
import matplotlib.pyplot as plt

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
    if turn == 0:
        print('''
Welcome to the Python-based Trivia Game!
In this game you will be given a random category and a question from that category.
Let's begin! :) ''')
    while state == True:
        print('Would you like to spin?')
        Go = input('Type Y or N:')
        if Go == 'Y':
            g = random.randint(1, 5)
            if g == 1:
                print('You spun History')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['History'].keys()) 
                possible_answers = list(MasterDictionary['History'].values())
                QuestionNumber = random.randint(0,len(possible_questions) + 1)
                AnswerNumber = random.randint(1, 5)
                print('====================')
                print(possible_questions[QuestionNumber])
                if AnswerNumber == 1:
                    print('1.', possible_answers[QuestionNumber])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '1':
                        print('Correct!')
                        history_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 1' )
                        print('score:' + str(score))
                if AnswerNumber == 2:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[QuestionNumber])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '2':
                        print('Correct!')
                        history_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 2' )
                        print('score:' + str(score))
                if AnswerNumber == 3:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[QuestionNumber])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '3':
                        print('Correct!')
                        history_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 3' )
                        print('score:' + str(score))
                if AnswerNumber == 4:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[QuestionNumber])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '4':
                        print('Correct!')
                        history_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 4' )
                        print('score:' + str(score))
            elif g == 2:
                print('You spun Science')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['Science'].keys()) 
                possible_answers = list(MasterDictionary['Science'].values())
                QuestionNumber = random.randint(0,len(possible_questions) + 1)
                AnswerNumber = random.randint(1, 5)
                print('====================')
                print(possible_questions[QuestionNumber])
                if AnswerNumber == 1:
                    print('1.', possible_answers[QuestionNumber])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '1':
                        print('Correct!')
                        science_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 1' )
                        print('score:' + str(score))
                if AnswerNumber == 2:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[QuestionNumber])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '2':
                        print('Correct!')
                        science_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 2' )
                        print('score:' + str(score))
                if AnswerNumber == 3:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[QuestionNumber])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '3':
                        print('Correct!')
                        science_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 3' )
                        print('score:' + str(score))
                if AnswerNumber == 4:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[QuestionNumber])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '4':
                        print('Correct!')
                        science_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 4' )
                        print('score:' + str(score))
            elif g == 3:
                print('You spun Math')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['Math'].keys()) 
                possible_answers = list(MasterDictionary['Math'].values())
                QuestionNumber = random.randint(0,len(possible_questions) + 1)
                AnswerNumber = random.randint(1, 5)
                print('====================')
                print(possible_questions[QuestionNumber])
                if AnswerNumber == 1:
                    print('1.', possible_answers[QuestionNumber])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '1':
                        print('Correct!')
                        math_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 1' )
                        print('score:' + str(score))
                if AnswerNumber == 2:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[QuestionNumber])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '2':
                        print('Correct!')
                        math_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 2' )
                        print('score:' + str(score))
                if AnswerNumber == 3:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[QuestionNumber])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '3':
                        print('Correct!')
                        math_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 3' )
                        print('score:' + str(score))
                if AnswerNumber == 4:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[QuestionNumber])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '4':
                        print('Correct!')
                        math_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 4' )
                        print('score:' + str(score))
            else:
                print('You spun Sport')
                continue1 = input('Type anything to continue:')
                possible_questions = list(MasterDictionary['Sport'].keys()) 
                possible_answers = list(MasterDictionary['Sport'].values())
                QuestionNumber = random.randint(0,len(possible_questions) + 1)
                AnswerNumber = random.randint(1, 5)
                print('====================')
                print(possible_questions[QuestionNumber])
                if AnswerNumber == 1:
                    print('1.', possible_answers[QuestionNumber])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '1':
                        print('Correct!')
                        sport_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 1' )
                        print('score:' + str(score))
                if AnswerNumber == 2:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[QuestionNumber])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '2':
                        print('Correct!')
                        sport_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 2' )
                        print('score:' + str(score))
                if AnswerNumber == 3:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[QuestionNumber])
                    print('4.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '3':
                        print('Correct!')
                        sport_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 3' )
                        print('score:' + str(score))
                if AnswerNumber == 4:
                    print('1.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('2.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('3.', possible_answers[random.randint(0,len(possible_questions) + 1)])
                    print('4.', possible_answers[QuestionNumber])
                    print('====================')
                    guess = input('Type 1, 2, 3, or 4:')
                    if guess == '4':
                        print('Correct!')
                        sport_score += 1
                        score += 100
                        print('score:' + str(score))
                    else:
                        print('Incorrect, the answer is 4' )
                        print('score:' + str(score))
        else:
            state = False
            plt.bar(['History', 'Science', 'Math', 'Sport'], [history_score, science_score, math_score, sport_score])
            plt.title('How did you do?')
            plt.xlabel('Number of Questions Correct')
            plt.ylabel('Category')
            plt.show()


    
