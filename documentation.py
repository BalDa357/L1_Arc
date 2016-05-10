# import configparser
# import pydoc
# import MODEL
# import CONTROLLER
# pydoc.writedoc(CONTROLLER)

import sqlite3 as lite


def get_list(database):
    database.execute("SELECT * FROM Products")
    rows = database.fetchall()
    products = {}
    for row in rows:
        products[row[0]] = row[1]
    return products


def create_product(name, calories, database):
    database.execute("INSERT INTO Products VALUES (?,?)", (name, calories))


def delete(name, database):
    database.execute("DELETE FROM Products WHERE NAME =:NAME ", {"NAME": name})


def update(name, calories, database):
    database.execute("UPDATE Products SET CALORIES=? WHERE NAME =?", (calories, name))


if __name__ == '__main__':
    con = lite.connect('test.db')

    with con:
        database = con.cursor()
        print(get_all(database))
        #prd = {"bread": 200, "coffee": 25, "milk": 10, "potato": 202, "tomato": "40", "ice cream": 222, "butter": 350}
        #for k in prd:
            #create(k, prd[k], database)
            # database.execute("CREATE TABLE Products(NAME TEXT NOT NULL PRIMARY KEY UNIQUE , CALORIES INT)")
