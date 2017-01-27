#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import random
import string
from sys import argv
from crypto_funcs import *

char_set = string.printable


def affine_cipher(txt, user_option=None, user_key=None):

    def encrypt_decrypt():
        while True:
            option = raw_input("Encrypt/Decrypt (e/d)?: ")
            if option == 'd' or option == 'e':
                return key_get(option)
            else:
                print "Please choose a valid option for decryption/encryption.\n"

    def key_get(option):
        while True:
            key = input("Enter an encryption/decryption key: ")
            if int(key):
                return operation(option, key)
            else:
                print "Please enter an integer value for the key.\n"

    def compute_keys(key):
        key_a = key // len(char_set)
        key_b = key % len(char_set)
        return key_a, key_b

    def check_keys(key_a, key_b, mode):
        if key_a == 1 and mode == 'e':
            print "The affine cipher is very weak when key A computes to 1. Choose a different key.\n"
            key_get(mode)
        elif key_b == 0 and mode == 'e':
            print "The affine cipher is very weak when key B computes to 0. Choose a different key.\n"
            key_get(mode)
        elif key_a < 0 or (len(char_set) - 1 < key_b < 0):
            print "Key A must be greater than 0 and Key B must be between 0 and {0}. Choose a different key.\n".format(
                len(char_set) - 1)
            key_get(mode)
        elif gcd(key_a, len(char_set)) != 1:
            print "Key A ({0}) and the symbol set size ({1}) are not relatively prime.\n".\
                format(key_a, len(char_set))

            if mode == 'e':
                rand_key = raw_input("Would you like a random key to be generated? (y/n): ")
                if 'y' in rand_key:
                    return operation(mode, get_random_key())
                else:
                    key_get(mode)
        else:
            return True  # if the check worked, tell the operation method that it did

    def operation(enc_dec, key):
        key_a, key_b = compute_keys(key)

        if ('e' or 'E') in enc_dec and (user_option is not None):
            print encrypt(key_a, key_b, txt)
        elif (('e' or 'E') in enc_dec) and (check_keys(key_a, key_b, enc_dec) is True) and (user_option is None):
            print encrypt(key_a, key_b, txt)
        elif 'd' in enc_dec:
            print decrypt(key_a, key_b, txt)

    def encrypt(key_a, key_b, message):
        cipher_text = ""

        for char in message:
            if char in char_set:
                char_index = char_set.find(char)
                cipher_text += char_set[(char_index * key_a + key_b) % len(char_set)]
            else:
                cipher_text += char  # leave this character unencrypted

        return cipher_text

    def decrypt(key_a, key_b, message):
        decrypt_text = ""

        for char in message:
            if char in char_set:
                char_index = char_set.find(char)
                decrypt_text += char_set[((char_index - key_b) * mod_inverse(key_a, len(char_set))) % len(char_set)]
            else:
                decrypt_text += char

        return decrypt_text

    def get_random_key():
        while True:
            key_a = random.randint(2, len(char_set))
            key_b = random.randint(2, len(char_set))
            if gcd(key_a, len(char_set)) == 1:
                print "Key is {0}".format(key_a * len(char_set) + key_b)
                return key_a * len(char_set) + key_b

    if (user_option is not None) and (user_key is not None):
        return operation(user_option, user_key)
    else:
        return encrypt_decrypt()

if __name__ == "__main__":
    if len(argv) == 1:
        text = raw_input("Enter a string to be encrypted/decrypted using the affine cipher\n> ")
        affine_cipher(text)
    else:  # handle input from command line
        text = ""
        script = argv
        word_num = len(argv)

        # append command line string arguments into a variable
        for k in range(1, word_num):
            if k == (word_num - 1):
                text += argv[k]
            else:
                text += argv[k] + " "

        affine_cipher(text)
