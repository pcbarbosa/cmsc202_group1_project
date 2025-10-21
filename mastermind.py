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

#checks if players.txt is present in the system, if not, creates one
def checker_file():
    if not os.path.exists(players_file):
        with open(players_file,"w") as file:
            file.write("Name,Password\n")
    print("Check File")

def encrypt_password():
    print("Encrypt Password")

def decrypt_password():
    print("Decrypt Password")

#checks if username already exists in players.txt
def is_username_exist(name):
    checker_file()
    with open(players_file,"r") as file:
        next(file)
        for line in file:
            stored_name = line.strip().split(",")[0]
            if stored_name.lower() == name.lower():
                return True
    return False
    print("Check Username")

#saves new player to players.txt or prompts if username already exists
def save_player (name, password):
    checker_file()
    if is_username_exist(name):
        print ("Username already exists. Please log in or try another username.")
    else:
        if not name.strip() or not password.strip():
         raise ValueError("Name or password cannot be empty.")
        if "," in name or "," in password or "\n" in name or "\n" in password:
         raise ValueError("Commas and line breaks are not allowed in the name or password.")
        with open(players_file, "a") as file:
            file.write(f"{name},{password}\n")
            print("User successfully registered!")
    print("Save player")


#validation to ensure appropriate characters are entered
try:
    save_player(input("Please enter your username: "),input('Please enter your password:'))
except ValueError as e:
    print(e)

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