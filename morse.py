"""Encrypts and Decrypts Morse Code"""

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    encrypt_text = ""
    for char in message:
        if char == ' ':
            encrypt_text += '/'
        else:
            encrypt_text += MORSE_CODE_DICT[char.upper()] + ' '
    return encrypt_text


def decrypt(message):
    decrypt_text = ""
    morse_codes = message.split('/')
    for code in morse_codes:
        for letter in code.split():
            for key, value in MORSE_CODE_DICT.items():
                if letter == value:
                    decrypt_text += key
                    break
        decrypt_text += ' '
    return decrypt_text


operation = input('Encrypt or Decrypt? ').lower().strip()[0]

if operation == "e":
    message = input('Plain Text: ')
    print(encrypt(message))
else:
    message = input('Cipher: ')
    print(decrypt(message))
