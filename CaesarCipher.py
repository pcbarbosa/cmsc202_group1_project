def encrypt_password(password):
    result=""
    for ch in password:
        if 32 <= ord(ch) <= 126:
            shifted = (ord(ch) - 32 + caesar_shift) % 95 + 32
            result += chr(shifted)
        else:
            result += ch
    return result

def decrypt_password(password):
    result = ""
    for ch in password:
        if 32 <= ord(ch) <= 126:
            shifted = (ord(ch) - 32 - caesar_shift) % 95 + 32
            result += chr(shifted)
        else:
            result += ch
    return result