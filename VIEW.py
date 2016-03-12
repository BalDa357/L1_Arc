__author__ = 'Dart Vader'

from CONTROLLER import DataWork

class View:
    def __init__(self):
        self.dw = DataWork()
    def products(self):
        for i in self.dw.dr.data_new:
                print i

    def choice(self, name, mass):
        if self.dw.dr.calories_amount(name, mass):
                self.dw.dr.user_calories


    def mainInterface(self, chosen):
        if chosen == '1':
            self.products()
        if chosen == '2':
            print 'Input your choice: '
            choicen = raw_input()
            print 'Mass of this product: '
            mass = raw_input()
            self.choice(choicen)
        if chosen == '3':
            print 'Your calories: ', self.dw.dr.user_calories
