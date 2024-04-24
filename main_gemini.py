import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
values = {"Number": (2, 3, 4, 5, 6, 7, 8, 9, 10), "Face": 10, "Ace": 11}

# Data structure to store results
game_data = []


def create_deck():
    """Creates a deck of cards"""
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    return deck


def deal_card(deck):
    """Deals a card from the deck"""
    card = random.choice(deck)
    deck.remove(card)
    return card


def calculate_hand_value(hand):
    """Calculates the total value of a hand"""
    total = 0
    has_ace = False
    for card in hand:
        rank = card[1]
        if rank in values["Number"]:
            total += values["Number"][rank]
        elif rank in ("Jack", "Queen", "King"):
            total += values["Face"]
        else:  # Ace
            has_ace = True
            total += values["Ace"]

    # Adjust ace value if necessary
    if has_ace and total > 21:
        total -= 10
    return total


def play_game():
    """Simulates a single game of blackjack"""
    starting_hand = []
    for _ in range(2):
        starting_hand.append(deal_card(deck))

    # Record starting hand
    starting_value = calculate_hand_value(starting_hand)
    game_data.append({"hand": starting_hand, "win": None})

    # Player turn
    player_turn = True
    while player_turn:
        action = input("Hit (h) or Stand (s)? ")
        if action.lower() == "h":
            card = deal_card(deck)
            starting_hand.append(card)
            player_value = calculate_hand_value(starting_hand)
            if player_value > 21:
                # Player Busts
                player_turn = False
                game_data[-1]["win"] = False
                print("You BUSTED! Dealer Wins!")
        else:
            player_turn = False

    # Dealer turn
    dealer_hand = []
    for _ in range(2):
        dealer_hand.append(deal_card(deck))

    dealer_value = calculate_hand_value(dealer_hand)
    while dealer_value < 17:
        card = deal_card(deck)
        dealer_hand.append(card)
        dealer_value = calculate_hand_value(dealer_hand)

    # Determine winner
    if dealer_value > 21:
        # Dealer Busts
        game_data[-1]["win"] = True
        print("Dealer BUSTED! You Win!")
    elif dealer_value > player_value:
        game_data[-1]["win"] = False
        print("Dealer Wins!")
    elif dealer_value == player_value:
        game_data[-1]["win"] = "Push"
        print("Push! Nobody Wins!")
    else:
        game_data[-1]["win"] = True
        print("You Win!")


# Main loop
num_games = int(input("How many games to simulate? "))
for _ in range(num_games):
    deck = create_deck()
    random.shuffle(deck)
    play_game()

# Print data after all games
print("\nGame Data:")
for game in game_data:
    print(f"Starting Hand: {game['hand']}, Win: {game['win']}")