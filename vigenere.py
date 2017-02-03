#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import string
import sys
from cipher_funcs import CipherFuncs, cmd_handles, clipboard

char_set = string.ascii_lowercase


def vigenere(text="", option="", key=""):
    vigenere_cipher = CipherFuncs(text, option, key)
    text, option, key = vigenere_cipher.call_source()

    cipher_text = encrypt_decrypt(text, option, key)
    return clipboard(cipher_text)


def encrypt_decrypt(message, option, key):
    cipher_text = ""
    key_index = 0

    for char in message:
        if char.lower() in char_set:  # alphabet provided is all lower case - used to search for capital letters
            msg_let_index = char_set.find(char.lower())  # ex: '20' for t
            key_let_index = char_set.find(key[key_index])  # ex: '2' for b

            if option.startswith('e'):
                encode_text = (msg_let_index + key_let_index) % len(char_set)
            elif option.startswith('d'):
                encode_text = (msg_let_index - key_let_index) % len(char_set)

            if char.islower():
                cipher_text += char_set[encode_text]
            elif char.isupper():
                cipher_text += char_set[encode_text].upper()

            key_index += 1
            if key_index == len(key):  # when the end of the key is reached, wrap back to the start
                key_index = 0

        else:
            cipher_text += char

    return cipher_text

if __name__ == "__main__":
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError("This module should be in the same folder as cipher_funcs.py")

    vigenere(msg)
