import json


class JsonSerialization:
    @staticmethod
    def upd_file(func):
        """
        decorator for reading from .json file
        :param func:
        :return:
        """

        def wrapper(product, data, calories):
            with open('data.json', 'r') as f:
                data = json.load(f)
            calories = func(product, data, calories)
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return calories
        return wrapper
