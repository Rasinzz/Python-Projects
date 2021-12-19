def getWinner(player1, player2):
    player1_wins = "Player 1 wins!"
    player2_wins = "Player 2 wins!"
    tie = "Tie!"

    if player1 == "rock":
        if player2 == "rock":
            return tie
        elif player2 == "paper":
            return player2_wins
        elif player2 == "scissors":
            return player1_wins
        else:
            return "Invalid input"
    elif player1 == "paper":
        if player2 == "rock":
            return player1_wins
        elif player2 == "paper":
            return tie
        elif player2 == "scissors":
            return player2_wins
        else:
            return "Invalid input"
    elif player1 == "scissors":
        if player2 == "rock":
            return player2_wins
        elif player2 == "paper":
            return player1_wins
        elif player2 == "scissors":
            return tie
        else:
            return "Invalid input"
    else:
        return "Invalid input"

while True:
    print("Lets play Rock Paper Scissors!")
    player1_choice = str(input("(Player 1) Enter your choice (rock/paper/scissors): "))
    player2_choice = str(input("(Player 2) Enter your choice (rock/paper/scissors): "))

    print(getWinner(player1_choice, player2_choice))

    keepPlaying = str(input("Would you like to keep playing? (yes/no): "))

    if keepPlaying.lower() == "yes":
        continue
    elif keepPlaying.lower() == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input")