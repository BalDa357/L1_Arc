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
        if name in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product already exist')
        else:
            self.display.message('Input calories of new product: ')
            calories = input()
            self.products.create_product(name, {}, int(calories))
            self.display.message('Added.')

    def show_list(self):
        """
        show list of products
        :return:
        """
        if self.products.get_list != {}:
            self.display.show_products(self.products.get_list('', {}, 0))
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
        clr = self.products.get_product(name, {}, 0)
        user_calories += round((int(mass) / 100) * clr, 3)
        self.user.set_user_calories(user_calories)

    def add_to_calc(self):
        """
        add item to user calories list and calculate it
        :return:
        """
        self.display.message('Input name of product')
        name = input().lower()
        if name not in self.products.get_list('', {}, 0):
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
        if name not in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product does not exist')
        else:
            self.display.show_calories(self.products.get_product(name, {}, 0))

    def del_product(self):
        """
        delete product from list
        :return:
        """
        self.display.message('Input name of product: ')
        name = input().lower()
        if name not in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product does not exist')
        else:
            self.products.delete_product(name, {}, 0)
            self.display.message('Deleted.')

    def upd_product(self):
        """
        update product in list
        :return:
        """
        self.display.message('Input name of product: ')
        name = input().lower()
        if name not in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product does not exist')
        else:
            self.display.message('Input new calories of  product: ')
            calories = input()
            self.products.update_product(name, {}, calories)
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


class Console(DataWork):
    def __init__(self):
        self.products = Products()
        self.user = User()
        self.display = View()
        parser = self.create_parser()
        namespace = parser.parse_args(sys.argv[1:])
        self.parser_analyze(namespace,sys.argv[1:])

    def create_parser(self):
        """
        Creating parser
        :return:
        """
        parser = argparse.ArgumentParser(
            prog = 'lab3',
            description = '''Lab 3 Calories Calculator''',
            epilog = '''(c) Bala D., Viflinzider V., Kletsov S. 2016 KPI'''
        )

        parser.add_argument('-a','--add', nargs='+', help = 'Adding new product in format "Name" "Calories"')
        parser.add_argument('-d','--delete', help = 'Deleting product "Name"')
        parser.add_argument('-s','--show',action='store_const', const=True, default=False, help = 'Showing all products')
        parser.add_argument('-u','--update',nargs='+',help = 'Updating product "Name" with new "Calories"')
        parser.add_argument('-c','--calories',help = 'Showing products "Name" calories')
        parser.add_argument('-r','--result',nargs="+",help='Calculation yours calories in format "Name" "Mass" ...')

        return parser

    def parser_analyze(self, namespace,params):
        """
        Analyzing keys
        :param namespace:
        :param params:
        :return:
        """
        if '-s' in params or '--show' in params:
            DataWork.show_list(self)
        if '-a' in params or '--add' in params:
            self.new_product(namespace)
        if '-d' in params or '--delete' in params:
            self.del_product(namespace)
        if '-u' in params or '--update' in params:
            self.upd_product(namespace)
        if '-c' in params or '--calories' in params:
            self.c_of_product(namespace)
        if '-r' in params or '--result' in params:
            self.calculate(namespace)


    def new_product(self, namespace):
        """
        Adding new product to file
        :param namespace:
        :return:
        """
        if len(namespace.add) < 2:
            self.display.message('Wrong number of arguments')
            return
        self.products.create_product(namespace.add[0].lower(),{},int(namespace.add[1]))

    def del_product(self, namespace):
        """
        Deleting product from file
        :param namespace:
        :return:
        """
        name = namespace.delete.lower()
        if name not in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product does not exist')
        else:
            self.products.delete_product(name, {}, 0)
            self.display.message('Deleted.')

    def upd_product(self, namespace):
        """
        Updating product in file
        :param namespace:
        :return:
        """
        if len(namespace.update) < 2:
            self.display.message('Wrong number of arguments')
            return
        name = namespace.update[0].lower()
        calories = int(namespace.update[1])
        if name not in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product does not exist')
        else:
            self.products.update_product(name, {}, calories)
            self.display.message('Updated.')

    def c_of_product(self,namespace):
        """
        Showing products calories
        :param namespace:
        :return:
        """
        name = namespace.calories.lower()
        if name not in list(self.products.get_list('', {}, 0).keys()):
            self.display.message('Product does not exist')
        else:
            self.display.show_calories(self.products.get_product(name, {}, 0))

    def calculate(self,namespace):
        """
        Calculating total calories
        :param namespace:
        :return:
        """
        for i in range(0,len(namespace.result),2):
            name = namespace.result[i]
            if name not in self.products.get_list('', {}, 0):
                self.display.message('Wrong product name')
                return
            try:
                mass = int(namespace.result[i+1])
            except:
                print('Wrong mass')
                return
            DataWork.calories_amount(self,mass,name)
        print(self.user.get_user_calories())



if __name__ == "__main__":
    if config['DEFAULT']['ControllerType'] == 'default':
        data_work = DataWork()
        data_work.main_interface()
    elif config['DEFAULT']['ControllerType'] == 'console':
        console_work = Console()
    else:
        print('Wrong controller type')

