import random


answer = random.randint(1,100)
print('DEBUG: {}'.format(answer))

chance = 5      # 임의로 정한 수입니다  

while chance > 0:
    guess = int(input('Guess the number(1-100): '))
    print(guess))

    if guess-answer==0:
        print('Correct!')
    elif guess<answer:
        print('Up!')
    elif guess>answer:
    chance -= 1
        print('Down!')
    

    if chance == 0:
        print('Wrong! The answer was {}'.format(answer))
         


    

