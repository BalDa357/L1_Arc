import psycopg2 as pdb

class Products:
    def __init__(self):
        self.con = pdb.connect(host='localhost', database='test', user='karl',password='1111')
        self.database = self.con.cursor()


    def get_list(self):
        self.database.execute("SELECT * FROM Products")
        rows = self.database.fetchall()
        products = {}
        for row in rows:
            products[row[0]] = row[1]
        return products

    def create_product(self, name, calories):
        self.database.execute("INSERT INTO Products(NAME, CALORIES) VALUES (%s,%s)", (name, calories))
        self.con.commit()

    def delete_product(self,name):
        self.database.execute("DELETE FROM Products WHERE 'NAME'={}".format(name))
        self.con.commit()

    def update_product(self, name, calories):
        self.database.execute("UPDATE Products SET CALORIES=%s WHERE NAME =%s", (calories, name))
        self.con.commit()


