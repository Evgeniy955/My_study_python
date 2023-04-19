table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]


def flush_card():
    card_suit = [i[-1] for i in table_cards]
    card_suit_hand = [i[-1] for i in hand_cards]

    cards = card_suit + card_suit_hand

    flush = any([cards.count(i) >= 5 for i in 'SHDC'])

    if flush:
        print("Flush")
    else:
        print("No Flush!")


flush_card()
