#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import sys
from cipher_funcs import CipherFuncs, cmd_handles, clipboard
from crypto_funcs import mod_inverse

char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~'
char_set_len = len(char_set)


def affine(text="", option="", key=""):
    affine_cipher = CipherFuncs(text, option, key)
    text, option, key = affine_cipher.call_source()

    key_a, key_b = compute_keys(key)

    cipher_text = encrypt_decrypt(text, option, key_a, key_b)
    return clipboard(cipher_text)


def encrypt_decrypt(message, option, key_a, key_b):
    if option.startswith('e'):
        return encrypt(key_a, key_b, message)
    else:
        return decrypt(key_a, key_b, message)


def encrypt(key_a, key_b, message):
    cipher_text = ""

    for char in message:
        if char in char_set:
            char_index = char_set.find(char)
            cipher_text += char_set[(char_index * key_a + key_b) % char_set_len]
        else:
            cipher_text += char  # leave this character unencrypted

    return cipher_text


def decrypt(key_a, key_b, message):
    decrypt_text = ""

    for char in message:
        if char in char_set:
            char_index = char_set.find(char)
            decrypt_text += char_set[((char_index - key_b) * mod_inverse(key_a, char_set_len)) % char_set_len]
        else:
            decrypt_text += char

    return decrypt_text


def compute_keys(key):
    key_a = int(key) // char_set_len
    key_b = int(key) % char_set_len
    return key_a, key_b

if __name__ == "__main__":
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError("This module should be in the same folder as cipher_funcs.py")

    affine(msg)
