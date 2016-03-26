import pickle

__author__ = 'Dart Vader'


class DataProcessing:
    def __init__(self):
        """
        Read dictionary from pickle file
        :return:
        >>> dp = DataProcessing()
        """

        with open('data.pickle', 'rb') as f:
            self.data_new = pickle.load(f)
        self.user_calories = 0

    def get_data(self):
        """
        :return: Dictionary of all products and calories (100g) this product
        """
        print(self.data_new)
        return self.data_new

    def add_new_product(self, name, calories):
        """
        Recreating pickle file
        """
        self.data_new.update({name:calories})
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.data_new, f)


    def get_user_calories(self):
        """
        :return: User calories
        """
        return self.user_calories

    def reset_values(self):
        """
        Reset count of user calories
        :return:
        >>> dp = DataProcessing()
        """
        self.user_calories = 0

    def calorie(self, name):
        """
        Returns the amount of calories per 100 grams. of chosen product
        :param name: chosen product
        :return: amount of calories per 100 grams

        >>> dp = DataProcessing()
        >>> dp.calorie('ice cream')
        61
        """
        if name.lower() in self.data_new:
            return self.data_new[name]
        else:
            return False

    def calories_amount(self, name, mass):
        """
        Count all calories of chosen products
        :param name: chosen product
        :param mass: product mass
        :return:
        >>> dp = DataProcessing()
        >>> dp.calories_amount('ice cream', 200)
        122.0

        """
        if self.calorie(name.lower()):
            self.user_calories += round((int(mass)/100)*self.calorie(name), 3)
            return self.user_calories
        else:
            return False

