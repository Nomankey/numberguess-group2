import random


answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))


chance = 5                  # the number of chance is randomly chosen 

while chance > 0:
    guess = int(input('Guess the number(1-100): '))
    print(guess, type(guess))

    if guess-answer==0:
        print('Correct!')
        break
    else:
        print('Wrong! The answer was {}.'.format(answer))

    if chance == 0:        # Add a sentence to be printed when the chance is all used up
        print('Unfortunately, you've used up all the chances... Next time!')
