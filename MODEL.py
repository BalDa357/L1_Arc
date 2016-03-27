import configparser
config = configparser.ConfigParser()
config.read('fileconfig.ini')
if config['DEFAULT']['ModelFile'] == 'pickle':
    from MOD_PICKLE import upd_file
if config['DEFAULT']['ModelFile'] == 'json':
    from MOD_JSON import upd_file
if config['DEFAULT']['ModelFile'] == 'yaml':
    from MOD_YAML import upd_file


class DataProcessing:
    user_calories = 0

    def __init__(self):
        """
        Read dictionary from pickle file
        :return:
        >>> dp = DataProcessing()
        """
        self.user_calories = 0

    @staticmethod
    @upd_file
    def get_product(name, data, calories):
        """
        get calorie of product from list
        :param name:
        :param data:
        :param calories:
        :return: calories
        """
        return data[name]

    @staticmethod
    @upd_file
    def get_list(name, data, calories):
        """
        get product from list
        :param name:
        :param data:
        :param calories:
        :return:
        """
        return data

    @staticmethod
    @upd_file
    def create_product(product, data, calories):
        """
        add product to list
        :param product:
        :param data:
        :param calories:
        :return:
        """
        data.update({product: calories})

    @staticmethod
    @upd_file
    def delete_product(product, data, calories):
        """
        delete product from list
        :param product:
        :param data:
        :param calories:
        :return:
        """
        data.pop(product)

    @staticmethod
    @upd_file
    def update_product(product, data, calories):
        """
        upadte some product
        :param product:
        :param data:
        :param calories:
        :return:
        """
        data[product] = calories

    def get_user_calories(self):
        """
        :return: User calories
        """
        return self.user_calories

    def set_user_calories(self, new_calories):
        """
        Set user calories
        :param new_calories:
        :return:
        """
        self.user_calories = new_calories
