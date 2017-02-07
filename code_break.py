#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import itertools
import string
import sys

import affine
import caesar
import transposition
import vigenere

from crypto_funcs import gcd

char_set = string.ascii_lowercase + '  \t\n'


class CodeBreak(object):
    """Base class for code breaking attempts."""

    def __init__(self, cipher_text):
        self.cipher_text = cipher_text
        self.dict_words = {}

        self.EXTRA_CHARS = 3
        self.TRANSPOS_START = 2
        self.VIGENERE_WORD_THRESH = 80

    def code_break(self):
        """Take the instantiated cipher text and attempt all supported decryption attempts sequentially
        until a candidate decryption is detected, or all methods have finished execution with no result.
        """

        self.dictionary_load()

        attacks = {1: [self.caesar_brute, 'Caesar'], 2: [self.transposition_brute, 'Transposition'],
                   3: [self.affine_brute, 'Affine'], 4: [self.vigenere_dict_attack, 'Vigenere']}

        for attempt in attacks:
            decryption_attempt = attacks[attempt][0]()
            if not decryption_attempt:
                print '\n{} decryption failed'.format(attacks[attempt][1])

    def dictionary_load(self):
        """Load a dictionary object with contents of an English dictionary .txt file."""

        dict_file = open('20k.txt')
        for word in dict_file.read().split('\n'):
            self.dict_words[word] = None
        dict_file.close()

    def english_count(self, decrypted_text):
        """Strip symbols from a string returned from a decryption attempt. Compare each word found in the decrypted
        string to words present in an English dictionary.
        """

        symbols_removed_text = decrypted_text.lower()
        symbols_removed_text = remove_symbols(symbols_removed_text)

        potential_words = symbols_removed_text.split()

        if not potential_words:
            return 0

        word_matches = 0
        for word in potential_words:
            if word in self.dict_words:
                word_matches += 1

        percent_identified = float(word_matches) / len(potential_words)

        # Return the percentage of words in decryption that matched English words present in the dictionary.
        return percent_identified

    def text_comparison(self, decrypted_text, word_threshold=65, letter_threshold=80):
        """Determine if the number of english words identified exceeds a certain threshold value to avoid presenting
        the user with an abundance of false-positive results. Also determine if there are too many symbols present
        in the string.
        """

        words_match = self.english_count(decrypted_text) * 100 >= word_threshold
        num_letters = len(remove_symbols(decrypted_text))

        ct_letter_percent = float(num_letters) / len(decrypted_text) * 100
        letters_match = ct_letter_percent >= letter_threshold

        # Return True only if both variables previously evaluated to True.
        return words_match and letters_match

    def caesar_brute(self):
        """Caesar cipher decryption on each possible caesar cipher key."""

        for key in range(len(char_set) - self.EXTRA_CHARS):
            decrypted_text = caesar.encrypt_decrypt(self.cipher_text, 'd', key)
            if self.text_comparison(decrypted_text):
                valid_message = possible_decryption(key, decrypted_text)
                if valid_message:
                    return valid_message

        return False

    def transposition_brute(self):
        """Transposition cipher decryption on each possible transposition cipher key."""

        for key in range(self.TRANSPOS_START, len(self.cipher_text) - 1):
            decrypted_text = transposition.encrypt_decrypt(self.cipher_text, 'd', key)
            if self.text_comparison(decrypted_text, 90):
                valid_message = possible_decryption(key, decrypted_text)
                if valid_message:
                    return valid_message

        return False

    def vigenere_dict_attack(self, perm_attempt=False):
        """Vigenere cipher decryption using all words present in an English dictionary file. If the key isn't found,
         each word in the dictionary may be iterated over again, attempting all case permutations (i.e. upper and lower
         case) for each word.
        """

        def vigenere_dict_check(key):
            """Present the user with a candidate decryption string if enough English words were detected."""

            if self.text_comparison(decrypted_text, self.VIGENERE_WORD_THRESH):
                valid_message = possible_decryption(key, decrypted_text)
                if valid_message:
                    # Since the decryption was successful, break the loop.
                    return valid_message
            else:
                return False

        for word in self.dict_words:
            # By default, the first decryption attempt does not compute case permutations.
            if not perm_attempt:
                decrypted_text = vigenere.encrypt_decrypt(self.cipher_text, 'd', word)
                if vigenere_dict_check(word):
                    break
            else:
                # If no key was found using the original dictionary, attempt case permutations.
                words = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word)))
                for permutation in words:
                    decrypted_text = vigenere.encrypt_decrypt(self.cipher_text, 'd', permutation)
                    if vigenere_dict_check(permutation):
                        break
        else:
            print '\nNo success with standard Vigenere dictionary attack.'
            print 'Would you like to try again using all case permutations of each word in the dictionary? (y/n)'
            print '(Note: This may take a while)\n'

            choice = raw_input('> ')

            if choice.startswith('y'):
                self.vigenere_dict_attack(perm_attempt=True)
            else:
                return False

    def affine_brute(self):
        """Affine cipher decryption using all possible affine cipher keys."""

        for key in range(affine.char_set_len ** 2):
            key_a, key_b = affine.compute_keys(key)
            if gcd(key_a, affine.char_set_len) != 1:
                # If key_a and the char set length aren't relatively prime, try a new key.
                continue

            decrypted_text = affine.encrypt_decrypt(self.cipher_text, 'd', key_a, key_b)
            if self.text_comparison(decrypted_text):
                valid_message = possible_decryption(key, decrypted_text)
                if valid_message:
                    return valid_message

        return False


def possible_decryption(key, decrypted_text):
    """Present candidate decryptions to the user."""

    print
    print 'Possible decryption:'
    print 'Key: ' + str(key) + ' -> ' + decrypted_text[:100]
    print
    print 'If this decryption is correct, type q to quit or press enter to continue decryption'

    choice = raw_input('> ')

    if choice.startswith('q'):
        sys.exit()
    else:
        return False


def remove_symbols(modified_text):
    """Remove non-alphanumeric characters from a string."""

    formatted_text = []
    for char in modified_text:
        if char in char_set:
            formatted_text.append(char)

    return ''.join(formatted_text)
