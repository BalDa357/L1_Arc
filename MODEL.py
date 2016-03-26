import pickle


def upd_file(func):
        def wrapper(product, data, calories):
            with open('data.pickle', 'rb') as f:
                data = pickle.load(f)
            calories = func(product, data, calories)
            with open('data.pickle', 'wb') as f:
                pickle.dump(data, f)
            return calories
        return wrapper


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
        return data[name]

    @staticmethod
    @upd_file
    def get_list(name, data, calories):
        return data

    @staticmethod
    @upd_file
    def create_product(product, data, calories):
            data.update({product: calories})

    @staticmethod
    @upd_file
    def delete_product(product, data, calories):
        data.pop(product)

    @staticmethod
    @upd_file
    def update_product(product, data, calories):
        data[product] = calories

    def get_user_calories(self):
        """
        :return: User calories
        """
        return self.user_calories

    def set_user_calories(self, new_calories):
        self.user_calories = new_calories
