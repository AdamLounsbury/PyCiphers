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

    def encrypt_decrypt():
        option = raw_input("Encrypt/Decrypt (e/d)?: ")
        while True:
            key = raw_input("Enter an encryption/decryption key (0-25), or type \'all\': ")
            if not key.isdigit():
                if key == 'all':
                    operation_option(option, key)
                    break
                else:
                    print "Please enter an integer value for the key between 0 and 25, or type \'all\'"
            elif -1 < int(key) < 26:
                key = int(key)
                operation_option(option, key)
                break
            else:
                print "Please enter an integer value for the key between 0 and 25, or type \'all\'"

    def find_index(curr_char, index_key, enc_dec):
        
        def encode(enc_char, enc_key):
            if curr_char.islower():
                let_index = alphabet_lower.index(enc_char)
            else:
                let_index = alphabet_upper.index(enc_char)

            if let_index + enc_key < len(alphabet_lower):
                encode_index = let_index + enc_key
            else:
                encode_index = (let_index + enc_key) % len(alphabet_lower)

            return encode_index

        def decode(dec_char, dec_key):
            if curr_char.islower():
                let_index = alphabet_lower.index(dec_char)
            else:
                let_index = alphabet_upper.index(dec_char)

            if let_index + dec_key < len(alphabet_lower):
                decode_index = let_index - dec_key
            else:
                decode_index = (let_index - dec_key) % len(alphabet_lower)

            return decode_index

        if enc_dec == 'e' or enc_dec == 'E':
            return encode(curr_char, index_key)
        else:
            return decode(curr_char, index_key)

    def caesar_message(ed, key_in):
        transformed_message = ''
        for char in message:
            if char in alphabet_lower:
                transformed_message += alphabet_lower[find_index(char, key_in, ed)]
            elif char in alphabet_upper:
                transformed_message += alphabet_upper[find_index(char, key_in, ed)]
            else:
                transformed_message += char

        return transformed_message

    def operation_option(option, key):
        if key == 'all':
            for j in range(len(alphabet_lower)):
                print j, ': ' + caesar_message(option, j)
        elif key == int(key):
            print caesar_message(option, key)

    encrypt_decrypt()
    
if __name__ == '__main__':
    caesar_cipher(text)
