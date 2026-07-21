import random


def main():
    target = random.randint(1, 100)
    guesses = 0
    trick_in = random.randint(1, 5)  # lie after this many guesses

    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    print("Careful... I might lie to you every now and then.")

    while True:
        raw = input("Your guess (or 'q' to quit): ").strip().lower()

        if raw in ("q", "quit", "exit"):
            print(f"The number was {target}. Thanks for playing!")
            return

        if not raw.isdigit() or not 1 <= int(raw) <= 100:
            print("Please enter a whole number between 1 and 100.")
            continue

        guess = int(raw)
        guesses += 1

        if guess == target:
            plural = "guess" if guesses == 1 else "guesses"
            print(f"Correct! You got it in {guesses} {plural}.")
            return

        # Decide whether this hint is a lie.
        trick_in -= 1
        lying = trick_in <= 0
        if lying:
            trick_in = random.randint(1, 5)  # schedule the next trick

        higher = guess < target  # the truthful direction
        if lying:
            higher = not higher  # flip it to trick the player

        print("Higher!" if higher else "Lower!")


if __name__ == "__main__":
    main()
