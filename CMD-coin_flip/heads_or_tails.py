from Coin_action import *

#Heads or tails main script


print('Welcome to Heads or Tails!')

cycle = True
score = []
correct = 0
incorrect = 0
my_coin = Coin(25,'Quarter')

while cycle == True:

#####asking heads or tails
    while True:

        question = input('Heads or Tails?: ')

        if question[0].lower() == 'h' or question[0].lower() == 't':
            guess = action(question)
            break
        else:
            print('Please choose a valid answer (Heads/Tails)')
            continue



######flip and answer
    outcome = my_coin.flip()
    print(f'\n{outcome}')
    score.append(outcome)

    if guess == outcome:
        correct += 1
    else:
        incorrect += 1


#######ask for another round
    while True:
        round = input('Would you like to play again? (Y/N): ').upper()

        if round[0] == 'Y' or round[0] == 'N':
            if play_again(round) == True:
                break
            elif play_again(round) == False:
                total_heads = score.count('Heads')
                total_tails = score.count('Tails')
                print(f'Guesses right: {correct} Guesses wrong: {incorrect}')
                print(f'Heads: {total_heads} Tails: {total_tails}')
                quit()

            else:
                print('Input not valid, Try again: ')
                continue
