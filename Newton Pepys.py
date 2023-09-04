##############################################################################
##
## CS 101
## Program #2
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: Compute the probabilities of 6, 12, and 18 dice rolling a six during
##            a specific number of trials 
##
## ALGORITHM: 
##      1. Print intro to program and ask for user input
##            1.Print expository info
##            2.Retrieve user input
##      2. Validate that user input isn't less than 10
##            1.While user input is less than 10
##            2.Inform user that user input is too small
##            3.Ask for user input
##      3. Calculate dice rolls and populate percentage list with results
##            1.For every roll in trial,
##              2.For every i in 6, 12, and 18 rolls,
##                3.For every every j in i,
##                  4.If j is 6, add to dice list
##                  5.Add 1 to total list
##            2.Populate percent list by dividing dice by totals
##      4. Print percentages of trial rolls
##            1.After n trials
##            2.Print how many sixes were rolled in 6 trials, 12 trials, and 18 trials
##      5. Run percentages through if-tree and print correct dice likelihood
##            1.if a six was rolled most during 6 roll, print that this occurred the most
##            2.elif a six was rolled most during 12 rolls, print that this occurred the most
##            3.elif a six was rolled most during 18 rolls, print that this occurred the most
##            4.elif a six was rolled most during 6 and 12 rolls, print that these occurred the most
##            5.elif a six was rolled most during 6 and 18 rolls, print that these occurred the most
##            6.elif a six was rolled most during 12 and 18 rolls, print that these occurred the most
##            7.else print that all three rolls as equally likely
##      6. Ask for and then validate user input, then determine if loop program
##           or terminate program
##            1.Retrieve user input
##            2.While user input is not Y, YES, N, or NO
##              1.Inform user that user input is too small
##              2.Ask for user input
##            3.If user input is Y or YES, return to beginning
##            4.Else, terminate program
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
##############################################################################

import random

play_again = [('Y', 'YES'), ('N', 'NO')]
play = True
dice = [0,0,0,0]
totals = [0,0,0,0]

while play == True:
    #Print intro to program and ask for user input
    print('\nDie Odds')
    print('Samuel Pepys once asked Isaac Newton which is more likely')
    print('* At least 1 six occurs when 6 dice are rolled')
    print('* at least 2 sixes happen when 12 dice are rolled')
    print('* at least 3 sixes occur when 18 dice are rolled')
    print('Enter the number of trials to throw the dice')

    trials = int(input('\nHow many trials? ==> '))

    #Validate that user input isn't less than 10
    while not (trials >= 10):
        print('\nThe number of trials must be 10 or larger')
        trials = int(input('How many trials? ==> '))

    #Calculate dice rolls and populate percentage list with results
    for roll in range (trials):
        for i in range (6, 19, 6):
            for j in range(i):
                if random.randint(1,6) == 6:
                    dice[int(i/6)] += 1
                totals[int(i/6)] += 1

    percent = [round((dice[1] / totals[1]*100),1),
               round((dice[2] / totals[2]*100),1),
               round((dice[3] / totals[3]*100),1)
               ]
    #Print percentages of trial rolls
    print('After %d' % trials)
    print('At least one die was a six when 6 are rolled', percent[0], '%')
    print('At least two die was a six when 12 are rolled', percent[1], '%')
    print('At least three die was a six when 18 are rolled', percent[2], '%')
    print('')

    #Run percentages through if-tree and print correct dice likelihood
    if (percent[0] > percent[1] and percent[0] > percent[2]):
        print('At least one dice were a six when 6 are rolled occurred the most.')
    elif (percent[1] > percent[0] and percent[1] > percent[2]):
        print('At least two dice were a six when 12 are rolled and occurred the most.')
    elif (percent[2] > percent[0] and percent[2] > percent[1]):
        print('At least three dice were a six when 18 are rolled occurred the most.')
    elif (percent[0] == percent[1] and percent[0] > percent[2] and percent[1] > percent[2]):
        print('At least one dice were a six when 6 are rolled and\n',
              'At least two dice were a six when 12 are rolled and occurred the most.\n',
              'Try again with more trials')
    elif (percent[0] == percent[2] and percent[0] > percent[1] and percent[2] > percent[1]):
        print('At least one dice were a six when 6 are rolled and\n',
              'At least three dice were a six when 18 are rolled and occurred the most.\n',
              'Try again with more trials')
    elif (percent[1] == percent[2] and percent[1] > percent[0] and percent[2] > percent[0]):
        print('At least two dice were a six when 12 are rolled and\n',
              'At least three dice were a six when 18 are rolled and occurred the most.\n',
              'Try again with more trials')
    else:
        print('In this run they are all 3 likely. Try it with more trials')
    
    #Ask for and then validate user input, then determine if loop program or terminate program
    play = input('\nDo you want to play again? Y/YES/N/NO ==> ').upper()
    while not (play in play_again[0] or play in play_again[1]):
        print('You must enter Y YES N or NO')
        play = input('\nDo you want to play again? Y/YES/N/NO ==> ').upper()
    if play in play_again[0]:
        play = True
    else:
        play = False
