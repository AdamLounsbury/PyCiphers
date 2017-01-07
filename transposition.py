#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

from math import ceil
from sys import argv


def transposition_cipher(txt):
    """Encode or decode a string using the transposition cipher."""

    def encrypt_decrypt():
        """Retrieve cipher operation(encrypt/decrypt) and cipher key (if not using 'all') information from the user"""
        while True:
            option = raw_input("Encrypt/Decrypt (e/d)?: ")
            if option == 'd' or option == 'e':
                break
            else:
                print 'Please choose a valid option for decryption/encryption.'

        while True:
            try:
                transpos_key = int(raw_input('Enter an encryption/decryption key: '))  # indicates 'row' size
                if int(transpos_key):
                    operation(option, transpos_key)
                    break
            except ValueError:
                print "Please enter an integer value for the encryption key."

    def operation(enc_dec, transpos_key):

        str_len = len(txt) # length of the input text
        col_size = int(ceil(float(str_len) / transpos_key)) # encoding column size

        def encode():
            encode_new_str = [''] * transpos_key

            for i in range(transpos_key):
                col_loc = 0  # current location in a column
                for j in range(col_size):
                    if (i + col_loc) < str_len:
                        encode_new_str[i] += txt[i + col_loc]
                        col_loc += transpos_key

            print ''.join(encode_new_str)

        def decode():
            no_char = (col_size * transpos_key) - str_len  # number of 'shaded' boxes
            decode_new_str = [''] * col_size

            row = 0
            col = 0

            for char in txt:
                decode_new_str[col] += char
                col += 1

                if (col == col_size) or (col == col_size - 1 and row >= transpos_key - no_char):
                    col = 0
                    row += 1

            print ''.join(decode_new_str)

        if ('e' or 'E') in enc_dec:
            return encode()
        else:
            return decode()

    encrypt_decrypt()

if __name__ == '__main__':
    text = ''
    script = argv
    word_num = len(argv)

    # append command line string arguments into a variable
    for k in range(1, word_num):
        if k == (word_num - 1):
            text += argv[k]
        else:
            text += argv[k] + ' '

    transposition_cipher(text)
