#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import sys
import vigenere
import transposition
import affine
import caesar
import substitution
from cipher_funcs import clipboard

func_dict = {1: caesar.caesar, 2: transposition.transposition, 3: affine.affine, 4: vigenere.vigenere,
             5: substitution.substitution}


def main():
    print "\nWelcome! Please input a numbered option below (or type 'help' for examples)\n"
    print "1) Single encryption"
    print "2) Sequential encryption (with random key generation)"
    print "3) Single decryption"
    print "4) Brute-force code breaking"
    print "5) Quit\n"

    main_choice = raw_input("> ")

    if main_choice == '1':
        return single_encryption_decryption('e')
    elif main_choice == '2':
        return sequential_encryption()
    elif main_choice == '3':
        return single_encryption_decryption('d')
    elif main_choice == '4':
        return code_break()
    elif main_choice == '5' or main_choice.startswith('q'):
        sys.exit()
    elif main_choice.startswith('h') or main_choice.startswith('H'):
        return examples()
    else:
        print "Invalid choice"
        return main()


def single_ciphers():
    print "1) Caesar"
    print "2) Transposition"
    print "3) Affine"
    print "4) Vigenere"
    print "5) Substitution\n"


def cipher_run(choice, option):
    if choice == 1:
        clipboard(caesar.caesar(option=option))

    elif choice == 2:
        clipboard(transposition.transposition(option=option))

    elif choice == 3:
        clipboard(affine.affine(option=option))

    elif choice == 4:
        clipboard(vigenere.vigenere(option=option))

    elif choice == 5:
        clipboard(substitution.substitution(option=option))

    elif choice.startswith('q'):
        sys.exit()

    else:
        print "Invalid choice"
        return cipher_run(choice, option)


def single_encryption_decryption(option):
    print "\nPlease choose a cipher\n"
    single_ciphers()
    choice = input("> ")
    return cipher_run(choice, option)


def sequential_encryption():
    print "\nPlease enter a string to be encrypted\n"

    cipher_text = raw_input("> ")

    print "\nPlease enter a sequence of numbers (1-5) that represent the ciphers you wish to execute on a string"
    print "An example input might be 423, which would execute the vigenere, transposition, and affine ciphers " \
          "sequentially, using randomly-generated keys for each\n"

    single_ciphers()
    sequence = sequence_prompt()

    cipher_sequence = []

    for cipher in sequence:
        cipher_sequence.append(func_dict[int(cipher)])

    for func in cipher_sequence:
        cipher_text = func(cipher_text, 'e', 'random')

    print '\nfinal cipher text is:', cipher_text


def sequence_prompt():
    sequence = raw_input("> ")
    print '\n'

    for i in sequence:
        if int(i) <= 0 or int(i) > 5:
            print "Invalid sequence"
            return sequence_prompt()
        else:
            return sequence


def code_break():
    pass


def examples():
    pass


if __name__ == "__main__":
    main()
