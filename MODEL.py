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
