# Global Variables
players_file = "players.txt"
highscores_file = "highscores.txt"
code_length = 4
max_attempts = 10
color_set = {
    "R": "Red",
    "G": "Green",
    "B": "Black",
    "Y": "Yellow",
    "W": "White",
    "O": "Orange",
}

def checker_file():
    print("Check File")

def encrypt_password(password):
    result=""
    for i, ch in enumerate(password):
        code = (ord(ch) - 32 + (i % 5) + 1) % 95 + 32 
        result += chr(code)
    return result[::-1]

def decrypt_password(password):
    password = password[::-1]
    result=""
    for i, ch in enumerate(password):
        code = (ord(ch) - 32 -  (i % 5) - 1) % 95 + 32
        result += chr(code)
    return result

def is_username_exist ():
    print("Check Username")

def save_player ():
    print("Save player")

def load_player():
    print("Load player")

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