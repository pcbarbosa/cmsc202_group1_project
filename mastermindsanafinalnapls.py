import os
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

# Shift each letter in the text by the value of CAESAR_SHIFT while non-letters remain unchanged
def caesar_shift(text, shift): 
    result = ""
    for character in text:
        if "A" <= character <= "Z":
            result += chr((ord(character) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= character <= "z":
            result += chr((ord(character) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += character

    return result


def encrypt_password(password): 
    return caesar_shift(password, CAESAR_SHIFT)


def decrypt_password(password): 
    return caesar_shift(password, -CAESAR_SHIFT)

# adding variable - Rin
def reset_player_password(username):
    player_record = get_record(PLAYER_FILE,username)
    if not player_record:
        print(f'\nPlayer username [{username}] does not exist.')
        return

    new_password = input("Enter your new password: ").strip()
    confirm_password = input("Confirm new password: ").strip()

    if not new_password:
        print ("Password field can't be empty.")
        return

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    encrypted_new_password = encrypt_password(new_password)
    update_record(PLAYER_FILE, username, encrypted_new_password)
    print(f'Password for [{username} has been successfully updated!')

# Check if file exist. If not create an empty txt file and display that it has been created
def validate_file(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8"): 
            print(f"Created new file called [{path}]")


# Save a new record to the specified file by appending it to the end of the file
def save_record(file_path, key, value):
    validate_file(file_path)
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{key}{DELIMETER}{value}\n")


# Reads the specified file and returns its contents as a dictionary
def load_records(file_path):
    validate_file(file_path)
    records = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for record in f:
            # Process only records that contain the delimiter
            if DELIMETER in record:
                key, value = record.strip().split(DELIMETER, 1) # Split the record based on the delimiter
                records[key] = value # Insert the record into the dictionary

    return records # Return an empty dictionary if not found


# Get a single record as a tuple from the specified file
def get_record(file_path, key):
    records = load_records(file_path)  # Load all records from the file as a dictionary

    # Check each record key in a case-insensitive way without modifying the stored key
    for record_key, record_value in records.items():
        if record_key.lower() == key.lower():
            return (record_key, record_value)

    return () # Return an empty tuple if no matching key is found


# Update a record by rewriting the whole file because single entries cannot be edited directly
def update_record(file_path, key, value):
    records = load_records(file_path)  # Load all existing records to use as a reference
    records[key] = value  # The record data that will be updated with the new value

    with open(file_path, "w", encoding="utf-8") as f:
        for record_key, record_value in records.items():
            f.write(f"{record_key}{DELIMETER}{record_value}\n")


# Save a new record for the player if it does not already exist
def save_player(username, password):
    player_record = get_record(PLAYER_FILE, username)

    if not player_record:
        encrypted_password = encrypt_password(password) # Encrypt the password using Caesar Cipher
        save_record(PLAYER_FILE, username, encrypted_password)
        print(f"Player username [{username}] data has been saved.")
        return username
    
    else:
        stored_username, stored_password = player_record
        print(f"Player username [{stored_username}] already exists.")
        return None


# Save or update the player's high score depending on whether the record exists
def save_player_highscore(username, highscore):
    player_record = get_record(HIGHSCORES_FILE, username)

    if not player_record:
        save_record(HIGHSCORES_FILE, username, highscore)
        print(f"Player username [{username}] high score has been saved.")

    else:
        stored_username, stored_highscore = player_record
        update_record(HIGHSCORES_FILE, stored_username, highscore)
        print(f"Player username [{stored_username}] high score has been updated.")
        

# Load an existing player and verify password
def load_player(username, password):
    player_record = get_record(PLAYER_FILE, username)

    if not player_record:
        print(f"\nPlayer username [{username}] does not exist.")
        return None
    
    else:
        stored_username, stored_password = player_record
        decrypted_password = decrypt_password(stored_password)  # Decrypt the password using Caesar Cipher

        # Password is case-sensitive
        if decrypted_password == password:
            print(f"\nLogin successful! Welcome back [{stored_username}].")
            return stored_username
        
        else:
            print("\nPassword is incorrect.")
            return None


# Load the high score of an existing player
def load_player_highscore(username):
    player_record = get_record(HIGHSCORES_FILE, username)

    if not player_record:
        return 0

    try:
        stored_username, stored_highscore = player_record
        return int(stored_highscore) # Convert string to int
    except Exception:
        return 0 # Return 0 if the record cannot be loaded or the stored score is invalid


# Load all player highscores and return a list of tuple
def load_all_player_highscore():
    player_records = load_records(HIGHSCORES_FILE)
    valid_player_records = {}

    # Convert value from the dictionary to int data type. Skip those that are not int
    for username, highscore in player_records.items():
        if str(highscore).isdigit():
            valid_player_records[username] = int(highscore)

    return valid_player_records


def run_authentication(mode):
    while True:
        if mode == "register":
            print("\n-------------- Player Registration Screen --------------\n")
        
        elif mode == "login":
            print("\n-------------- Player Login Screen --------------\n")
        
        else:
            return None

        username = input("Enter your username or enter [E] to go back to the main screen: ").strip()

        # Go back to the main screen if the user chooses to exit
        if username.lower() == "e":
            return None

        # Validate username input
        if not username:
            print("Username can't be empty.")
            continue

        if DELIMETER in username:
            print(f"Username cannot contain the delimiter character: [{DELIMETER}]")
            continue

        # REGISTER MODE 
        if mode == "register": 
            password = input("Enter password: ").strip() 
            if not password: 
                print("Password can't be empty.") 
                continue 

            player_record = save_player(username, password)
            if player_record: 
                return player_record
            else: 
                press_continue() 
                continue 

        # LOGIN MODE 
        elif mode == "login": 
            player_record = get_record(PLAYER_FILE, username) 

        # Check if username exists before asking for password
 
            if not player_record: 
                print(f"\nPlayer username [{username}] does not exist.") 
                press_continue() 
                continue 

        # Only ask password after confirming username 
        password = input("Enter password: ").strip() 
        if not password: 
            print("Password can't be empty.") 
            continue 

        stored_username, stored_password = player_record 
        decrypted_password = decrypt_password(stored_password) 

        if decrypted_password == password: 
            print(f"\nLogin successful! Welcome back [{stored_username}].")
            return 

        else: 
            print("\nPassword is incorrect.") 
            forgot_choice = input("\nForgot your password? [Y/N]: ").strip().lower() 
            if forgot_choice == "y": 
                reset_choice = input("Would you like to reset your password? [Y/N]: ").strip().lower()
                if reset_choice == "y": 
                    reset_player_password(username) 
                    press_continue() 
                    continue 
            
            print("Try logging in again.") 
            press_continue() 
            continue
            

def display_leaderboard():
    print("\n-------------- Leaderboard Screen --------------\n")
    highscore_records = load_all_player_highscore()
    # Sort by lowest to highest score and show only the top 5 player records
    sorted_highscore_records = sorted(highscore_records.items(), key=lambda item: item[1], reverse=False)[:5]

    print(f"{'PLAYER':<20}{'SCORE'}")
    
    for username, highscore in sorted_highscore_records:
        print(f"{username:<20}{highscore}")


# Pause the program until the user presses Enter
def press_continue():
    input("Press [Enter] to continue ")

# Stores game instructions as a function
def show_instructions():
    print('''
             -------------- MASTERMIND GAME INSTRUCTIONS --------------
                      
Welcome to Mastermind! In this game, your goal is to guess a secret sequence of four colors
within a limited number of tries.
                      
SETUP
A random sequence of four colors will be generated. There are six possible colors to choose from:
Red (R), Green (G), Blue (B), Yellow (Y), White (W), and Orange (O).
Note: The colors in the secret code may be repeated.\n
                      
HOW TO PLAY
Type a string of four letters (e.g. RGBY) to make your guess. After each guess, you’ll receive
feedback in the form of pegs:
• If you have guessed a correct color in the correct position, a black peg will be placed in the
position of that color, as indicated by a letter “B”.
• If you have guessed a correct color in the wrong position, a white peg will be placed in the
position of that color, as indicated by a letter “W”.
• If you have guessed a color that is not in the secret code, no pegs will be placed in the
position of that color, as indicated by “O”.
                      
Example: A feedback of “BWOB” means you have guessed two correct colors in the correct
position, one correct color in the wrong position, and one color not in the secret code.
                      
You win when you crack the secret code and collect four black pegs (BBBB) within the guess limit.
                      
Challenge your friends in the leaderboards to see who can break the code in the fewest tries!
''')


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

        
def main():
    is_running = True
    player_username = None
    player_highscore = 0

    while is_running:

        # Authentication Loop
        while not player_username:
            print("\n-------------- Authentication Screen --------------\n")
            print("Press the following key to continue:")
            print("[R] Register a new account")
            print("[L] Login to an existing account")
            print("[H] View game mechanics and instructions")
            print("[E] Exit the program")

            choice = input("\nEnter choice: ").strip().lower()

            if choice == "r":
                player_username = run_authentication("register")
                if player_username:
                    player_highscore = 0

            elif choice == "l":
                player_username = run_authentication("login")
                if player_username:
                    player_highscore = load_player_highscore(player_username)
            
            elif choice == "h":
                show_instructions()
                press_continue()
                continue

            elif choice == "e":
                print("\nExiting the program. Goodbye!")
                is_running = False
                return
            
            else:
                print (f"\n[{choice}] is not a valid choice. Please try again.")

        # Dashboard Loop
        while True:
            print("\n-------------- Dashboard Screen --------------\n")
            print(f"Player Name: [{player_username}] | High Score: [{'None' if player_highscore == 0 else player_highscore}]\n")
            print("Press the following key to continue:")
            print("[S] Start the game")
            print("[D] Display the leaderboard")
            print("[L] Logout")
            print("[E] Exit the program")

            choice = input("\nEnter choice: ").strip().lower()

            if choice == "s":
                # Start the game to get the score
                player_new_score = run_game()
                # Check whether the player manage to guess the secret code
                if player_new_score != 0:
                    # Save the new score if player has no highscore yet
                    if player_highscore == 0:
                        save_player_highscore(player_username, player_new_score)
                        player_highscore = player_new_score
                        print(f"\nCongratulations! You got a new high score: [{player_new_score}]")

                    else:
                        # Save the score if the new score has lower attempts
                        if player_new_score < player_highscore:
                            save_player_highscore(player_username, player_new_score)
                            player_highscore = player_new_score
                            print(f"\nCongratulations! You got a new high score: [{player_new_score}]")

            elif choice == "d":
                display_leaderboard()
            

            elif choice == "l":
                print("\nLogging out!")
                player_username = None
                player_highscore = 0
                break

            elif choice == "e":
                print("\nExiting the program. Goodbye!")
                is_running = False
                return
            
            else:
                print (f"\n[{choice}] is not a valid choice. Please try again.")

 
main()
