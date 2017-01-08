
from sys import argv

char_set_lower = "abcdefghijklmnopqrstuvwxyz"
char_set_upper = char_set_lower.upper()

key = 'butcheroomba'


def vigenere_cipher(message, user_option=None, user_key=None):

    cipher_text = ""
    key_index = 0

    for char in message:
        if char in char_set_lower:
            key_let_index = char_set_lower.find(key[key_index])  # example: '2' for b
            msg_let_index = char_set_lower.find(char)  # example: '20' for t
            encode_text = (msg_let_index + key_let_index) % len(char_set_lower)

            cipher_text += char_set_lower[encode_text]
            key_index += 1

            if key_index == len(key):
                key_index = 0

        else:
            cipher_text += char

    print cipher_text


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
