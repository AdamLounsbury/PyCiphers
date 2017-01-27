import sys


def main():
    print "\nWelcome! Please input a numbered option below (or type 'help' for examples)\n"
    print "1) Single encryption"
    print "2) Sequential encryption (with random key generation)"
    print "3) Single decryption"
    print "4) Brute-force code breaking"
    print "5) Quit\n"

    main_choice = raw_input("> ")

    if main_choice == '1':
        return single_encryption()
    elif main_choice == '2':
        return sequential_encryption()
    elif main_choice == '3':
        return single_decryption()
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
    print "\nPlease choose a cipher\n"
    print "1) Caesar"
    print "2) Transposition"
    print "3) Affine"
    print "4) Vigenere"
    print "5) Substitution\n"


def cipher_run(cipher_choice, option):
    if cipher_choice == 4:
        try:
            from vigenere_test import vigenere
            return vigenere(option=option)
        except ImportError:
            print "Couldn't import the vigenere cipher module. Has it been renamed or moved?"
            sys.exit()
    elif cipher_choice.startswith('q'):
        sys.exit()
    else:
        print "Invalid choice"
        if option == 'e':
            return single_encryption()
        else:
            return single_decryption()


def single_encryption():
    single_ciphers()
    cipher_choice = input("> ")
    return cipher_run(cipher_choice, 'e')


def sequential_encryption():
    pass


def single_decryption():
    single_ciphers()
    cipher_choice = input("> ")
    return cipher_run(cipher_choice, 'd')


def code_break():
    pass


def examples():
    pass


if __name__ == "__main__":
    main()
