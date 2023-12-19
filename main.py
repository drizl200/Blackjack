from deck import *
from blackjack import *

#def card_test():
    #c1 = card('10', 'c')
    # print(c1.info())
    # print(c1.to_string())
    # print(c1.value())

    # double = deck(8)
    # print(double.info_deck)
    # print(double.get_deck_size())

def deck_test():
    my_deck = deck(1)
    first_card = my_deck.deal_card()

    print(first_card.to_string())
    print(my_deck.string_deck)
    print(my_deck.get_deck_size())

def hand_test():
    my_deck = deck(2)
    my_hand = hand(my_deck)

    print(my_hand.string_hand)
    print(my_deck.get_deck_size())
    print(my_hand.hand_value)

def main():
    hand_test() 

if __name__ == "__main__":
    main()
    
