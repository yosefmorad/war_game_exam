from utils.deck import *

def create_player(name= "AI" ,hand=None ,won_pile=None) -> dict :
    if hand == None:
        hand =[]
    if won_pile == None:
        won_pile = []

    return {"name":name ,"hand": hand ,"won_pile":won_pile}


def init_game()->dict:


    deck= (create_deck())
    deck_shuffle = shuffle(deck)
    hand_p1 = deck_shuffle[0:26]
    hand_p2 = deck_shuffle[0:26]

    p1 = create_player(hand= hand_p1)
    p2 = create_player("hermon" ,hand= hand_p2)


    return {"deck":  deck_shuffle ,"player_1":p1 ,"player_2":p2}


def play_round(player_1,player_2):
    card_1 = init_game()[player_1].pop()
    card_2 = init_game()[player_2].pop()

    temp =  compare_cards(card_1 ,card_2)
    if "p_1 win " in temp:
        temp_2 = create_player(won_pile= temp)
    elif "p_2 win " in temp:
        temp_3 =create_player( "hermon",won_pile= temp)

    if len(player_1) > len(player_2):
        print("p_1 winn")
    elif len(player_1) < len(player_2):
        print("p_2 winn")



    pass