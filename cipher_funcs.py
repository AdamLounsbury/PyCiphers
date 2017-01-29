#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import crypto_funcs
import inspect
import platform
import random
import sys
import string
import win32clipboard


class CipherFuncs(object):

    def __init__(self, text="", option="", key=""):
        self.text = text
        self.option = option
        self.key = key
        self.char_set_len = len(string.printable)

    def get_message(self):
        self.text = raw_input("Enter a string to be encrypted/decrypted: ")
        return self.text

    def encrypt_decrypt_prompt(self):
        self.option = raw_input("Encrypt/Decrypt (e/d)?: ")
        if self.check_option():
            return self.option
        else:
            return self.encrypt_decrypt_prompt()

    def check_option(self):
        if self.option.startswith('E') or self.option.startswith('e'):
            self.option = self.option.lower()
            return self.option
        elif self.option.startswith('D') or self.option.startswith('d'):
            self.option = self.option.lower()
            return self.option
        else:
            print '\nInvalid operation detected. Please enter a valid operation (encryption/decryption).'
            return False

    def key_get(self):
        self.key = raw_input("Enter an encryption/decryption key: ")
        self.key = self.check_key()
        return self.key

    def check_key(self):
        """Three cases to check for: affine (key specificity), int, and str; each time, will look in the call stack
            for the function name and handle key input errors with respect to each cipher's key requirements"""
        frame = str(inspect.stack())

        if 'vigenere' in frame:
            try:
                self.key = self.key.replace(" ", "")  # in case the user enters a string key containing spaces
            except AttributeError:
                print "Please enter a string key."
                return self.key_get()
            else:
                return self.key
        elif 'transposition' in frame:
            try:
                int(self.key)
            except ValueError:
                print "Please enter an integer key (NB: should be less than the string length for best results)"
                return self.key_get()
            else:
                return int(self.key)
        elif 'affine' in frame:
            try:
                key_a, key_b = self.affine_compute_keys()
                if key_a == 1:
                    print "The affine cipher is very weak when key A computes to 1. Choose a different key.\n"
                    self.key_get()
                elif key_b == 0:
                    print "The affine cipher is very weak when key B computes to 0. Choose a different key.\n"
                    self.key_get()
                elif key_a < 0 or self.char_set_len - 1 < key_b < 0:
                    print "Key A must be greater than 0 and Key B must be between 0 and {}. Choose a different key.\n"\
                        .format(self.char_set_len - 1)
                elif crypto_funcs.gcd(key_a, self.char_set_len) != 1:
                    print "Key A ({}) and the symbol set size ({}) are not relatively prime.\n". \
                        format(key_a, self.char_set_len)
                    if self.option == 'e':
                        rand_key = raw_input("Would you like a random key to be generated? (y/n): ")
                        if rand_key.startswith('y'):
                            return self.rand_key()
                        else:
                            return self.key_get()
            except ValueError:
                print "Please enter an integer key > 0"
                return self.key_get()
            else:
                return self.key  # key A and B satisfy strength and validity tests
        elif 'caesar' in frame:
            try:
                assert self.key > 26
            except AssertionError:
                print "Please enter an integer key (NB: should be less than the string length for best results)"
                return self.key_get()
            else:
                return self.key
        elif 'substitution' in frame:
            pass
            # 3 cases: affine, int, and str

    def affine_compute_keys(self):
        key_a = int(self.key) // len(string.printable)
        key_b = int(self.key) % len(string.printable)
        return key_a, key_b

    def rand_key(self):
        frame = str(inspect.stack())
        if 'affine' in frame:
            while True:
                key_a = random.randint(2, self.char_set_len)
                key_b = random.randint(2, self.char_set_len)
                if crypto_funcs.gcd(key_a, self.char_set_len) == 1:
                    print "Key is {0}".format(key_a * self.char_set_len + key_b)
                    return key_a * self.char_set_len + key_b

    def script_call(self):
        x = self.get_message()
        y = self.encrypt_decrypt_prompt()
        z = self.key_get()
        return x, y, z

    def main_call(self):
        x = self.get_message()
        y = self.key_get()
        return x, y

    def cli_call(self):
        x = self.encrypt_decrypt_prompt()
        y = self.key_get()
        return x, y

    def shell_call(self):
        x = self.check_option()
        y = self.check_key()
        if x and y:  # both option and key must have received valid inputs
            return True
        else:
            return False

    def call_source(self):
        if not self.text and not self.option and not self.key:  # if cipher is run as a script with no arguments
            self.text, self.option, self.key = self.script_call()
            return self.text, self.option, self.key
        elif self.option and not self.text and not self.key:  # cipher called from main.py, so enc/dec is specified
            self.text, self.key = self.main_call()
            return self.text, self.option, self.key
        elif self.text and not self.option and not self.key:  # cipher called directly from CLI with an included string
            self.option, self.key = self.cli_call()
            return self.text, self.option, self.key
        else:                                                 # cipher run in the shell with all arguments provided
            valid_choices = self.shell_call()
            if valid_choices:
                return self.text, self.option, self.key
            else:
                print "Try again!\n"
                sys.exit()


def cmd_handles(*args):
    text = ""

    if len(args[0]) > 1:
        word_num = len(args[0])  # everything in argv excluding the file name
        for k in range(1, word_num):
            if k == (word_num - 1):
                text += args[0][k]
            else:
                text += args[0][k] + " "
        return text
    else:
        return False


def clipboard(cipher_text):
    if platform.system() == "Windows":
        store_clip = raw_input("\nStore output in clipboard? (y/n): ")
        if store_clip.startswith('y'):
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(cipher_text)
            win32clipboard.CloseClipboard()
        return True
    else:
        sys.exit()

if __name__ == "__main__":
    pass
