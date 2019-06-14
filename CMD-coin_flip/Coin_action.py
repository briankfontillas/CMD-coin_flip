from random import randint

'''
Here are the classes/functions used for the basic heads or tails game
'''


############################################



######coin class
class Coin():

    def __init__(self,amount,coin_type):
        self.amount = amount
        self.coin_type = coin_type

    def flip(self):

        sides = ['Heads','Tails']

        chance = randint(1,2)

        if chance == 1:
            return sides[0]
        else:
            return sides[1]


######asking heads or tails
def action(guess):

    if guess[0].lower() == 'h':
        return 'Heads'
    elif guess[0].lower() == 't':
        return 'Tails'


###########play again function
def play_again(answer):

    if answer == 'Y':
        return True
    elif answer == 'N':
        return False

########################################
