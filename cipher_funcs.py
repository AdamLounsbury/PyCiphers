import inspect


class CipherFuncs(object):
    def __init__(self, text="", option="", key=""):
        self.text = text
        self.option = option
        self.key = key

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
            for the function name and handle key input errors with respect to each cipher's requirements"""

        frame = str(inspect.stack())
        if 'vigenere' or 'caesar' or 'substitution' in frame:
            try:
                self.key = self.key.replace(" ", "")  # in case the user enters a string key containing spaces
            except AttributeError:
                print "Please enter a string key."
                return False
            else:
                return self.key
            # 3 cases: affine, int, and str

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
        if x and y:  # check if the option and key are valid inputs
            return True
        else:
            return False

    def rand_key(self):
        pass


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

if __name__ == "__main__":
    pass
