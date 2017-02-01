#!/usr/bin/env python
# ACL 2016 - alounsbu@alumni.uwo.ca

import vigenere
import string

char_set = string.ascii_lowercase + "  \t\n"


class CodeBreak(object):
    def __init__(self, cipher_text):
        self.cipher_text = cipher_text
        self.dict_words = {}

    def main(self):
        plain_text = self.vigenere_dict_attack()

        if plain_text is not None:
            print plain_text
        else:
            print "Failed to code break using Vigenere code breaking"

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

    def text_comparison(self, decrypted_text, word_threshold=60, letter_threshold=80):
        # see if more than 20% of the words are in the dictionary AND if
        words_match = self.english_count(decrypted_text) * 100 >= word_threshold
        num_letters = len(remove_symbols(decrypted_text))

        ct_letter_percent = float(num_letters) / len(decrypted_text) * 100
        letters_match = ct_letter_percent >= letter_threshold

        return words_match and letters_match  # return True only if both variables previously evaluated to True

    def caesar_brute(self):
        pass

    def transposition_brute(self):
        pass

    def vigenere_dict_attack(self):
        self.dictionary_load()

        for word in self.dict_words:
            decrypted_text = vigenere.encrypt_decrypt(self.cipher_text, 'd', word)
            if self.text_comparison(decrypted_text):
                print
                print "Possible decryption:"
                print "Key: " + str(word) + " -> " + decrypted_text[:100]  # show only the first 100 chars for brevity
                print
                print "If this decryption is correct, type q to quit or press enter to continue decryption"

                choice = raw_input("> ")

                if choice.startswith('q'):
                    return decrypted_text

    def vigenere_kasiski_exam(self):
        pass


def remove_symbols(modified_text):
    formatted_text = []
    for char in modified_text:
        if char in char_set:
            formatted_text.append(char)

    return ''.join(formatted_text)


if __name__ == "__main__":
    pass
