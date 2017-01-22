# Ciphers
Presented here are a variety of ciphers, each with encryption and decryption ability. 

Each script can take a string and encrypt/decrypt that string using a user-provided key. With some ciphers, the user may choose to use a randomly generated encryption key (e.g. affine).

Currently implemented ciphers include:
* Caesar cipher
* Transposition cipher
* Affine cipher
* Vigenère cipher

# How to use
Each script may be executed without arguments. The user will then be prompted for a message to be encrypted/decrypted, followed by a key. 
Alternatively, each script's main method may be called, using up to 3 arguments (in the following order): message, encryption option, key (or key size). Depending on the cipher being used, the key may be an integer or a string. 

If neither the encryption option or key is provided, the user will be prompted for them. Otherwise, the cipher will immediately begin operating.

Example:

```python
from vigenere import *
vigenere_cipher('This is a test message', 'e', 'blastoise')
Usik bg i lite mwlgiyi
```

# To-do
* Implement the following ciphers:
  * Substitution cipher
  * RSA cipher
* Allow the user to encrypt a string using more than one cipher, applied any number of times (e.g. use the transposition cipher, followed by the affine cipher).
* Built-in brute force decryption options
* Detect english words in brute force decryption efforts and present candidate strings to the user
