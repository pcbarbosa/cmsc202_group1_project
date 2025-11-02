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
