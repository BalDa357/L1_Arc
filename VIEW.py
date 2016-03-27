__author__ = 'Dart Vader'


class View:
    @staticmethod
    def show_menu():
        """
        show menu
        :return:
        """
        print('1. Show list of products')
        print('2. Add product to calculator ')
        print('3. Show result of calculate')
        print('4. Reset result of calculate')
        print('5. Add new product to products list')
        print('6. Show product calories')
        print('7. Delete product')
        print('8. Update product')
        print('0. Exit')

    @staticmethod
    def show_products(data_list):
        """
        show all products to choice
        :param data_list: List to show
        :return:
        """
        print('Products:')
        for key in data_list:
                print('{} = {}'.format(key, data_list[key]))

    @staticmethod
    def show_calories(calories):
        """
        show user calories
        :param calories: user calories
        :return:
        """
        print(str(calories) + ' calories')

    @staticmethod
    def inp_mass_msg():
        """
        show msg for user "Mass of this product: "
        :return:
        """
        print('Mass of this product: ')

    @staticmethod
    def message(mess):
        print(mess)
