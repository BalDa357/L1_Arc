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

    @property
    def get_data(self):
        """
        :return: Dictionary of all products and calories per 100 gram this product
        >>> dp = DataProcessing()
        >>> dp.get_data
        {'basmati rice': 58, 'cornflakes': 84, 'pineapple, fresh': 66, 'rye bread': 65, 'weetabix': 69, 'french fries': 75, 'honey': 58, 'boiled potatoes': 56, 'mars bar': 68, 'branflakes': 74, 'jacket potato': 85, 'cheerios': 74, 'puffed wheat': 89, 'ice cream': 61, 'pitta bread': 57, 'baguette': 95, 'swede': 72, 'bagel': 72, 'parsnips, boiled': 97, 'cantaloupe melon': 67, 'couscous': 65, 'muesli, non toasted': 56, 'white bread': 70, 'crumpet, toasted': 69, 'jelly beans': 80, 'coco pops': 77, 'raisins': 64, 'shortbread biscuit': 64, 'white rice, steamed': 98, 'new potatoes': 62, 'coca cola': 63, 'digestive biscuit': 59, 'ryvita': 69, 'watermelon': 72, 'wholemeal bread': 69, 'cheese and tomato pizza': 60, 'croissant': 67, 'rice cakes': 82, 'shredded wheat': 67, 'apricots, canned in syrup': 64, 'rice krispies': 82, 'mashed potato': 70, 'sultanas': 56}

        """
        return self.data_new

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
