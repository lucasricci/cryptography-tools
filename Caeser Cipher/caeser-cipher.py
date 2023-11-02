"""Encrypts and Decrypts Caeser Cipher"""

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord("A")
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord("A")
            encrypted_char = chr((ord(char) - base - shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


operation = input("Encryption or Decryption? ").lower().strip()[0]

if operation == "e":
    plain_text = input("Plain Text: ").upper()
    shift = int(input("Shift [0-25]: "))
    print(encrypt(plain_text, shift))
else:
    encrypted_text = input("Encrypted Text: ").upper()
    for c in range(1, 27):
        print(f"Shift = {c}\n{decrypt(encrypted_text, c)}")