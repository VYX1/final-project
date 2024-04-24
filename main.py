import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = []
threshold = 14


def make_deck():
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    player()


def card_deal():
    card = random.choice(deck)
    deck.remove(card)
    value = values[ranks.index(card[1])]
    return card, value


dealer_hand = [0]
player_hand = [0]


def dealer():
    while sum(dealer_hand) <= 16:
        dealer_hand.append(card_deal()[1])
        print("dealer hits")


def player():
    card_1 = card_deal()
    card_2 = card_deal()
    player_hand.append(card_1[1])
    player_hand.append(card_2[1])
    print(f"you drew: {card_1[0]}, {card_2[0]}")
    while sum(player_hand) <= threshold:
        player_hit()
    is_game_over()


def player_hit():
    card_x = card_deal()
    player_hand.append(card_x[1])
    print(f"you drew: {card_x[0]}")


def is_game_over():
    dealer()
    if sum(player_hand) > 21:
        print(f"Player Bust, deck value: {sum(player_hand)}, threshold: {threshold}")
    elif sum(player_hand) == sum(dealer_hand):
        print(f"Tie, deck value: {sum(player_hand)}, threshold: {threshold}")
    elif sum(dealer_hand) > 21:
        print(f"Dealer Bust, deck value: {sum(player_hand)}, threshold: {threshold}")


make_deck()
