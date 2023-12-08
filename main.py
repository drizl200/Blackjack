from deck import *

if __name__ == "__main__":
    c1 = card('10', 'c')
    # print(c1.info())
    # print(c1.to_string())
    # print(c1.value())

    # double = deck(8)
    # print(double.info_deck)
    # print(double.get_deck_size())

    my_deck = deck(1)
    first_card = my_deck.deal_card()

    print(first_card.to_string())
    print(my_deck.string_deck)
    print(my_deck.get_deck_size())
    
