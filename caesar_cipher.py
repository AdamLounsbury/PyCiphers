#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

from sys import argv

text = ''
script = argv
word_num = len(argv)

# append command line string arguments into a variable
for i in range(1, word_num):
    text += argv[i] + ' '


def caesar_cipher(message):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()

    while True:
        key = raw_input("Enter an encryption/decryption key (0-25) or 'all': ")
        if not key.isdigit():
            if key == 'all':
                break
            else:
                print "Please enter a integer value for the key between 0 and 25"
        elif -1 < int(key) < 26:
            key = int(key)
            break
        else:
            print "Please enter a integer value for the key between 0 and 25"

    def find_index(letter, key_in):
        if letter.islower():
            let_index = alphabet_lower.index(letter)
        else:
            let_index = alphabet_upper.index(letter)

        if let_index + key_in < 26:
            encode_index = let_index + key_in
        else:
            encode_index = (let_index + key_in) % 26

        return encode_index

    def encode_message(key_in):
        encoded_message = ''
        for char in message:
            if char in alphabet_lower:
                encoded_message += alphabet_lower[find_index(char, key_in)]
            elif char in alphabet_upper:
                encoded_message += alphabet_upper[find_index(char, key_in)]
            else:
                encoded_message += char

        return encoded_message

    if key == 'all':
        for i in range(len(alphabet_lower)):
            print i, ': ' + encode_message(i)
    elif key == int(key):
        print encode_message(key)


if __name__ == '__main__':
    caesar_cipher(text)
