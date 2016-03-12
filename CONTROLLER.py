__author__ = 'Dart Vader'

from MODEL import DataProcessing
from VIEW import View

class DataWork:

    def __init__(self):
        self.dp = DataProcessing()
        self.v = View()

    def mainInterface(self):
        """
        Main interface menu
        :return:
        """
        while True:
            self.v.show_menu()
            chosen = raw_input()
            if chosen == '1':
                self.v.show_products(self.dp.getData())
            elif chosen == '2':
                self.v.inp_choice_msg()
                name = raw_input()
                if name not in self.dp.getData():
                    print 'Wrong product name'
                else:
                    self.v.inp_mass_msg()
                    mass = input()
                    if self.dp.calories_amount(name, mass):
                        self.dp.getUserCalories()
                    else:
                        print 'Error'
            elif chosen == '3':
                print 'Your calories: ', self.dp.getUserCalories()
            elif chosen == '4':
                self.dp.ResetValues()
            elif chosen == '0':
                break




dw = DataWork()
dw.mainInterface()


