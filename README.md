# Ciphers
Presented here are a variety of cryptographic ciphers, each with encryption and decryption ability.

Each cipher accepts a string and encrypts/decrypts that string using a key. The user may choose to use a randomly generated encryption key by inputting 'random' as the key.

Implemented ciphers include:
* Caesar cipher
* Transposition cipher
* Affine cipher
* Vigenère cipher
* Substitution cipher

# How to use

Run `main.py` from a terminal to see a menu of possible operations. Current options include encryption/decryption, brute force decryption, and multiple encryption.

Alternatively, each cipher may be executed independently in the Python shell or from a terminal.

Examples:

```python
from affine import affine
affine('This is a test message', 'e', 1696)
L0ig ig U yBgy ~BggU.B
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


# Acknowledgements

- The dictionary I used was modified from the '20k.txt' file in https://github.com/first20hours/google-10000-english
- Thanks to Neal Stephenson's amazing book "Cryptonomicon" and Al Sweigart for sparking my interest in Cryptography!