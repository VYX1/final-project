import random


def draw_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])


def calculate_score(hand):
    score = sum(hand)
    # Adjust score if there are aces
    num_aces = hand.count(11)
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score


def write_to_file(player_hand, decision, outcome):
    with open("blackjack_data.txt", "a") as file:
        file.write(f"Player's original sum: {sum(player_hand[:2])}, Decision: {decision}, Outcome: {outcome}\n")


def blackjack():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Write initial hand to file
    # write_to_file(player_hand, '', '')

    if player_score == 21:
        write_to_file(player_hand, '', "Player has Blackjack!")
        return

    while True:
        # decision = input("Do you want to hit or stand? (h/s): ").lower()
        if player_score <= 16:
            player_hand.append(draw_card())
            player_score = calculate_score(player_hand)
            if player_score > 21:
                write_to_file(player_hand, 'hit', "Player busts! Dealer wins.")
                return
        else:
            break

    # Dealer's turn
    while dealer_score < 17:
        dealer_hand.append(draw_card())
        dealer_score = calculate_score(dealer_hand)

    # Determine winner
    if dealer_score > 21:
        write_to_file(player_hand, 'stand', "Dealer busts! Player wins.")
    elif dealer_score == player_score:
        write_to_file(player_hand, 'stand', "It's a tie!")
    elif dealer_score > player_score:
        write_to_file(player_hand, 'stand', "Dealer wins.")
    else:
        write_to_file(player_hand, 'stand', "Player wins.")


num_games = int(input("How many games to simulate? "))
for _ in range(num_games):
    if __name__ == "__main__":
        blackjack()
