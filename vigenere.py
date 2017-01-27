import string
import sys
from cipher_funcs import CipherFuncs, cmd_handles

char_set = string.ascii_lowercase


def vigenere(text="", option="", key=""):
    vigenere_cipher = CipherFuncs(text, option, key)

    if not text and not option and not key:  # if vigenere is run as a script with no arguments
        text, option, key = vigenere_cipher.script_call()
        return encrypt_decrypt(text, option, key)

    elif option and not text and not key:  # if vigenere is called from main.py, enc/dec is specified in the menu choice
        text, key = vigenere_cipher.main_call()
        return encrypt_decrypt(text, option, key)

    elif text and not option and not key: # if vigenere is called directly from a CLI with an included string
        option, key = vigenere_cipher.cli_call()
        return encrypt_decrypt(text, option, key)

    else:  # if vigenere is run in the shell with all arguments provided
        valid_choices = vigenere_cipher.shell_call()
        if valid_choices:
            return encrypt_decrypt(text, option, key)
        else:
            print "Try again!\n"


def encrypt_decrypt(message, option, key):
    cipher_text = ""
    key_index = 0

    for char in message:
        if char.lower() in char_set:  # alphabet provided is all lower case - used to search for capital letters
            msg_let_index = char_set.find(char.lower())  # ex: '20' for t
            key_let_index = char_set.find(key[key_index])  # ex: '2' for b

            if option.startswith('e'):
                encode_text = (msg_let_index + key_let_index) % len(char_set)
            elif option.startswith('d'):
                encode_text = (msg_let_index - key_let_index) % len(char_set)

            if char.islower():
                cipher_text += char_set[encode_text]
            elif char.isupper():
                cipher_text += char_set[encode_text].upper()

            key_index += 1
            if key_index == len(key):  # when the end of the key is reached, wrap back to the start
                key_index = 0

        else:
            cipher_text += char

    print cipher_text

if __name__ == "__main__":
    try:
        msg = cmd_handles(sys.argv)
    except NameError:
        raise NameError("This module should be in the same folder as cipher_funcs.py")

    vigenere(msg)
