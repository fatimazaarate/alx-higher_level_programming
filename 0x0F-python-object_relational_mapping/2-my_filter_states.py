#!/usr/bin/python3
"""
    Connects to a MySQL database and retrieves and prints data
    from the 'states' table.

    Usage: python script.py <user> <password> <database>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    state_name = sys.argv[4]

    mycursor = mydb.cursor()
    mySQLformulat = "SELECT * \
        FROM states WHERE name = '{:s}' \
        ORDER BY id ASC".format(state_name)

    mycursor.execute(mySQLformulat)
    states = mycursor.fetchall()

    for state in states:
        print(state)
