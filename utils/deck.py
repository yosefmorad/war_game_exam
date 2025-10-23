from random import randrange, uniform
def create_card(rank:str,suite:str) -> dict :

    if   rank <= "10" or rank >= "2":
        val = int(rank)
    elif rank == "J" or rank == "j":
        val = 11
    elif rank == "Q" or rank == "q":
        val = 12
    elif rank == "K" or rank == "k":
        val = 13
    elif rank == "A" or rank == "a":
        val = 14
    else:
        val = "value error"


    return {"rank": rank.upper() , "suite" : suite.upper() ,"value":val}



def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] <  p2_card["value"]:
        return f"{p1_card} ,{p2_card} , 'p2 win'"

    elif  p1_card["value"] >  p2_card["value"]:
        return f"{p1_card} ,{p2_card} , 'p1 win'"

    else:
        return f"{p1_card} ,{p2_card} , 'war'"


def create_deck() -> list[dict]:
    deck = []
    for num1 in range(2 ,15):
        deck.append(create_card(str(num1) ,"H"))

    for num2 in range(2 ,15):
        deck.append(create_card(str(num2) ,"C"))

    for num3 in range(2 ,15):
        deck.append(create_card(str(num3) ,"D"))

    for num4 in range(2 ,15):
        deck.append(create_card(str(num4) ,"S"))

    return deck



def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):

        index1 =  randrange(2, 52)
        index2 = randrange(2, 52)

        deck[index1] , deck[index2]= deck[index2]  ,deck[index1]

    return deck