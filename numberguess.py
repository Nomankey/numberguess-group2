import random


answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))

chance = 5 

while chance > 0:
    guess = int(input('Guess the number(1-100): '))
    print(guess, type(guess))

   if guess-answer==0:
        print('Correct!')
   elif guess>answer:
        print('Down!')
    elif guess<answer:
        print('Up!')


    

