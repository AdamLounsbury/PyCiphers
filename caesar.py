#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import string
import sys
from cipher_funcs import CipherFuncs, cmd_handles, clipboard

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase


def caesar(text="", option="", key=""):
    caesar_cipher = CipherFuncs(text, option, key)
    text, option, key = caesar_cipher.call_source()

    cipher_text = encrypt_decrypt(text, option, key)  # cast str key to int
    return clipboard(cipher_text)


def encrypt_decrypt(message, option, key):
    cipher_text = ''
    for char in message:
        if char in alphabet_lower:
            cipher_text += alphabet_lower[find_index(char, key, option)]
        elif char in alphabet_upper:
            cipher_text += alphabet_upper[find_index(char, key, option)]
        else:
            cipher_text += char
    return cipher_text


def find_index(char, key, option):
    if char.islower():
        let_index = alphabet_lower.index(char)
    else:
        let_index = alphabet_upper.index(char)

    if option.startswith('e'):
        if let_index + key < len(alphabet_lower):
            encode_index = let_index + key
        else:
            encode_index = (let_index + key) % len(alphabet_lower)
        return encode_index
    else:
        if let_index + key < len(alphabet_lower):
            decode_index = let_index - key
        else:
            decode_index = (let_index - key) % len(alphabet_lower)
        return decode_index


if __name__ == "__main__":
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError("This module should be in the same folder as cipher_funcs.py")

    caesar(msg)

