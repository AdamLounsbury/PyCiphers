#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

from sys import argv
from random import randrange
from crypto_funcs import gcd, generate_prime, mod_inverse


def keygen(key_size):

    a = generate_prime(key_size)
    b = generate_prime(key_size)
    n = a * b

    # generate a number relatively prime to (p - 1) * (q - 1); will be part of the public key
    while True:
        e = randrange(2 ** (key_size - 1), 2 ** key_size)
        if gcd(e, (a - 1) * (b - 1)) == 1:
            break

    d = mod_inverse(e, (a - 1) * (b - 1))

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def check_key(key):
    try:
        if int(key):
            return key
    except ValueError:
        print "Please enter a key size (eg. 2048)."
        return False


def print_keys(pub, pri):
    txt = open("Public_Key.txt".format(key_size1), "w")
    txt.write("{0},{1},{2}".format(key_size1, pub[0], pub[1]))
    txt.close()

    txt = open("Private_Key.txt".format(key_size1), "w")
    txt.write("{0},{1},{2}".format(key_size1, pri[0], pri[1]))
    txt.close()


if __name__ == "__main__":
    if len(argv) == 1:
        key_size1 = input("Enter a key size for the RSA cipher\n> ")
        if check_key(key_size1):
            public, private = keygen(key_size1)
            print_keys(public, private)

    elif len(argv) == 2:
        key_size1 = int(argv[1])
        if check_key(key_size1):
            public, private = keygen(key_size1)
            print_keys(public, private)
