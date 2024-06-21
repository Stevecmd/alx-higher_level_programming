#!/usr/bin/python3
"""
2-my_filter_states module
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database, user_input = argv[1:5]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' " \
            "ORDER BY id ASC".format(user_input)
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
