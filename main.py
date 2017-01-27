import sys

def main():
    print "\nWelcome! Please input a numbered option below (or type 'help' for examples)\n"
    print "1) Single encryption"
    print "2) Sequential encryption (with random key generation)"
    print "3) Single decryption"
    print "4) Brute-force code breaking"
    print "5) Quit\n"

    choice = raw_input("> ")

    if choice == '1':
        return single_encryption()
    elif choice == '2':
        return sequential_encryption()
    elif choice == '3':
        return single_decryption()
    elif choice == '4':
        return code_break()
    elif choice == '5' or choice.startswith('q'):
        sys.exit()
    elif choice.startswith('h') or choice.startswith('H'):
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
    print "5) Substitution"


def cipher_run(choice):
    if choice == 1:
        pass
    elif choice == 4:
        pass
    elif choice.startswith('q'):
        sys.exit()
    else:
        print "Invalid choice"
        return cipher_run(choice)


def single_encryption():
    single_ciphers()
    choice = input("> ")
    return cipher_run(choice)

def sequential_encryption():
    pass


def single_decryption():
    pass


def code_break():
    pass


def examples():
    pass


if __name__ == "__main__":
    main()
