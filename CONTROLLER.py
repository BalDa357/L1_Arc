__author__ = 'Dart Vader'

from MODEL import DataRead

class DataWork:
    def __init__(self):
        self.dr = DataRead()

    def choice(self):
        ch = raw_input()
        if ch == '1':
            return self.dr.getData()


