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
    print(my_hand.get_hand_value())

def hand_test_two():
    my_deck = deck(2)
    player_1 = player(10000, 10)
    player_1.player_deal(0, my_deck)
    player_1.player_deal(0, my_deck)
    print(player_1.get_player_hand_string(0))
    player_1.split_hand(0,my_deck)

    
    print(player_1.player_hands[0].string_hand)
    print(player_1.player_hands[1].string_hand)
    print(my_deck.get_deck_size())

def main():
    hand_test_two() 

if __name__ == "__main__":
    main()
    
