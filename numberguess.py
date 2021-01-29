import random


answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))

username = input('What is your name? ')
guess = int(input('Guess the number(1-100): '))
print(guess, type(guess))

if guess-answer==0:
    print('Correct, {}!'.format(username))
elif guess>answer:
    print('Down, {}!'.format(username))
elif guess<answer:
    print('Up, {}!'.format(username))

