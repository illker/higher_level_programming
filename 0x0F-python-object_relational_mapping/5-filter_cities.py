#!/usr/bin/python3
"""script safe from MySQL injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    bacon = db.cursor()
    bacon.execute("SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id=states.id \
            WHERE states.name=%s ORDER BY cities.id", (argv[4],))
    burger = bacon.fetchall()
    print(", ".join(bu[0] for bu in burger))
    bacon.close()
    db.close()
