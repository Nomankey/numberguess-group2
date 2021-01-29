import random

user_id = str(input("What is Your Name? "))
answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))

guess = int(input('Guess the number(1-100): '))
print(guess, type(guess))

if guess-answer==0:
    print('Correct, {}!'.format(user_id))
else:
    print('Wrong, {}! The answer was {}.'.format(user_id, answer))

