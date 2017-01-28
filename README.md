# Ciphers
Presented here are a variety of cryptographic ciphers, each with encryption and decryption ability.

Each cipher accepts a string and encrypts/decrypts that string using a user-provided key. With some ciphers, the user may choose to use a randomly generated encryption key (e.g. affine).

Currently implemented ciphers include:
* Caesar cipher
* Transposition cipher
* Affine cipher
* Vigenère cipher

# How to use
Each cipher may be executed without arguments. The user will then be prompted for a message, whether they want the message encrypted or decrypted, and a key.
Alternatively, each cipher may be called by name and optionally accepts 3 arguments (in the following order): `message`, `decrypt/encrypt`, `key` (or key size). Depending on the cipher being used, the key format may be different.

If a cipher option and key are not provided, the user will be prompted for them. Otherwise, the cipher will immediately begin operating.

Examples:

```python
from vigenere import vigenere
vigenere('This is a test message', 'e', 'blastoise')
Usik bg i lite mwlgiyi
```

```bash
./vigenere.py encrypt this message
Encrypt/Decrypt (e/d)?: e
Enter an encryption/decryption key: blastoise
fycjrdb lljd mwlgiyi
```

```bash
python transposition.py
Enter a string to be encrypted/decrypted using the transposition cipher
> cryptography is cool
Encrypt/Decrypt (e/d)?: e
Enter an encryption/decryption key: 6
cg orrilyaspp thcoyo
```

Alternatively, run main.py from a CLI, which allows for sequential encryption and code breaking capability.

# To-do
* Implement the following ciphers:
  * Substitution cipher
* Allow the user to encrypt a string using more than one cipher, applied any number of times (e.g. use the transposition cipher, followed by the affine cipher).
* Built-in brute force decryption options
* Detect english words in brute force decryption efforts and present candidate strings to the user
