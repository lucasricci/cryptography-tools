"""
https://www.johndcook.com/blog/2019/02/25/prime-test/

https://github.com/tarcisio-marinho/RSA/blob/master/encode.py
"""

import secrets
import gmpy2
import os
from sympy.ntheory.primetest import mr


cwd = os.getcwd()
N = 3825123056546413051
ps = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def multiply(x, y):
    return x * y


def mod_inverse(e, phi):
    return int(gmpy2.invert(e, phi))


def totient(p, q):
    return (p - 1) * (q - 1)


def generate_large_prime(bits):
    while True:
        num = secrets.randbits(bits)
        if num % 2 == 0:
            num += 1
        if mr(num, ps):
            return num


def encrypt(plaintext, pub_key):
    n, e = pub_key
    i = 0
    cipher = []
    while i < len(plaintext):
        letter = plaintext[i]
        k = ord(letter)
        c = gmpy2.powmod(k, e, n)
        cipher.append(c)
        i += 1
    return cipher


def decrypt(ciphertext, priv_key):
    n, d = priv_key
    i = 0
    plaintext = []
    while i < len(ciphertext):
        og = gmpy2.powmod(ciphertext[i], d, n)
        letra = chr(og)
        plaintext.append(letra)
        i += 1
    return plaintext


if __name__ == "__main__":
    # Here we calculate two random large prime numbers
    p = generate_large_prime(1024)
    q = generate_large_prime(1024)
    while p == q:
        q = generate_large_prime(1024)

    # Modulus of n = p x q
    n = multiply(p, q)

    # Totient of phi(n)
    t = totient(p, q)

    # For efficiency and security reasons
    e = 65537

    # Keys
    d = mod_inverse(e, t)
    public_key = (n, e)
    private_key = (n, d)

    msg = input("What message you want to encrypt? ")
    print(f"Encrypted Message: {encrypt(msg, public_key)}")

    public_key_path = os.path.join(cwd, "public_key")
    private_key_path = os.path.join(cwd, "private_key")

    with open(public_key_path, "w") as f:
        f.write(repr(public_key))
    with open(private_key_path, "w") as f:
        f.write(repr(private_key))
