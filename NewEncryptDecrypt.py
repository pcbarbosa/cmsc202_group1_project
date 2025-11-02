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