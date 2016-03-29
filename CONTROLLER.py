from MODEL import DataProcessing
from VIEW import View

__author__ = 'Dart Vader'


class DataWork:

    def __init__(self):
        self.dp = DataProcessing()
        self.v = View()

    def new_product(self):
        """
        add new product to products list
        :return:
        """
        self.v.message('Input name of product: ')
        name = input().lower()
        if name in list(self.dp.get_list('', {}, 0).keys()):
            self.v.message('Product already exist')
        else:
            self.v.message('Input calories of new product: ')
            calories = input()
            self.dp.create_product(name, {}, int(calories))
            self.v.message('Added.')

    def show_list(self):
        """
        show list of products
        :return:
        """
        self.v.show_products(self.dp.get_list('', {}, 0))

    def calories_amount(self, mass, name):
        """
        Sum of all calories from user list
        :param mass:
        :param name:
        :return:
        """
        user_calories = self.dp.get_user_calories()
        clr = self.dp.get_product(name, {}, 0)
        user_calories += round((int(mass)/100)*clr, 3)
        self.dp.set_user_calories(user_calories)

    def add_to_calc(self):
        """
        add item to user calories list and calculate it
        :return:
        """
        self.v.message('Input name of product')
        name = input().lower()
        if name not in self.dp.get_list('', {}, 0):
            self.v.message('Wrong product name')
        else:
            self.v.message('Input mass of product')
            mass = input()
            self.calories_amount(mass, name)

    def c_of_product(self):
        """
        Calories of products
        :return:
        """
        self.v.message('Input name')
        name = input().lower()
        self.v.show_calories(self.dp.get_product(name, {}, 0))

    def del_product(self):
        """
        delete product from list
        :return:
        """
        self.v.message('Input name of product: ')
        name = input().lower()
        if name not in list(self.dp.get_list('', {}, 0).keys()):
            self.v.message('Product does not exist')
        else:
            self.dp.delete_product(name, {}, 0)
            self.v.message('Deleted.')

    def upd_product(self):
        """
        update product in list
        :return:
        """
        self.v.message('Input name of product: ')
        name = input().lower()
        if name not in list(self.dp.get_list('', {}, 0).keys()):
            self.v.message('Product does not exist')
        else:
            self.v.message('Input new calories of  product: ')
            calories = input()
            self.dp.update_product(name, {}, calories)
            self.v.message('Updated.')

    def main_interface(self):
        """
        Main interface menu
        :return:
        """
        while True:
            self.v.show_menu()
            chosen = input()
            if chosen == '1':
                self.show_list()
            elif chosen == '2':
                self.add_to_calc()
            elif chosen == '3':
                self.v.show_calories(self.dp.get_user_calories())
            elif chosen == '4':
                self.dp.set_user_calories(0)
            elif chosen == '5':
                self.new_product()
            elif chosen == '6':
                self.c_of_product()
            elif chosen == '7':
                self.del_product()
            elif chosen == '8':
                self.upd_product()
            elif chosen == '0':
                break


dw = DataWork()
dw.main_interface()
