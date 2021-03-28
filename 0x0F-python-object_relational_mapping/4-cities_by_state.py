#!/usr/bin/python3
"""script safe from MySQL injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    bacon = db.cursor()
    bacon.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    burger = bacon.fetchall()
    for bu in burger:
        print(bu)
    bacon.close()
    db.close()
