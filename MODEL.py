__author__ = 'Dart Vader'

import pickle

class DataRead:
    user_calories = 0
    def __init__(self):
        with open('data.pickle', 'rb') as f:
            self.data_new = pickle.load(f)

    def getData(self):
        return self.data_new

    def calorie (self, name):
        if name in self.data_new:
            return self.data_new[name]
        else:
            return False

    def calories_amount(self, name, mass):
        if self.calorie(name):
            return self.user_calories + (mass/100)*self.calorie(name)
        else:
            return False
