import os

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

# Checks to see if players files are present and creates a new file if not
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
    validate_file(file_path)
    records = load_records(file_path)  # Load all records from the file as a dictionary

    # Check each record key in a case-insensitive way without modifying the stored key
    for record_key, record_value in records.items():
        if record_key.lower() == key.lower():
            return (record_key, record_value)

    return () # Return an empty tuple if no matching key is found

# Update a record by rewriting the whole file because single entries cannot be edited directly
def update_record(file_path, key, value): 
    validate_file(file_path)
    records = load_records(file_path)  # Load all existing records to use as a reference
    records[key] = value  # The record data that will be updated with the new value

    with open(file_path, "w", encoding="utf-8") as f:
        for record_key, record_value in records.items():
            f.write(f"{record_key}{DELIMETER}{record_value}\n")

def is_username_exist ():
    print("Check Username")

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

def load_all_highscores():
    print("Load all scores")

def save_all_highscores():
    print("Save highest score")

def load_player_highscore():
    print("Load highest score")

def save_player_highscore():
    print("Save player highest score")

def show_leaderboard():
    print("Show thee first five players with the highest score")

def generate_secret_code():
    print("Generate secret code")

def give_feedback():
    print("Show feedback")

def validate_guess():
    print("Validate guess")

def press_enter():
    input("Press Enter to continue... ")

def start_game():
    print("Start game")

def register_player():
    print("Register player")

def login_player():
    print("Login player")

def main():
    print("Main logic contains all functions")

main()