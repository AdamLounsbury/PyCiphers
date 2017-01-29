#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import string
import sys
from cipher_funcs import CipherFuncs, cmd_handles, clipboard


def substitution(text="", option="", key=""):
    substitution_cipher = CipherFuncs(text, option, key)
    text, option, key = substitution_cipher.call_source()

    cipher_text = encrypt_decrypt(text, option, key)
    print cipher_text
    clipboard(cipher_text)


def encrypt_decrypt(text, option, key):
    cipher_text = ""

    char_set = string.ascii_lowercase
    key_1 = key

    if option.startswith('d'):
        char_set, key_1 = key_1, char_set

    for char in text:
        if char.lower() in char_set:
            char_index = char_set.find(char.lower())
            if char.isupper():
                cipher_text += key_1[char_index].upper()
            else:
                cipher_text += key_1[char_index]
        else:
            cipher_text += char

    return cipher_text


if __name__ == "__main__":
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError("This module should be in the same folder as cipher_funcs.py")

    substitution(msg)
