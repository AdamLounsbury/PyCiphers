#!/usr/bin/env python
# ACL 2017 - alounsbu@alumni.uwo.ca

import sys

import vigenere
import transposition
import affine
import caesar
import substitution

from code_break import CodeBreak
from cipher_funcs import clipboard

cipher_dict = {1: caesar.caesar, 2: transposition.transposition, 3: affine.affine, 4: vigenere.vigenere,
               5: substitution.substitution}


def main():
    """Menu display of available operations"""

    print '\nWelcome! Please input a numbered option below\n'
    print '1) Single encryption'
    print '2) Multiple encryption (with random key generation)'
    print '3) Single decryption'
    print '4) Brute-force code breaking'
    print '5) Quit\n'

    main_choice = raw_input('> ')

    if main_choice == '1':
        return single_encryption_decryption('e')
    elif main_choice == '2':
        cipher_text = multiple_encryption()
        return clipboard(cipher_text)
    elif main_choice == '3':
        return single_encryption_decryption('d')
    elif main_choice == '4':
        return code_break()
    elif main_choice == '5' or main_choice.startswith('q'):
        sys.exit()
    else:
        print 'Invalid choice'
        return main()


def single_ciphers():
    """Menu display of currently implemented ciphers."""

    print '1) Caesar'
    print '2) Transposition'
    print '3) Affine'
    print '4) Vigenere'
    print '5) Substitution\n'


def cipher_run(choice, option):
    """Pass user's cipher choice to the appropriate cipher and execute that cipher."""

    if choice.isdigit() and 0 < int(choice) <= 5:
        cipher_dict[int(choice)](option=option)
    elif choice.startswith('q'):
        sys.exit()
    else:
        print 'Invalid choice, please choose a valid option\n'
        choice = raw_input('> ')
        return cipher_run(choice, option)


def single_encryption_decryption(option):
    """Prompt user for a cipher and pass that choice off for validation."""

    print '\nPlease choose a cipher\n'
    single_ciphers()
    choice = raw_input('> ')
    return cipher_run(choice, option)


def multiple_encryption():
    """Prompt user for a sequence of ciphers, which are called sequentially on a string."""

    print '\nPlease enter a string to be encrypted\n'

    cipher_text = raw_input('> ')

    print '\nPlease enter a sequence of numbers (1-5) that represent the ciphers you wish to execute on a string'
    print 'An example input might be 423, which would execute the vigenere, transposition, and affine ciphers ' \
          'sequentially, using randomly-generated keys for each (each key will be displayed)\n'

    single_ciphers()
    sequence = sequence_prompt()

    for func in sequence:
        # [int(func) - 1] is used due to cipher_dict using non-zero labeling for ease of human use.
        cipher_text = cipher_dict.items()[int(func)-1][1](cipher_text, 'e', 'random')

    return cipher_text


def sequence_prompt():
    """Prompt the user for a sequence of ciphers in integer format and then validate that sequence."""

    sequence = raw_input('> ')
    print '\n'

    try:
        for i in sequence:
            if int(i) <= 0 or int(i) > 5:
                print 'Invalid sequence\n'
                return sequence_prompt()
        else:
            return sequence
    except ValueError:
        print 'Please enter a numerical sequence\n'
        return sequence_prompt()


def code_break():
    """Prompt the user for a string for brute-force decryption."""

    print '\nPlease enter a string for attempted brute-force decryption\n'

    cipher_text = raw_input('> ')

    try:
        assert len(cipher_text) > 0
    except AssertionError:
        print 'Please enter a valid string'
        return code_break()

    decrypt = CodeBreak(cipher_text)
    decrypt.code_break()

if __name__ == '__main__':
    main()
