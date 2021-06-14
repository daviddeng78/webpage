import random
import matplotlib.pyplot as plt

#Organizing the questions into a dictionary
def createDictionary(filename):

    openedFile = open(filename, errors='ignore', encoding="utf-8")
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

MathInteger = createDictionary('Math(Integer).txt')
MusicSong = createDictionary('Music(Song).txt')
MusicPlace = createDictionary('Music(Place).txt')
MusicGroup = createDictionary('Music(Group).txt')
MusicAlbum = createDictionary('Music(Album).txt')
MusicPeople = createDictionary('Music(People).txt')
SciencePeople = createDictionary('Science(People).txt')
ScienceAnimal = createDictionary('Science(Animal).txt')
ScienceTerm = createDictionary('Science(Term).txt')
ScienceElement = createDictionary('Science(Element).txt')
ScienceSpace = createDictionary('Science(Space).txt')
ScienceProcess = createDictionary('Science(Process).txt')
ScienceBody = createDictionary('Science(Body).txt')
GeographyPlace = createDictionary('Geography(Place).txt')
MovieMovie = createDictionary('Movie(Movie).txt')
MoviePeople = createDictionary('Movie(People).txt')
HistoryDate = createDictionary('History(Date).txt')
HistoryEvent = createDictionary('History(Event).txt')
HistoryLocation = createDictionary('History(Location).txt')
HistoryPeople = createDictionary('History(People).txt')

MasterDictionary = {}
MasterDictionary['Science'] = [SciencePeople, ScienceAnimal, ScienceTerm, ScienceElement, ScienceSpace, ScienceProcess, ScienceBody]
MasterDictionary['History'] = [HistoryDate, HistoryEvent, HistoryLocation, HistoryPeople]
MasterDictionary['Music'] = [MusicSong, MusicPlace, MusicGroup, MusicAlbum, MusicPeople]
MasterDictionary['Math'] = [MathInteger]
MasterDictionary['Geography'] = [GeographyPlace]
MasterDictionary['Movie'] = [MovieMovie, MoviePeople]

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
def failsafe2():
    category =  input('Type 1, 2, 3, 4, 5, or 6 to select the category of the question:')
    if category == '1' or category == '2' or category == '3' or category == '4' or category == '5'or category == '6':
        return category
    else:
        print('Sorry, that was not an option, please enter 1, 2, 3, 4, 5, 6.')
        
def AlexTrebek(possible_questions, possible_answers):
    QuestionNumber = random.randint(0,len(possible_questions) -  1)
    AnswerNumber = random.randint(1, 4)
    seperate = ('=' * 100)
    dict_wrong = {}
    possible_wrong = []
    fail = False
    for i in possible_answers:
        if i != possible_answers[QuestionNumber]:
            possible_wrong.append(i)
    for i in possible_wrong:
        dict_wrong[i] = 1
    possible_wrong = list(dict_wrong.keys())
    print(seperate)
    print(possible_questions[QuestionNumber])
    choices_wrong = random.sample(possible_wrong, 3)
    if AnswerNumber == 1:
        print('1.', possible_answers[QuestionNumber])
        print('2.', choices_wrong[0])
        print('3.', choices_wrong[1])
        print('4.', choices_wrong[2])
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
        print('1.', choices_wrong[0])
        print('2.', possible_answers[QuestionNumber])
        print('3.', choices_wrong[1])
        print('4.', choices_wrong[2])
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
        print('1.', choices_wrong[0])
        print('2.', choices_wrong[1])
        print('3.', possible_answers[QuestionNumber])
        print('4.', choices_wrong[2])
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
        print('1.', choices_wrong[0])
        print('2.', choices_wrong[1])
        print('3.', choices_wrong[2])
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
    MasterDictionary['Science'] = [SciencePeople, ScienceAnimal, ScienceTerm, ScienceElement, ScienceSpace, ScienceProcess, ScienceBody]
    MasterDictionary['History'] = [HistoryDate, HistoryEvent, HistoryLocation, HistoryPeople]
    MasterDictionary['Music'] = [MusicSong, MusicPlace, MusicGroup, MusicAlbum, MusicPeople]
    MasterDictionary['Math'] = [MathInteger]
    MasterDictionary['Geography'] = [GeographyPlace]
    MasterDictionary['Movie'] = [MovieMovie, MoviePeople]
    turn = 0
    score = 0
    history_score = 0
    science_score = 0
    math_score = 0
    geography_score = 0
    music_score = 0
    movie_score = 0
    state = True
    fail1 = True
    fail2 = True
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
            g = random.randint(0, 6)
            if g == 0:
                print('You spun the Crown')
                print('''Choose a category:
1. History
2. Science
3. Math
4. Geography
5. Music
6. Movie''')
                g = failsafe2()
                if g == '1' or g == '2' or g == '3' or g == '4'or g == '5'or g == '6':
                    fail2 = False
                else:
                    fail2 = True
                while fail2 == True:
                    g = failsafe2()
                    if g == '1' or g == '2' or g == '3' or g == '4'or g == '5'or g == '6':
                        fail2 = False
            if g == 1 or g == '1':
                print('You spun History')
                continue1 = input('Type anything to continue:')
                subset = random.randint(0, len(MasterDictionary['History']) - 1)
                possible_questions = list((MasterDictionary['History'])[subset].keys()) 
                possible_answers = list((MasterDictionary['History'])[subset].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    history_score += 1
                    score += 100
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                    
            if g == 2 or g == '2':
                print('You spun Science')
                continue1 = input('Type anything to continue:')
                subset = random.randint(0, len(MasterDictionary['Science']) - 1)
                possible_questions = list((MasterDictionary['Science'])[subset].keys()) 
                possible_answers = list((MasterDictionary['Science'])[subset].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    science_score += 1
                    score += 100
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
            if g == 3 or g == '3':
                print('You spun Math')
                continue1 = input('Type anything to continue:')
                subset = random.randint(0, len(MasterDictionary['Math']) - 1)
                possible_questions = list((MasterDictionary['Math'])[subset].keys()) 
                possible_answers = list((MasterDictionary['Math'])[subset].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    math_score += 1
                    score += 100
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
            if g == 4 or g == '4':
                print('You spun Geography')
                continue1 = input('Type anything to continue:')
                subset = random.randint(0, len(MasterDictionary['Geography']) - 1)
                possible_questions = list((MasterDictionary['Geography'])[subset].keys()) 
                possible_answers = list((MasterDictionary['Geography'])[subset].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    science_score += 1
                    score += 100
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
            if g == 5 or g == '5':
                print('You spun Music')
                continue1 = input('Type anything to continue:')
                subset = random.randint(0, len(MasterDictionary['Music']) - 1)
                possible_questions = list((MasterDictionary['Music'])[subset].keys()) 
                possible_answers = list((MasterDictionary['Music'])[subset].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    music_score += 1
                    score += 100
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
            if g == 6 or g == '6':
                print('You spun Movie')
                continue1 = input('Type anything to continue:')
                subset = random.randint(0, len(MasterDictionary['Movie']) - 1)
                possible_questions = list((MasterDictionary['Movie'])[subset].keys()) 
                possible_answers = list((MasterDictionary['Movie'])[subset].values())
                Answer = AlexTrebek(possible_questions, possible_answers)
                if Answer == 1:
                    print('Correct!')
                    movie_score += 1
                    score += 100
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
                else:
                    print('Incorrect, the answer is', Answer)
                    print('score:' + str(score))
                    turn += 1
                    print('round:' + str(turn))
        else:
            state = False
            plt.bar(['History', 'Science', 'Math', 'Geography', 'Music', 'Movie'], [history_score, science_score, math_score, geography_score, music_score, movie_score])
            plt.title('How did you do?')
            plt.xlabel('Category')
            plt.ylabel('Number of Questions Correct')
            plt.show()




    
