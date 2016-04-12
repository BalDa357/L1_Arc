class View:
    @staticmethod
    def show_menu():
        """
        show menu
        :return:
        """
        print('\n________________________\n1. Show list of products')
        print('\n________________________\n2. Add product to calculator ')
        print('3. Show result of calculate')
        print('4. Reset result of calculate')
        print('\n________________________\n5 .Add new product to products list')
        print('6. Show product calories')
        print('7. Delete product')
        print('8. Update product')
        print('0. EXIT\n________________________\n')

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
    def message(mess):
        """
            show message for user
            :return:
        """
        print(mess)
