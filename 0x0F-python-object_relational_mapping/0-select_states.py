#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves and prints data
    from the 'states' table.

    Usage: python script.py <user> <password> <database>
    """
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states")
    states = mycursor.fetchall()

    for state in states:
        print(state)


if __name__ == "__main__":
    main()
