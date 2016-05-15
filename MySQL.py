import pymysql as mdb

class Products:
    def __init__(self):
        self.con = mdb.connect(host='localhost',
                             user='root',
                             password='4075',
                             db='test',
                             charset='utf8mb4',
                             cursorclass = mdb.cursors.DictCursor)
        self.database = self.con.cursor()


    def get_list(self):
        self.database.execute("SELECT * FROM Products")
        rows = self.database.fetchall()
        products = {}
        for row in rows:
            products[row['NAME']] = row['CALORIES']
        return products

    def create_product(self, name, calories):
        self.database.execute("INSERT INTO Products(NAME, CALORIES) VALUES (%s,%s)", (name, calories))
        self.con.commit()

    def delete_product(self,name):
        self.database.execute("DELETE FROM Products WHERE NAME =%s ", (name))
        self.con.commit()

    def update_product(self, name, calories):
        self.database.execute("UPDATE Products SET CALORIES=%s WHERE NAME =%s", (calories, name))
        self.con.commit()

