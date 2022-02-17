import itertools as  it 
import string
from util import timefunc

class Brutarce:
    def __init__(self, charset, length=None):
        self.charset = charset
        self.length = length

    def crackit(self, password):
        pass 

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)

@timefunc
def main():
    charset = string.ascii_letters + string.digits 
    brute = Brutarce(charset, 4)
    for guess in brute.guesses:
        print(guess)

if __name__ == '__main__':
    main()