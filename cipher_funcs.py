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

    def rand_key(self):
        pass

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
        if x and y:  # both option and key must have received valid inputs
            return True
        else:
            return False

    def call_source(self):
        if not self.text and not self.option and not self.key:  # if cipher is run as a script with no arguments
            self.text, self.option, self.key = self.script_call()
            return self.text, self.option, self.key
        elif self.option and not self.text and not self.key:  # cipher called from main.py, so enc/dec is specified
            self.text, self.key = self.main_call()
            return self.text, self.option, self.key
        elif self.text and not self.option and not self.key:  # cipher called directly from CLI with an included string
            self.option, self.key = self.cli_call()
            return self.text, self.option, self.key
        else:                                                 # cipher run in the shell with all arguments provided
            valid_choices = self.shell_call()
            if valid_choices:
                return self.text, self.option, self.key
            else:
                print "Try again!\n"


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
