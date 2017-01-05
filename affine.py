#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

from sys import argv, exit
from crypto_funcs import *


def affine_cipher(txt):
    char_set = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]=^_`abcdefghijklmnopqrstuvwxyz{|}~"""

    def encrypt_decrypt():
        while True:
            option = raw_input("Encrypt/Decrypt (e/d)?: ")
            if option == 'd' or option == 'e':
                key_get(option)
                break
            else:
                print 'Please choose a valid option for decryption/encryption.\n'

    def key_get(option):
        while True:
            user_key = input("Enter an encryption/decryption key: ")
            if int(user_key):
                operation(option, user_key)
                break
            else:
                print "Please enter an integer value for the key.\n"

    def operation(enc_dec, key):
        key_a, key_b = compute_keys(key)
        check_keys(key_a, key_b, enc_dec)

        if ('e' or 'E') in enc_dec:
            return encrypt(key_a, key_b, txt)
        else:
            return decrypt()

    def compute_keys(key):
        key_a = key // len(char_set)
        key_b = key % len(char_set)
        return key_a, key_b

    def check_keys(key_a, key_b, mode):
        if key_a == 1 and mode == 'e':
            print 'The affine cipher is very weak when key A computes to 1. Choose a different key.'
            key_get(mode)
        if key_b == 0 and mode == 'e':
            print 'The affine cipher is very weak when key B computes to 0. Choose a different key.'
            key_get(mode)
        if key_a < 0 or (len(char_set) - 1 < key_b < 0):
            print 'Key A must be greater than 0 and Key B must be between 0 and {0}'.format(len(char_set) - 1)
            key_get(mode)
        if gcd(key_a, len(char_set)) != 1:
            print 'Key A ({0}) and the symbol set size ({1}) are not relatively prime. Choose a different key.'.format(
                key_a, len(char_set))
            key_get(mode)

    def encrypt(key_a, key_b, message):
        cipher_text = ''
        for char in message:
            if char in char_set:
                char_index = char_set.find(char)
                cipher_text += char_set[(char_index * key_a + key_b) % len(char_set)]
            else:
                cipher_text += char # leave this character unencrypted
        print cipher_text

    def decrypt():
        pass

    encrypt_decrypt()

if __name__ == '__main__':
    if len(argv) == 1:
        text = raw_input("Enter a string to be encrypted/decrypted using the affine cipher\n> ")
        affine_cipher(text)
    else:
        text = ''
        script = argv
        word_num = len(argv)

        # append command line string arguments into a variable
        for k in range(1, word_num):
            if k == (word_num - 1):
                text += argv[k]
            else:
                text += argv[k] + ' '

        affine_cipher(text)
