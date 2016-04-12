import configparser
config = configparser.ConfigParser()
config.read('fileconfig.ini')
if config['DEFAULT']['ModelFile'] == 'pickle':
    from MOD_PICKLE import PickleSerialization
    serialize = PickleSerialization()


elif config['DEFAULT']['ModelFile'] == 'json':
    from MOD_JSON import JsonSerialization
    serialize = JsonSerialization()


if config['DEFAULT']['ModelFile'] == 'yaml':
    from MOD_YAML import YamlSerialization
    serialize = YamlSerialization()


class Products:
    @staticmethod
    @serialize.upd_file
    def get_product(name, data, calories):
        return data[name]

    @staticmethod
    @serialize.upd_file
    def get_list(name, data, calories):
        return data

    @staticmethod
    @serialize.upd_file
    def create_product(product, data, calories):
            data.update({product: calories})

    @staticmethod
    @serialize.upd_file
    def delete_product(product, data, calories):
        data.pop(product)

    @staticmethod
    @serialize.upd_file
    def update_product(product, data, calories):
        data[product] = calories


class User:
    def __init__(self):
        """
        Read dictionary from pickle file
        :return:
        >>> user = User()
        """
        self.user_calories = 0

    def get_user_calories(self):
        """
        :return: User calories
        """
        return self.user_calories

    def set_user_calories(self, new_calories):
        self.user_calories = new_calories
