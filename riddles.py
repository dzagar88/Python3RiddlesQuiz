# Daniel Zagar
# Python 3.9.5
# Riddles Quiz

'''
Each question is a While Loop looking for a match on the answer or the question to be answered wrong 3 times to move on.
Answers aren't case sensitive but must match exact spelling.
User has 3 chances to get each question right before they are moved onto the next question.  Retries are counted and displayed at the end of the game.
The score is tracked and displayed at the end of the game as well.
'''

print('Welcome to the Riddles Quiz!  Have fun answering these 5 super awesome riddles!')
print('You have 3 chances to answer each riddle before you are moved on to the next one!')

player = input('Please enter your name: ')
score = 0
retry = 0
wrong = 0

print('_____')
# Riddle 1: What has to be broken before you can use it?
count1 = 0

print(player + ', ' +'solve this riddle: What has to be broken before you can use it? (Answer in two words. Ex: "an _____")')

answer1 = 'an egg'
gameover1 = False

while gameover1 == False:
    guess1 = input('Enter your answer here: ').lower()
    count1 += 1
    if guess1 == answer1:
        print('Correct!')
        score += 20
        gameover1 = True
        break
    elif count1 == 3:
        print('Better luck next time!')
        wrong += 1
        gameover1 == True
        break
    else:
        print('Try again!')
        retry += 1
print('_____')

# Riddle 2: I’m tall when I’m young, and I’m short when I’m old. What am I?
count2 = 0

print(player + ', ' + 'try this riddle: I’m tall when I’m young, and I’m short when I’m old. What am I? (Answer in two words. Ex: "a _____")')

answer2 = 'a candle'
gameover2 = False

while gameover2 == False:
    guess2 = input('Enter your answer here: ').lower()
    count2 += 1
    if guess2 == answer2:
        print('Correct!')
        score += 20
        gameover2 = True
        break
    elif count2 == 3:
        print('Better luck next time!')
        wrong += 1
        gameover2 == True
        break
    else:
        print('Try again!')
        retry += 1
print('_____')

# Riddle 3: What month of the year has 28 days?
count3 = 0

print('OK, Smarty Pants, solve this riddle: How many months have 28 days? (Give a number answer)')

answer3 = '12'
gameover3 = False

while gameover3 == False:
    guess3 = input('Enter your answer here: ').lower()
    count3 += 1
    if guess3 == answer3:
        print('Correct!')
        score += 20
        gameover3 = True
        break
    elif count3 == 3:
        print('Better luck next time!')
        wrong += 1
        gameover3 == True
        break
    else:
        print('Try again!')
        retry += 1
print('_____')    

# Riddle 4 : What is full of holes but still holds water?
count4 = 0

print('Here' + "'" + 's a harder one, solve this riddle: What is full of holes but still holds water? (Answer in two words. Example: "a _____")')

answer4 = 'a sponge'
gameover4 = False

while gameover4 == False:
    guess4 = input('Enter your answer here: ').lower()
    count4 += 1
    if guess4 == answer4:
        print('Correct!')
        score += 20
        gameover4 = True
        break
    elif count4 == 3:
        print('Better luck next time!')
        wrong += 1
        gameover4 == True
        break
    else:
        print('Try again!')
        retry += 1      
print('_____')

# Riddle 5 : Where does today come before yesterday?
count5 = 0

print('OK, Smarty Pants, solve this riddle: Where does today come before yesterday? (Answer in two words. Example: "the _____")')

answer5 = 'the dictionary'
gameover5 = False

while gameover5 == False:
    guess5 = input('Enter your answer here: ').lower()
    count5 += 1
    if guess5 == answer5:
        print('Correct!')
        score += 20
        gameover5 = True
        break
    elif count5 == 3:
        print('Better luck next time!')
        wrong += 1
        gameover5 == True
        break
    else:
        print('Try again!')
        retry += 1      

print('_____')
print('_____')
print('Game Over! Here are your stats:')
print('Name: ' + player)
print('Score: ' + str(score) + '%')
print(str('Wrong:'), wrong)
print(str('Retries:'), retry)
print('Thanks for playing, ' + player + '!')
print('_____')
print('_____')