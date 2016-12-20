from math import ceil
from sys import argv


def transpositional_cipher(txt=''):
    while True:
        try:
            transpos_key = int(raw_input('Enter an encryption/decryption key: '))  # indicates 'row' size
            if int(transpos_key):
                break
        except ValueError:
            print "Please enter an integer value for the encryption key."

    newstr = [''] * transpos_key

    strlen = len(txt)

    col_size = int(
        ceil(float(strlen) / transpos_key))  # determines number of characters that will be in each text 'box'

    for i in range(transpos_key):
        col_loc = 0  # current location in a column
        for j in range(col_size):
            if (i + col_loc) < strlen:
                newstr[i] += txt[i + col_loc]
                col_loc += transpos_key

    print ''.join(newstr)


if __name__ == '__main__':
    text = ''
    script = argv
    word_num = len(argv)

    # append command line string arguments into a variable
    for i in range(1, word_num):
        text += argv[i] + ' '

    transpositional_cipher(text)
