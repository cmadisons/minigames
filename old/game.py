import random

CHOICES = ("rock", "paper", "scissors", "match")
# Each choice maps to the set of choices it beats.
BEATS = {
    "rock": {"scissors", "match"},
    "paper": {"rock"},
    "scissors": {"paper", "match"},
    "match": {"paper"},
}


def get_player_choice():
    while True:
        raw = input("Choose rock, paper, scissors, or match (or 'q' to quit): ").strip().lower()

        if raw in ("q", "quit", "exit"):
            return None

        # Allow shorthand like r/p/s/m.
        shorthand = {"r": "rock", "p": "paper", "s": "scissors", "m": "match"}
        if raw in shorthand:
            return shorthand[raw]

        if raw in CHOICES:
            return raw

        print("Sorry, I didn't understand that. Try again.")


def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if computer in BEATS[player]:
        return "player"
    return "computer"


def main():
    wins = losses = ties = 0

    print("Let's play Rock Paper Scissors!")

    while True:
        player = get_player_choice()
        if player is None:
            break

        computer = random.choice(CHOICES)
        print(f"You chose {player}. I chose {computer}.")

        result = decide_winner(player, computer)
        if result == "tie":
            ties += 1
            print("It's a tie!")
        elif result == "player":
            wins += 1
            print(f"{player.capitalize()} beats {computer}. You win!")
        else:
            losses += 1
            print(f"{computer.capitalize()} beats {player}. You lose!")

        print(f"Score - Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

    print(f"\nThanks for playing! Final score - Wins: {wins}, Losses: {losses}, Ties: {ties}")


if __name__ == "__main__":
    main()
