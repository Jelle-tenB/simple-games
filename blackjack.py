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
pc_hand = []
player_hand = []
player = "Player"
computer = "Computer"


def deal_card(cards):
    random.shuffle(cards)
    card = cards[0]
    return card


def calculate_score(hand, turn):
    score = sum(hand)
    if score == 21:
        if len(hand) == 2:
            print("BLACKJACK")
            score = 0
            return score
        else:
            return score
    elif score > 21:
        try:
            position = hand.index(11)
            hand[position] = 1
            return calculate_score(hand, turn)
        except:
            print(f"{turn} has busted with {hand} for total of {score}\n")
            if turn == computer:
                print("You won!")
            else:
                pass
            start(new_game, turn)
            return score
    else:
        if turn == "Player":
            return score
        else:
            if score < 17:
                hand.append(deal_card(cards))
                return calculate_score(hand, turn)
            else:
                return score


def compare(player_hand2, pc_hand2, new_game2):
    new_game2 = True
    if sum(player_hand2) < sum(pc_hand2):
        print(f"The dealer has {pc_hand2} for a total of {calculate_score(pc_hand2, turn)}")
        print(f"You have {player_hand2} for a total of {calculate_score(player_hand2, turn)}")
        print("You lost...")
        return new_game2
    elif sum(player_hand2) > sum(pc_hand2):
        print(f"The dealer has {pc_hand2} for a total of {calculate_score(pc_hand2, turn)}")
        print(f"You have {player_hand2} for a total of {calculate_score(player_hand2, turn)}")
        print("Congratulations, you won!")
        return new_game2
    else:
        print(f"The dealer has {pc_hand2} for a total of {calculate_score(pc_hand2, turn)}")
        print(f"You have {player_hand2} for a total of {calculate_score(player_hand2, turn)}")
        print("It's a draw, bets have been pushed.")
        return new_game2


global new_game
new_game = True
turn = ""


def start(new_game, turn):
    while new_game == True:
        turn = player
        new = input("Would you like to start a new game? Y/N ").lower()
        if new == "y":
            global pc_hand
            global player_hand
            pc_hand.clear()
            player_hand.clear()
            pc_hand.append(deal_card(cards))
            pc_hand.append(deal_card(cards))
            player_hand.append(deal_card(cards))
            player_hand.append(deal_card(cards))
            turn = player
            print(f"{turn}'s hand is: {player_hand} For a total of {calculate_score(player_hand, turn)}")
            print(f"The dealer is showing an {pc_hand[0]}")
            if calculate_score(pc_hand, turn) == 0:
                print("The dealer has Blackjack. You lost...")
                start(new_game, turn)
            else:
                pass
            new_game = False
        else:
            start(new_game, turn)    
    hit = input("Would you like another card? Y/N ").lower()
    if hit == "y" and calculate_score(player_hand, turn) < 21:
        player_hand.append(deal_card(cards))
        print(f"{turn}'s hand is: {player_hand} For a total of {calculate_score(player_hand, turn)}")
        new_game = False
        start(new_game, turn)
    else:
        turn = "Computer"
        calculate_score(pc_hand, turn)
        compare(player_hand, pc_hand, new_game)
        new_game = True
        start(new_game, turn)


print(logo)
new_game = start(new_game, turn)