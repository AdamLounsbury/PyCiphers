#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import string
import sys

from cipher_funcs import CipherFuncs, cmd_handles, clipboard

char_set = string.ascii_lowercase


def caesar(text='', option='', key=''):
    """Instantiate a CipherFuncs class for the Caesar cipher, obtaining all required parameters from the user
    based off of what arguments were initially provided and how this method was called.
    """

    caesar_cipher = CipherFuncs(text, option, key)
    text, option, key = caesar_cipher.call_source()

    cipher_text = encrypt_decrypt(text, option, key)  # cast str key to int
    return clipboard(cipher_text)


def encrypt_decrypt(message, option, key):
    """Apply the Caesar cipher to a string."""

    cipher_text = ''
    for char in message:
        if char in char_set:
            cipher_text += char_set[find_index(char, key, option)]
        elif char in char_set.upper():
            cipher_text += char_set.upper()[find_index(char, key, option)]
        else:
            cipher_text += char
    return cipher_text


def find_index(char, key, option):
    """Find and return the index position of a character in the alphabet, shifted by an amount specified by the key."""

    if char.islower():
        let_index = char_set.index(char)
    else:
        let_index = char_set.upper().index(char)

    if option.startswith('e'):
        if let_index + key < len(char_set):
            encode_index = let_index + key
        else:
            encode_index = (let_index + key) % len(char_set)
        return encode_index
    else:
        if let_index + key < len(char_set):
            decode_index = let_index - key
        else:
            decode_index = (let_index - key) % len(char_set)
        return decode_index


if __name__ == '__main__':
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError('This module should be in the same folder as cipher_funcs.py')

    caesar(msg)

