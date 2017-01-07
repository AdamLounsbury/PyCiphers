# Ciphers
Presented here are a variety of ciphers, each with encryption and decryption ability. 

Each script can take a string and encrypt/decrypt that string using a user-provided key. With some ciphers, the user may choose to use a randomly generated encryption key (e.g. affine).

Currently implemented ciphers include:
* Caesar cipher
* Transposition cipher
* Affine cipher

# To-do
* Implement the following ciphers:
  * Vigenère cipher
  * Substitution cipher
  * RSA cipher
* Allow the user to encrypt a string using more than one cipher, applied any number of times (e.g. use the transposition cipher, followed by the affine cipher).
* Built-in brute force decryption options
* Detect english words in brute force decryption efforts and present candidate strings to the user
