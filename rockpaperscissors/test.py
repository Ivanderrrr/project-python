import random

player_choice = input("Whats your choices (rock, paper, scissors): ")
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
dict_choice = {"player": player_choice, "computer": computer_choice}

print("player chose " + dict_choice["player"] + " computer chose " + dict_choice["computer"])
if dict_choice["player"] == dict_choice["computer"]:
    print("draw !!!")
elif dict_choice["player"] == "rock":
    if dict_choice["computer"] == "scissors":
        print("your win!!!")
    else:
        print("your lose!!!")
elif dict_choice["player"] == "scissors":
    if dict_choice["computer"] == "paper":
        print("your win!!!")
    else:
        print("your lose!!!")
elif dict_choice["player"] == "paper":
    if dict_choice["computer"] == "rock":
        print("your win!!!")
    else:
        print("your lose!!!")

