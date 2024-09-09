# Guessing Game 

'''
1. Need to generate a random number (i.e) jackpot number
2. get a input from user
3. compare the input from user and jackpot number if wrong give a multiple attempt
4. if correct show the number'''


import random
jackpot_number = random.randint(0,100)
# print(jackpot_number)
print('''Welcome to Guessing Game......
Enter 1 to 100 random number and guess the number to get a jackpot''')

guessing_number = int(input('Enter your guessing number: '))
counter = 1
while guessing_number != jackpot_number:
    if guessing_number < jackpot_number:
        print('Wrong.... Guess the higher number')
    else: 
        print('Wrong.... Guess the lower number')
    
    guessing_number = int(input('Enter your guessing number: '))
    counter += 1 
else: 
    print('Congratulation...! Correct Guessing...!')
    print('You have attempted', counter, 'times')
