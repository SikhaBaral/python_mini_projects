import random
def roll_on():
    min_Value = 1
    max_Value = 6
    rolling_Value = random.randint(min_Value, max_Value)
    return rolling_Value


while True:
    players = input("Enter the number of players (2 to 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players")
    else:
        print("Invalid User Input! Try Again!")

max_Score = 20
players_Score = [0 for _ in range(players)]
scores_Of_Players = max(players_Score)

while scores_Of_Players <= max_Score:
    for player_Idx in range(players):
        print("Player ", player_Idx + 1, "turn has just begun! \n")
        current_Score = 0

        while True:
            should_Roll = input("Would you like to roll (y)? ")
            if should_Roll.lower() == "Y":
                break

            value = roll_on()
            if value == 1:
                print("You rolled 1. Turn Done!")
                current_Score = 0
                break
            else:
                print("You rolled a ", value)
                current_Score += value
                print("Your current score is ", current_Score)

        players_Score[player_Idx] = current_Score
        print("Your overall score is: ", players_Score[player_Idx])

max_Score = max(players_Score)
players_winning_idx = players_Score.index(max_Score)
print("player", players_winning_idx + 1, "is the winner. ")
