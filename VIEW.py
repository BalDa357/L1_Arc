__author__ = 'Dart Vader'


class View:
    @staticmethod
    def show_menu():
        """
        show menu
        :return:
        """
        print('1. Show list of products')
        print('2. Add product to list')
        print('3. Show result of calculate')
        print('4. Reset result of calculate')
        print('0. Exit')

    @staticmethod
    def show_products(data_list):
        """
        show all products to choice
        :param data_list: List to show
        :return:
        """
        for i in data_list:
                print(i)

    @staticmethod
    def show_calories(calories):
        """
        show user calories
        :param calories: user calories
        :return:
        """
        print(calories)

    @staticmethod
    def inp_choice_msg():
        """
        show msg for user "Input your choice: "
        :return:
        """
        print('Input name of product: ')

    @staticmethod
    def inp_mass_msg():
        """
        show msg for user "Mass of this product: "
        :return:
        """
        print('Mass of this product: ')



