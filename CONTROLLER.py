from MODEL import DataProcessing
from VIEW import View

__author__ = 'Dart Vader'


class DataWork:

    def __init__(self):
        self.dp = DataProcessing()
        self.v = View()

    def main_interface(self):
        """
        Main interface menu
        :return:
        """
        while True:
            self.v.show_menu()
            chosen = input()
            if chosen == '1':
                self.v.show_products(self.dp.get_data())
            elif chosen == '2':
                self.v.inp_choice_msg()
                name = input()
                if name not in self.dp.get_data():
                    print('Wrong product name')
                else:
                    self.v.inp_mass_msg()
                    mass = input()
                    if self.dp.calories_amount(name, mass):
                        self.dp.get_user_calories()
                    else:
                        print('Error')
            elif chosen == '3':
                print('Your calories: ', self.dp.get_user_calories())
            elif chosen == '4':
                self.dp.reset_values()
            elif chosen == '5':
                self.v.inp_name_msg()
                name = input()
                self.v.inp_calories_msg()
                calories = input()
                self.dp.add_new_product(name,int(calories))

            elif chosen == '0':
                break


dw = DataWork()
dw.main_interface()
