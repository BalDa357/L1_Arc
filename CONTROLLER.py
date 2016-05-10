import configparser
import sys
import argparse

from MODEL import User, Products
from VIEW import View

config = configparser.ConfigParser()
config.read('fileconfig.ini')


class DataWork:
    def __init__(self):
        self.products = Products()
        self.user = User()
        self.display = View()

    def new_product(self):
        """
        add new product to products list
        :return:
        """
        self.display.message('Input name of product: ')
        name = input().lower()
        if name in list(self.products.get_list().keys()):
            self.display.message('Product already exist')
        else:
            self.display.message('Input calories of new product: ')
            calories = input()
            self.products.create_product(name,  int(calories))
            self.display.message('Added.')

    def show_list(self):
        """
        show list of products
        :return:
        """
        if self.products.get_list != {}:
            self.display.show_products(self.products.get_list())
        else:
            self.display.message("List empty")

    def calories_amount(self, mass, name):
        """
        Sum of all calories from user list
        :param mass:
        :param name:
        :return:
        """
        user_calories = self.user.get_user_calories()
        clr = self.products.get_product(name)
        user_calories += round((int(mass) / 100) * clr, 3)
        self.user.set_user_calories(user_calories)

    def add_to_calc(self):
        """
        add item to user calories list and calculate it
        :return:
        """
        self.display.message('Input name of product')
        name = input().lower()
        if name not in self.products.get_list():
            self.display.message('Wrong product name')
        else:
            self.display.message('Input mass of product')
            mass = input()
            self.calories_amount(mass, name)

    def c_of_product(self):
        """
        Calories of products
        :return:
        """
        self.display.message('Input name')
        name = input().lower()
        if name not in list(self.products.get_list().keys()):
            self.display.message('Product does not exist')
        else:
            self.display.show_calories(self.products.get_product(name))

    def del_product(self):
        """
        delete product from list
        :return:
        """
        self.display.message('Input name of product: ')
        name = input().lower()
        if name not in list(self.products.get_list().keys()):
            self.display.message('Product does not exist')
        else:
            self.products.delete_product(name)
            self.display.message('Deleted.')

    def upd_product(self):
        """
        update product in list
        :return:
        """
        self.display.message('Input name of product: ')
        name = input().lower()
        if name not in list(self.products.get_list().keys()):
            self.display.message('Product does not exist')
        else:
            self.display.message('Input new calories of  product: ')
            calories = input()
            self.products.update_product(name, calories)
            self.display.message('Updated.')

    def main_interface(self):
        """
        Main interface menu
        :return:
        """
        while True:
            self.display.show_menu()
            chosen = input()
            if chosen == '1':
                self.show_list()
            elif chosen == '2':
                self.add_to_calc()
            elif chosen == '3':
                self.display.show_calories(self.user.get_user_calories())
            elif chosen == '4':
                self.user.set_user_calories(0)
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


if __name__ == "__main__":
    data_work = DataWork()
    data_work.main_interface()
