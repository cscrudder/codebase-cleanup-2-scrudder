

from random import choice

# I used the dictionary structure provided by Prof Rossetti
def determine_winner(user_choice, computer_choice):
    """
    This fucntion decides the winner of a rock, paper, scissors game
    Both the user and the computer must use either 'rock', 'paper', or 'scissors'
    The function assumes inputs are valid and does not validate them.
    Inputs are (user's choice, computer's choice), although the order does not matter.
    """
    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice


## THIS IS THE GAMEPLAY CODE
if __name__ == "__main__":
    
    # Acceptable choices in RPS
    valid_choices = ["rock", "paper", "scissors"]

    # USER SELECTION
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)

    # User selection validation
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

    # COMPUTER SELECTION
    c = choice(valid_choices)
    print("COMPUTER CHOICE:", c)

    # References function above to determine winner
    winning_choice = determine_winner(u,c)

    # Prints game result
    if winning_choice == u:
        print("YOU WON")
    elif winning_choice == c:
        print("COMPUTER WON")
    else:
        print("TIE")


## ** THIS CODE WAS DEEMED TOO COMPLEX ** ##
# # if u == "rock" and c == "rock":
#     print("It's a tie!")
# elif u == "rock" and c == "paper":
#     print("The computer wins")
# elif u == "rock" and c == "scissors":
#     print("The user wins")

# elif u == "paper" and c == "rock":
#     print("The computer wins")
# elif u == "paper" and c == "paper":
#     print("It's a tie!")
# elif u == "paper" and c == "scissors":
#     print("The user wins")

# elif u == "scissors" and c == "rock":
#     print("The computer wins")
# elif u == "scissors" and c == "paper":
#     print("The user wins")
# elif u == "scissors" and c == "scissors":
#     print("It's a tie!")

