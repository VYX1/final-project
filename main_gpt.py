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


def write_to_file(data):
    with open("blackjack_data.txt", "a") as file:
        file.write(data + "\n")


def blackjack():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Write initial hand to file
    write_to_file(f"Player: {player_hand}, Dealer: [{dealer_hand[0]}, ?]")

    if player_score == 21:
        write_to_file("Player has Blackjack!")
        return

    while True:
        decision = input("Do you want to hit or stand? (h/s): ").lower()
        if decision == 'h':
            player_hand.append(draw_card())
            player_score = calculate_score(player_hand)
            write_to_file(f"Player hits: {player_hand}")
            if player_score > 21:
                write_to_file("Player busts! Dealer wins.")
                return
        elif decision == 's':
            break

    # Dealer's turn
    while dealer_score < 17:
        dealer_hand.append(draw_card())
        dealer_score = calculate_score(dealer_hand)
    write_to_file(f"Dealer's turn: {dealer_hand}")

    # Determine winner
    if dealer_score > 21:
        write_to_file("Dealer busts! Player wins.")
    elif dealer_score == player_score:
        write_to_file("It's a tie!")
    elif dealer_score > player_score:
        write_to_file("Dealer wins.")
    else:
        write_to_file("Player wins.")


if __name__ == "__main__":
    blackjack()
