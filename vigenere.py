
from sys import argv

char_set = "abcdefghijklmnopqrstuvwxyz"


def vigenere_cipher(message, user_option=None, user_key=None):

    def encrypt_decrypt_prompt():
        while True:
            option = raw_input("Encrypt/Decrypt (e/d)?: ")
            if option == 'd' or option == 'e':
                return key_get(option)
            else:
                print "Please choose a valid option for decryption/encryption.\n"

    def key_get(option):
        while True:
            key = raw_input("Enter an encryption/decryption key: ")
            key = key.replace(" ", "")  # in case the user enters a key containing spaces
            key = key.lower()  # in case the user input capital letters
            if key.isalpha():
                return encrypt_decrypt(option, key)
            else:
                print "Please enter a key containing only letters.\n"

    def encrypt_decrypt(option, key):
        cipher_text = ""
        key_index = 0

        for char in message:
            if char.lower() in char_set:  # alphabet provided is all lower case - used to search for capital letters
                msg_let_index = char_set.find(char.lower())    # ex: '20' for t
                key_let_index = char_set.find(key[key_index])  # ex: '2' for b

                if option == 'e':
                    encode_text = (msg_let_index + key_let_index) % len(char_set)
                elif option == 'd':
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
        return encrypt_decrypt(user_option, user_key)
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
