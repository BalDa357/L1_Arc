import configparser
import sqlite3 as lite

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
    def __init__(self):
        self.con = lite.connect('test.db')
        self.database = self.con.cursor()

    def get_list(self):
        self.database.execute("SELECT * FROM Products")
        rows = self.database.fetchall()
        products = {}
        for row in rows:
            products[row[0]] = row[1]
        return products

    def get_product(self, name):
        data = self.get_list()
        return data[name]

    def create_product(self, name, calories):
        self.database.execute("INSERT INTO Products VALUES (?,?)", (name, calories))

    def delete_product(self, name):
        self.database.execute("DELETE FROM Products WHERE NAME =:NAME ", {"NAME": name})

    def update_product(self,name, calories):
        self.database.execute("UPDATE Products SET CALORIES=? WHERE NAME =?", (calories, name))


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
