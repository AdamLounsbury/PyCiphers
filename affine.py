#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

from crypto_funcs import *


affine_cipher(txt):
    pass



if __name__ == '__main__':
    text = ''
    script = argv
    word_num = len(argv)

    # append command line string arguments into a variable
    for k in range(1, word_num):
        if k == (word_num - 1):
            text += argv[k]
        else:
            text += argv[k] + ' '

    affine_cipher(text)
