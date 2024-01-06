import random

def get_choices():
    player_choice = input("Whats your choices (rock, paper, scissors): ")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    dict_choice = {"player": player_choice, "computer": computer_choice}
    return dict_choice

def check_win(player, computer):
    print(f"player chose: {player}, and computer chose: {computer}")
    if player == computer:
        return "draw !!"
    elif player == "rock":
        if computer == "scissors":
            return "Your win !!!"
        else:
            return "Your lose !!!"
    elif player == "scissors":
        if computer == "paper":
            return "Your win !!!"
        else:
            return "Your lose !!!"
    elif player == "paper":
        if computer == "rock":
            return "Your win !!!"
        else:
            return "Your lose !!!"

getChoise = get_choices()
result = check_win(getChoise["player"], getChoise["computer"])
print(result)