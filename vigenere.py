
from sys import argv

char_set = "abcdefghijklmnopqrstuvwxyz"


def vigenere_cipher(message, user_option=None, user_key=None):

    def encrypt_decrypt_prompt():
        option = raw_input("Encrypt/Decrypt (e/d)?: ")
        if check_option(option):
            return key_get(option)
        else:
            return encrypt_decrypt_prompt()

    def key_get(option):
        key = raw_input("Enter an encryption/decryption key: ")
        key = check_key(key)
        if key:
            return encrypt_decrypt(option, key)
        else:
            return key_get(option)

    def check_option(option):
        if option.startswith('E') or option.startswith('e'):
            option = option.lower()
            return option
        elif option.startswith('D') or option.startswith('d'):
            option = option.lower()
            return option
        else:
            print 'Invalid operation detected. Please enter a valid operation (encryption/decryption).'
            return False

    def check_key(key):

        try:
            key = key.replace(" ", "")  # in case the user enters a string key containing spaces
        except AttributeError:
            print "Please enter a string key."
            return False

        if not isinstance(key, str):
            print "Please enter a string key."
            return False
        elif not key.isalpha():
            print "Please enter a string key containing only letters."
            return False
        else:
            key = key.lower()  # in case the user input capital letters
            return key

    def encrypt_decrypt(option, key):
        cipher_text = ""
        key_index = 0

        for char in message:
            if char.lower() in char_set:  # alphabet provided is all lower case - used to search for capital letters
                msg_let_index = char_set.find(char.lower())    # ex: '20' for t
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

    if (user_option is not None) and (user_key is not None):
        if check_option(user_option) and check_key(user_key):
            encrypt_decrypt(user_option, user_key)
    else:
        return encrypt_decrypt_prompt()


if __name__ == "__main__":
    if len(argv) == 1:
        text = raw_input("Enter a string to be encrypted/decrypted using the vigenere cipher\n> ")
        vigenere_cipher(text)
    else:  # handle input from command line
        text = ""
        script = argv
        word_num = len(argv)

        # append command line string arguments into a variable
        for k in range(1, word_num):
            if k == (word_num - 1):
                text += argv[k]
            else:
                text += argv[k] + " "

        vigenere_cipher(text)
