__author__ = 'Dart Vader'

class View:
    def show_menu(self):
        """
        show menu
        :return:
        """
        print '1. Show list of products'
        print '2. Add product to list'
        print '3. Show result of calculate'
        print '4. Reset result of calculate'
        print '0. Exit'

    def show_products(self, data_list):
        """
        show all products to choice
        :param data_list: List to show
        :return:
        """
        for i in data_list:
                print i

    def show_calories(self, calories):
        """
        show user calories
        :param calories: user calories
        :return:
        """
        print calories

    def inp_choice_msg(self):
        """
        show msg for user "Input your choice: "
        :return:
        """
        print 'Input name of product: '

    def inp_mass_msg(self):
        """
        show msg for user "Mass of this product: "
        :return:
        """
        print 'Mass of this product: '



