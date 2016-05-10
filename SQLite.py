import sqlite3 as lite

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
        self.con.commit()

    def delete_product(self, name):
        self.database.execute("DELETE FROM Products WHERE NAME =:NAME ", {"NAME": name})
        self.con.commit()

    def update_product(self,name, calories):
        self.database.execute("UPDATE Products SET CALORIES=? WHERE NAME =?", (calories, name))
        self.con.commit()