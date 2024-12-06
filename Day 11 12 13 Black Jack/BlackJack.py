import random
import game_data
import art

print(art.logo)

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# A function to draw a random card from the deck.
def deal_card():
    deal = random.choice(card_deck)
    return deal

def calculate_score(cards):                         # calculates the sum total of their cards.
    if sum(cards) == 21 and len(cards) ==2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    user_result = -1  # assigns -1 to skip the no value error for user_result
    computer_result = -1
    is_game_over = False

    for _ in range(2):                              # a loop to draw two cards for both user and computer
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_result = calculate_score(user_cards)
        computer_result = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and your score: {user_result}")
        print(f"Computer's first card: {computer_cards[0]} ")

        if user_result == 0 or computer_result == 0 or user_result > 21:
            is_game_over = True
        else:
            deal_another = input("Type 'y' to draw another card, type 'n' to pass.\n" ).lower()
            if deal_another == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_result != 0 and computer_result < 17:
        computer_cards.append(deal_card())
        computer_result = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_result}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_result}")
    print(compare(user_score = user_result, computer_score = computer_result))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == "y":
    play_game()
    print("\n" * 20)
