import random

# Constant variables. Any change here will affect the entire program
PLAYER_FILE = "players.txt"
HIGHSCORES_FILE = "highscores.txt"
SECRET_CODE_LENGTH = 4
MAX_ATTEMPTS = 10
CAESAR_SHIFT = 9
DELIMETER = ":"
COLOR_SET = { 
    "R": "Red", 
    "G": "Green", 
    "B": "Blue", 
    "Y": "Yellow", 
    "W": "White", 
    "O": "Orange" 
}


# Pause the program until the user presses Enter
def press_continue():
    input("Press [Enter] to continue ")


def validate_file():
    print("Validate file")


def save_record():
    print("Save Record")


def load_records():
    print("Load Record")


def get_record():
    print("Get Record")


def update_record():
    print("Update Record")


def save_player():
    print("Save Record")


def save_player_highscore():
    print("Save Highscore")
        

def load_player():
    print("Load Player")


def load_player_highscore():
    print("Load Highscore")


def load_all_player_highscore():
    print("Load all Highscore")


def caesar_shift():
    print("Caesar Shift")


def encrypt_password():
    print("Encrypt Password")


def decrypt_password():
    print("Decrypt Password")


def run_authentication():
    print("Login or Register")


def display_leaderboard():
    print("Display Leaderboard")


def generate_secret_code():
    color_keys = list(COLOR_SET.keys())
    secret_code = random.choices(color_keys, k=SECRET_CODE_LENGTH)
    return "".join(secret_code).upper()


def validate_guess(guess):
    # Validate the guess input
    if not guess:
        print(f"\nYour guess should not be empty.")
        return False

    # Validate the length of the guess
    if len(guess) != SECRET_CODE_LENGTH:
        print(f"\nYour guess contain [{SECRET_CODE_LENGTH}] letters.")
        return False

    invalid_keys = []

    # Collect all invalid color keys
    for key in guess:
        if key not in COLOR_SET:
            invalid_keys.append(key)

    # Validate the guess and display the incorrect color keys
    if invalid_keys:
        print("\nInvalid color key in your input.")
        print("These color keys are invalid:", " ".join(f"[{key}]" for key in invalid_keys))
        return False

    return True


def get_feedback(guess, secret_code):
    color_counts = {} # Store counts of unmatched colors in the secret code
    peg_list = [] # List of peg results for the guess

    # Create the default peg list based on the length of the secret code
    for i in range(SECRET_CODE_LENGTH):
        peg_list.append("O")

    # Check first for the black peg
    for i in range(SECRET_CODE_LENGTH):
        # Insert black peg if guess is correct and in the correct position
        if guess[i] == secret_code[i]:
            peg_list[i] = "B"
        
        # Track how many times each unmatched color appears in the secret code
        else:
            color = secret_code[i]
            if color not in color_counts:
                color_counts[color] = 1
            
            else:
                color_counts[color] += 1

    # Check next whether the remaining guess color is white peg or empty peg
    for i in range(SECRET_CODE_LENGTH):
        # Skip positions that are already black pegs
        if peg_list[i] == "B":
            continue

        guess_color = guess[i]
        current_color_count = color_counts.get(guess_color, 0)

        # Check whether the guess color has already been use or not
        if current_color_count > 0:
            peg_list[i] = "W" # Insert white peg if guess is correct but in the wrong position
            color_counts[guess_color] -= 1 # Reduce the remaining count for this color to prevent double counting
        
        else:
            peg_list[i] = "O" # Insert an empty peg if the current color's remaining count is 0

    return peg_list


def display_feedback(player_attempts, attempt, black_peg_count, white_peg_count):
    header_width = SECRET_CODE_LENGTH * 5 + 1
    default_guess = []
    default_feedback = []

    # Create the default guess result
    for i in range(SECRET_CODE_LENGTH):
        default_guess.append("O")

    # Create the default feedback result
    for i in range(SECRET_CODE_LENGTH):
        default_feedback.append("O")

    # Display the header
    print(f"\n{'GUESS':^{header_width}}{'FEEDBACK':^{header_width}}")

    # Display all guesses and their corresponding feedback
    for i in range(MAX_ATTEMPTS):
        if i < len(player_attempts):
            guess_list = player_attempts[i][0]
            feedback_list = player_attempts[i][1]
            print(guess_list, feedback_list)
        
        else:
            print(default_guess, default_feedback)
    
    # Display the current attempt number and peg counts
    print(f"\nAttempt Number: [{attempt}/{MAX_ATTEMPTS}] | Black Pegs: [{black_peg_count}] | White Pegs: [{white_peg_count}]")


def display_color_option():
    print (f"Choose [{SECRET_CODE_LENGTH}] colors using the letters below:")
    for key in COLOR_SET:
        print(f"[{key}] {COLOR_SET[key]}")


def run_game():
    secret_code = generate_secret_code() # Generate the secret code
    attempts = 1
    player_attempts = [] # Stores every guess made by the player

    # Continue the game until the player runs out of attempts
    while attempts <= MAX_ATTEMPTS:
        print("\n-------------- Game Screen --------------\n")
        # print(f"SECRET CODE: [{secret_code}]") # Uncomment this line for testing purposes
        display_color_option()
        guess = input(f"\n[Attempt {attempts}/{MAX_ATTEMPTS}] Enter your guess: ").strip().upper()

        # Validate the guess input
        if not validate_guess(guess):
            continue

        feedback = get_feedback(guess, secret_code)  # Get the feedback for the guess
        black_peg_count = feedback.count("B") # Get the number of black pegs
        white_peg_count = feedback.count("W") # Get the number of white pegs
        player_attempts.append([list(guess), feedback]) # Record this attempt

        display_feedback(player_attempts, attempts, black_peg_count, white_peg_count)
        
        # End the game if the player guesses the correct secret code and return the remaining attempts as their score
        if black_peg_count == SECRET_CODE_LENGTH:
            print(f"\nCongratulations! You guessed the secret code [{secret_code}]. Your score is [{attempts}]")
            press_continue()
            
            return attempts

        if attempts == MAX_ATTEMPTS:
            print(f"\nGame over! The secret code was [{secret_code}]")
            press_continue()
            return 0
        
        attempts += 1 # Increase the remaining attempt count by 1
        press_continue()