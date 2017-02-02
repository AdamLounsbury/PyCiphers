#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import caesar
import transposition
import vigenere
import string
import sys

char_set = string.ascii_lowercase + "  \t\n"

EXTRA_CHARS = 3
TRANSPOS_START = 2


class CodeBreak(object):
    def __init__(self, cipher_text):
        self.cipher_text = cipher_text
        self.dict_words = {}

    def code_break(self):
        self.dictionary_load()

        attacks = {1: [self.caesar_brute, "Caesar"], 2: [self.transposition_brute, "Transposition"],
                   3: [self.vigenere_dict_attack, "Vigenere"]}

        for attempt in attacks:
            decryption_attempt = attacks[attempt][0]()
            if not decryption_attempt:
                print '\n{} decryption failed'.format(attacks[attempt][1])

    def dictionary_load(self):
        dict_file = open('20k.txt')
        for word in dict_file.read().split('\n'):
            self.dict_words[word] = None
        dict_file.close()

    def english_count(self, decrypted_text):

        symbols_removed_text = decrypted_text.lower()
        symbols_removed_text = remove_symbols(symbols_removed_text)

        potential_words = symbols_removed_text.split()

        if not potential_words:
            return 0  # no words detected

        word_matches = 0
        for word in potential_words:
            if word in self.dict_words:
                word_matches += 1

        percent_identified = float(word_matches) / len(potential_words)
        return percent_identified  # % of words in the attempted string decryption that were found in the dictionary

    def text_comparison(self, decrypted_text, word_threshold=65, letter_threshold=80):
        words_match = self.english_count(decrypted_text) * 100 >= word_threshold
        num_letters = len(remove_symbols(decrypted_text))

        ct_letter_percent = float(num_letters) / len(decrypted_text) * 100
        letters_match = ct_letter_percent >= letter_threshold

        return words_match and letters_match  # return True only if both variables previously evaluated to True

    def caesar_brute(self):
        for key in range(len(char_set) - EXTRA_CHARS):
            decrypted_text = caesar.encrypt_decrypt(self.cipher_text, 'd', key)
            if self.text_comparison(decrypted_text):
                valid_message = possible_decryption(key, decrypted_text)
                if valid_message:
                    return valid_message

        return False

    def transposition_brute(self):
        for key in range(TRANSPOS_START, len(self.cipher_text) - 1):
            decrypted_text = transposition.encrypt_decrypt(self.cipher_text, 'd', key)
            if self.text_comparison(decrypted_text, 90):  # set a higher threshold for transposition cipher
                valid_message = possible_decryption(key, decrypted_text)
                if valid_message:
                    return valid_message

        return False

    def vigenere_dict_attack(self):
        for word in self.dict_words:
            word_cases = [x for x in all_cases(word)]
            for permutation in word_cases:
                decrypted_text = vigenere.encrypt_decrypt(self.cipher_text, 'd', permutation)
                if self.text_comparison(decrypted_text):
                    valid_message = possible_decryption(permutation, decrypted_text)
                    if valid_message:
                        return valid_message  # decryption successful; break the loop

        return False

    def vigenere_kasiski_exam(self):
        pass


def all_cases(key):
    if not key:
        yield ""
    else:
        first = key[:1]
        if first.lower() == first.upper():
            for sub_casing in all_cases(key[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_cases(key[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing


def possible_decryption(key, decrypted_text):
    print
    print "Possible decryption:"
    print "Key: " + str(key) + " -> " + decrypted_text[:100]  # show only the first 100 chars for brevity
    print
    print "If this decryption is correct, type q to quit or press enter to continue decryption"

    choice = raw_input("> ")

    if choice.startswith('q'):  # user indicates decryption attempt was successful
        sys.exit()
    else:
        return False


def remove_symbols(modified_text):
    formatted_text = []
    for char in modified_text:
        if char in char_set:
            formatted_text.append(char)

    return ''.join(formatted_text)
