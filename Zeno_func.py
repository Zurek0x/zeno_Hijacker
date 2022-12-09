
import pyperclip

class data_handle():
    def read():
        value = pyperclip.paste()
        return value
    def write(self):
        pyperclip.copy(f'{self}')