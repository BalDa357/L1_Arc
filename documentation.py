# import configparser
# import pydoc
# import MODEL
# import CONTROLLER
# pydoc.writedoc(CONTROLLER)

import pymysql as mdb
import sys
import sqlite3 as lite


def get_list(database):
    database.execute("SELECT * FROM Products")
    rows = database.fetchall()
    products = {}
    for row in rows:
        products[row['NAME']] = row['CALORIES']
        #print(row)
    return products


def create_product(name, calories, database):
    database.execute("INSERT INTO Products(NAME, CALORIES) VALUES (%s,%s)", (name, calories))


def delete(name, database):
    database.execute("DELETE FROM Products WHERE NAME =:NAME ", {"NAME": name})


def update(name, calories, database):
    database.execute("UPDATE Products SET CALORIES=? WHERE NAME =?", (calories, name))


if __name__ == '__main__':
    #con = lite.connect('test.db')
    con = mdb.connect(host='localhost',
                             user='root',
                             password='4075',
                             db='test',
                             charset='utf8mb4',
                             cursorclass = mdb.cursors.DictCursor)


    with con:

        database = con.cursor()
        #database.execute("CREATE TABLE Products(NAME VARCHAR(30) NOT NULL PRIMARY KEY UNIQUE , CALORIES INT)")
        print(get_list(database))
        #prd = {"bread": 200, "coffee": 25, "milk": 10, "potato": 202, "tomato": 40, "ice cream": 222, "butter": 350}
        #for k in prd:
        #    create_product(k, prd[k], database)







