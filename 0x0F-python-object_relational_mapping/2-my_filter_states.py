#!/usr/bin/python3
"""script takes arg and displays values where matches the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    bacon = db.cursor()
    bacon.execute(
        "SELECT * FROM states WHERE BINARY name='{}'\
            ORDER BY id ASC".format(argv[4]))
    burger = bacon.fetchall()
    for bu in burger:
        print(bu)
    bacon.close()
    db.close()
