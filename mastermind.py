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

def validate_guess():
    print("Validate Guess")


def get_feedback():
    print("Get Guess Feedback")


def display_feedback():
    print("Display Guess Feedback")


def display_color_option():
    print("Display Color Option")


def run_game():
    print("Run Mastermind Game")