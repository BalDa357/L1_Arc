__author__ = 'Dart Vader'
import pickle

class DataProcessing:
    def __init__(self):
        """
        Read dictionary from pickle file
        :return:
        """
        with open('data.pickle', 'rb') as f:
            self.data_new = pickle.load(f)
        self.user_calories = 0

    def getData(self):
        """
        :return: Dictionary of all products and calories per 100 gram this product
        """
        return self.data_new

    def getUserCalories(self):
        """
        :return: User calories
        """
        return self.user_calories

    def ResetValues(self):
        """
        Reset count of user calories
        :return:
        """
        self.user_calories = 0

    def calorie (self, name):
        """
        Returns the amount of calories per 100 grams. of chosen product
        :param name: chosen product
        :return: amount of calories per 100 grams
        """
        if name in self.data_new:
            return self.data_new[name]
        else:
            return False

    def calories_amount(self, name, mass):
        """
        Count all calories of chosen products
        :param name: chosen product
        :param mass: product mass
        :return:
        """
        if self.calorie(name):
            self.user_calories += (mass/100)*self.calorie(name)
            return self.user_calories
        else:
            return False
