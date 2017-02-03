#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import math
import sys

from cipher_funcs import CipherFuncs, cmd_handles, clipboard


def transposition(text='', option='', key=''):
    """Instantiate a CipherFuncs class for the Transposition cipher, obtaining all required parameters from the user
    based off of what arguments were initially provided and how this method was called.
    """

    transposition_cipher = CipherFuncs(text, option, key)
    text, option, key = transposition_cipher.call_source()

    cipher_text = encrypt_decrypt(text, option, key)  # cast str key to int
    return clipboard(cipher_text)


def encrypt_decrypt(message, option, key):
    """Apply the Transposition cipher to a string based on the option provided by calling the appropriate cipher
    method (i.e. encryption or decryption).
    """

    str_len = len(message)  # length of the input text
    col_size = int(math.ceil(float(str_len) / key))  # encoding column size

    if option.startswith('e'):
        return encrypt(message, col_size, key, str_len)
    else:
        return decrypt(message, col_size, key, str_len)


def encrypt(message, col_size, key, str_len):
    """Encrypt a string using the Transposition cipher."""

    encode_new_str = [''] * key

    for i in range(key):
        col_loc = 0  # current location in a column
        for j in range(col_size):
            if (i + col_loc) < str_len:
                encode_new_str[i] += message[i + col_loc]
                col_loc += key

    return ''.join(encode_new_str)


def decrypt(message, col_size, key, str_len):
    """Decrypt a string using the Transposition cipher."""

    no_char = (col_size * key) - str_len  # number of 'shaded' boxes
    decode_new_str = [''] * col_size

    row = 0
    col = 0

    for char in message:
        decode_new_str[col] += char
        col += 1

        if (col == col_size) or (col == col_size - 1 and row >= key - no_char):
            col = 0
            row += 1

    return ''.join(decode_new_str)

if __name__ == '__main__':
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError('This module should be in the same folder as cipher_funcs.py')

    transposition(msg)
