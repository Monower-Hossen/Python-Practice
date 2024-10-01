'''2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score. '''

import random

def game():
    # Simulate the game function which returns a score
    # In a real game, this function would contain the game logic

    return random.randint(0, 100)  # Example: returns a random score between 0 and 100


def read_hi_score(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            if line:
                return int(line)  # Return the hi-score if exists
            else:
                return 0  # Return 0 if the file is blank
    except FileNotFoundError:
        return 0  # If the file does not exist, return 0


def write_hi_score(filename, score):
    with open(filename, 'w') as file:
        file.write(str(score))  # Write the new hi-score to the file


def main():
    hi_score_file = 'Hi-score.txt'

    # Read the current Hi-score
    current_hi_score = read_hi_score(hi_score_file)
    print(f"Current Hi-score: {current_hi_score}")

    # Play the game and get the new score
    new_score = game()
    print(f"New Score: {new_score}")

    # Check if the new score breaks the Hi-score
    if new_score > current_hi_score:
        print("New Hi-score achieved!")
        write_hi_score(hi_score_file, new_score)  # Update the Hi-score
    else:
        print("No new Hi-score.")


if __name__ == "__main__":
    main()

