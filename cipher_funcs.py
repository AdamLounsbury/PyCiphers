#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import inspect
import platform
import random
import string
import sys
import win32clipboard

import crypto_funcs

CAESAR_MAX_KEY_SIZE = 25


class CipherFuncs(object):
    """Base class for cipher-related functions, including shell/terminal handling and clipboard functionality."""

    def __init__(self, text='', option='', key=''):
        self.text = text
        self.option = option
        self.key = key
        self.char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~'
        self.char_set_len = len(self.char_set)

    def get_message(self):
        """Get text that is to be processed via encryption/decryption."""

        self.text = raw_input('Enter a string to be encrypted/decrypted: ')
        return self.text

    def encrypt_decrypt_prompt(self):
        """Encryption/decryption prompt that also determines if the consequent input is valid."""

        self.option = raw_input('Encrypt/Decrypt (e/d)?: ')
        if self.check_option():
            return self.option
        else:
            return self.encrypt_decrypt_prompt()

    def check_option(self):
        """Determine if the option the user input for encryption/decryption is valid."""

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
        """Prompt the user to input an encryption/decryption key and check that key (based on the cipher used)."""

        self.key = raw_input('Enter an encryption/decryption key: ')
        self.key = self.check_key()
        return self.key

    def check_key(self):
        """Check the key in three cases: affine (for key specificity), int, and str; each time, the call stack is
        inspected for the function name. Key input errors are handled with respect to each cipher's key requirements
        """

        frame = str(inspect.stack())

        if self.key == 'random':
            return self.rand_key()

        elif 'vigenere' in frame:
            try:
                self.key = self.key.replace(' ', "")
            except AttributeError:
                print 'Please enter a string key.'
                return self.key_get()
            else:
                return self.key

        elif 'transposition' in frame:
            try:
                assert int(self.key)
                assert self.key != 0
            except AssertionError:
                print 'Please enter an integer key (NB: should be less than the string length for best results)'
                return self.key_get()
            else:
                return int(self.key)

        elif 'affine' in frame:
            import affine
            try:
                key_a, key_b = affine.compute_keys(self.key)
                if key_a == 1:
                    print 'The affine cipher is very weak when key A computes to 1. Choose a different key.\n'
                    return self.key_get()
                elif key_b == 0:
                    print 'The affine cipher is very weak when key B computes to 0. Choose a different key.\n'
                    return self.key_get()
                elif key_a < 0 or self.char_set_len - 1 < key_b < 0:
                    print 'Key A must be greater than 0 and Key B must be between 0 and {}. Choose a different ' \
                          'key.\n'.format(self.char_set_len - 1)
                    return self.key_get()
                elif crypto_funcs.gcd(key_a, self.char_set_len) != 1:
                    print 'Key A ({}) and the symbol set size ({}) are not relatively prime.\n'. \
                        format(key_a, self.char_set_len)
                    if self.option == 'e':
                        rand_key = raw_input('Would you like a random key to be generated? (y/n): ')
                        if rand_key.startswith('y'):
                            return self.rand_key()
                        else:
                            return self.key_get()
            except ValueError:
                print 'Please enter an integer key > 0'
                return self.key_get()
            else:
                # Key A and B satisfy strength and validity tests.
                return self.key

        elif 'caesar' in frame:
            try:
                assert int(self.key) < 26
            except AssertionError:
                print 'Please enter an integer key (NB: should be less than the string length for best results)'
                return self.key_get()
            else:
                return int(self.key)

        elif 'substitution' in frame:
            self.key = self.key.lower()
            try:
                assert len(self.key) == 26

                # Determine if the key's contents are the same as the char set, followed by if the order is the same.
                assert sorted(self.key) == list(string.ascii_lowercase)
                assert self.key != list(string.ascii_lowercase)
            except AssertionError:
                print 'Key requires all 26 letters of the alphabet in a non-alphabetical order'
                if self.option == 'e':
                    rand_key = raw_input('Would you like a random key to be generated? (y/n): ')
                    if rand_key.startswith('y'):
                        return self.rand_key()
                    else:
                        return self.key_get()
            else:
                return self.key

    def rand_key(self):
        """Generate a random key depending on which cipher is in the call stack."""

        frame = str(inspect.stack())

        if 'affine' in frame:
            while True:
                key_a = random.randint(2, self.char_set_len)
                key_b = random.randint(2, self.char_set_len)
                if crypto_funcs.gcd(key_a, self.char_set_len) == 1:
                    self.key = key_a * self.char_set_len + key_b
                    print 'Affine key is {}'.format(self.key)
                    return self.key

        elif 'substitution' in frame:
            self.key = list(string.ascii_lowercase)
            random.shuffle(self.key)
            print 'Substitution key is {}'.format(''.join(self.key))
            return ''.join(self.key)

        elif 'vigenere' in frame:
            self.key = ""
            for i in range(len(self.text)/2):
                self.key += string.ascii_lowercase[random.randint(0, 25)]

            print 'Vigenere key is {}'.format(self.key)
            return self.key

        elif 'transposition' in frame:
            # use 1/4 and 1/2 as divisors to create a reasonable spread of potential keys
            r1 = len(self.text) / 4
            r2 = len(self.text) / 2
            self.key = random.randint(r1, r2)

            print 'Transposition key is {}'.format(self.key)
            return self.key

        elif 'caesar' in frame:
            self.key = random.randint(0, CAESAR_MAX_KEY_SIZE)
            print 'Caesar key is {}'.format(self.key)
            return self.key

    def script_call(self):
        """If a cipher is executed as a script with no arguments, prompt the user for everything."""

        x = self.get_message()
        y = self.encrypt_decrypt_prompt()
        z = self.key_get()
        return x, y, z

    def main_call(self):
        """If a cipher is executed from main.py, encryption/decryption is specified and only the string and key are
        required from the user.
        """

        x = self.get_message()
        y = self.key_get()
        return x, y

    def cli_call(self):
        """If a cipher is executed from a terminal with an included string, encryption/decryption option and a key
        are required from the user.
        """

        x = self.encrypt_decrypt_prompt()
        y = self.key_get()
        return x, y

    def shell_call(self):
        """If a cipher is executed within the Python shell with all arguments provided, the option and key need only
        be checked for validity.
        """

        x = self.check_option()
        y = self.check_key()
        if x and y:  # both option and key must have received valid inputs
            return True
        else:
            return False

    def call_source(self):
        """Determine how a cipher is being executed and modify the required user inputs appropriately."""

        # If a cipher is run as a script with no arguments...
        if not self.text and not self.option and not self.key:
            self.text, self.option, self.key = self.script_call()
            return self.text, self.option, self.key

        # If a cipher is called from main.py, so enc/dec is specified...
        elif self.option and not self.text and not self.key:
            self.text, self.key = self.main_call()
            return self.text, self.option, self.key

        # If a cipher is called directly from a terminal with an included string...
        elif self.text and not self.option and not self.key:
            self.option, self.key = self.cli_call()
            return self.text, self.option, self.key

        # Otherwise, the cipher has been called in the shell with all arguments provided.
        else:
            valid_choices = self.shell_call()
            if valid_choices:
                return self.text, self.option, self.key
            else:
                print 'Try again!\n'
                sys.exit()


def cmd_handles(*args):
    """Get the string from the user in the appropriate way if a cipher has been executed
     from either the Python shell or a terminal.
     """

    text = ""

    if len(args[0]) > 1:
        word_num = len(args[0])  # everything in argv excluding the file name
        for k in range(1, word_num):
            if k == (word_num - 1):
                text += args[0][k]
            else:
                text += args[0][k] + ' '
        return text
    else:
        return False


def clipboard(cipher_text):
    """Give the user the option of automatically copying an encrypted/decrypted string to the Windows clipboard
    if Windows is the OS running on the user's computer.
    """

    frame = str(inspect.stack())

    if platform.system() == 'Windows':
        if 'multiple_encryption' not in frame:
            print cipher_text
            store_clip = raw_input('\nStore output in clipboard? (y/n): ')
            if store_clip.startswith('y'):
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(cipher_text)
                win32clipboard.CloseClipboard()
        else:
            return cipher_text
