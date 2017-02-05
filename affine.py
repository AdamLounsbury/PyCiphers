#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import sys

from cipher_funcs import CipherFuncs, cmd_handles, clipboard
from crypto_funcs import mod_inverse

char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~'
char_set_len = len(char_set)


def affine(text='', option='', key=''):
    """Instantiate a CipherFuncs class for the Affine cipher, obtaining all required parameters from the user
    based off of what arguments were initially provided and how this method was called.
    """

    affine_cipher = CipherFuncs(text, option, key)
    text, option, key = affine_cipher.call_source()

    key_a, key_b = compute_keys(key)

    cipher_text = encrypt_decrypt(text, option, key_a, key_b)
    return clipboard(cipher_text)


def encrypt_decrypt(message, option, key_a, key_b):
    """Apply the Affine cipher to a string based on the option provided by calling the appropriate cipher
    method (i.e. encryption or decryption).
    """

    if option.startswith('e'):
        return encrypt(key_a, key_b, message)
    else:
        return decrypt(key_a, key_b, message)


def encrypt(key_a, key_b, message):
    """Encrypt a string using the Affine cipher."""

    cipher_text = ''

    for char in message:
        if char in char_set:
            char_index = char_set.find(char)
            cipher_text += char_set[(char_index * key_a + key_b) % char_set_len]
        else:
            cipher_text += char

    return cipher_text


def decrypt(key_a, key_b, message):
    """Decrypt a string using the Affine cipher."""

    decrypt_text = ''

    for char in message:
        if char in char_set:
            char_index = char_set.find(char)
            decrypt_text += char_set[((char_index - key_b) * mod_inverse(key_a, char_set_len)) % char_set_len]
        else:
            decrypt_text += char

    return decrypt_text


def compute_keys(key):
    """Compute the two keys required for the Affine cipher and return them for validation inside the CipherFuncs
    class.
    """

    key_a = int(key) // char_set_len
    key_b = int(key) % char_set_len
    return key_a, key_b

if __name__ == '__main__':
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError('This module should be in the same folder as cipher_funcs.py')

    affine(msg)
