import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card():
    """ Get a random card"""
    return random.choice(cards)


def check_card(card):
    """ check who has the blackjack and replace 11 by 1 if the sum of card greater than 21"""
    if 11 in card and len(card) <= 2 and sum(card)<=21:
        return 0
    
    if 11 in card and sum(card) >= 21:
        card.remove(11)
        card.append(1)
        
        
def score_card(card) :
    """calculate the sum of the card"""
    return sum(card) 

def compare(user,computer):
    """compare scores to print the winner or the loser"""
    
    if check_card(computer) == 0:
        print("\tYou Lose,Opponent has a Blackjack!")
    elif check_card(user) == 0:
        print("\tYou Win with a Blackjack!")
    elif score_card(user)>21:
        print("\tYou went over 21, You lOSE!")
    elif score_card(computer)>21:
        print("\tOpponent went over, You WIN!")
    elif score_card(user)==score_card(computer):
        print("\tDRAW")
    elif score_card(user)>score_card(computer):
        print("\tYou Win!")
    else:
        print("\tYou LOSE!")


def blackjack_game():

    user_card = []
    computer_card = []

    start = input("Do want to Play Blackjack game, Type 'y' or 'n' \n").lower()
    if start == 'y':
        print(logo)
        for card in range(2):
            user_card.append(deal_card())
            computer_card.append(deal_card())
    else:
        return 0

    game_over = False

    while not game_over:

        print(f"Your card is{user_card}, current score: {score_card(user_card)}")
        print(f"Computer's first card: {computer_card[0]}")

        if score_card(user_card)>21 or check_card(user_card)==0 or check_card(computer_card)==0:
            game_over=True
        else:


            keep_playing = input("Type 'y' to get another card or 'n' to pass:\n").lower()
            if keep_playing=='y':
                user_card.append(deal_card())
            else:
                game_over = True
        
    while score_card(computer_card)<17 and check_card(computer_card)!=0:
        computer_card.append(deal_card())

    print(f"Your final hand: {user_card}, final score: {score_card(user_card)}")
    print(f"Computer's final hand: {computer_card}, Final score: {score_card(computer_card)}")
    compare(user_card, computer_card)
        


            
    

    blackjack_game()
    


blackjack_game()







