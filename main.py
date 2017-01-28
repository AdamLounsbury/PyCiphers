import sys
import vigenere, transposition, affine, caesar, substitution


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
    print "\nPlease choose a cipher\n"
    print "1) Caesar"
    print "2) Transposition"
    print "3) Affine"
    print "4) Vigenere"
    print "5) Substitution\n"


def cipher_run(choice, option):
    if choice == 1:
        return caesar.caesar(option=option)
    elif choice == 2:
        return transposition.transposition(option=option)
    elif choice == 3:
        return affine.affine(option=option)
    elif choice == 4:
        return vigenere.vigenere(option=option)
    elif choice == 5:
        return substitution.substitution(option=option)
    elif choice.startswith('q'):
        sys.exit()
    else:
        print "Invalid choice"
        return cipher_run(choice, option)


def single_encryption_decryption(option):
    single_ciphers()
    choice = input("> ")
    return cipher_run(choice, option)


def sequential_encryption():
    pass


def code_break():
    pass


def examples():
    pass


if __name__ == "__main__":
    main()
