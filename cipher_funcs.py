import inspect


class CipherFuncs(object):
    def __init__(self):
        self.option = ""
        self.key = ""

    def encrypt_decrypt_prompt(self):
        self.option = raw_input("Encrypt/Decrypt (e/d)?: ")
        if self.check_option():
            return self.key_get()
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
            print 'Invalid operation detected. Please enter a valid operation (encryption/decryption).'
            return False

    def key_get(self):
        self.key = raw_input("Enter an encryption/decryption key: ")
        self.key = self.check_key()
        if self.key:
            return True

    def check_key(self):
        """Three cases to check for: affine (key specificity), int, and str"""
        # the function name is always in the same spot in the stack
        if inspect.stack()[-2][-3].startswith('v'):  # vigenere case
            try:
                self.key = self.key.replace(" ", "")  # in case the user enters a string key containing spaces
            except AttributeError:
                print "Please enter a string key."
                return False
            else:
                return self.key


        # 3 cases: affine, int, and str

    def rand_key(self):
        pass


if __name__ == "__main__":
    pass
