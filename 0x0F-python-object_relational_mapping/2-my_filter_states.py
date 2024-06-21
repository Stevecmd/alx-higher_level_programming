#!/usr/bin/python3
"""
2-my_filter_states module
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


def filter_states(username, password, database, state_name):
    """
    Connects to the MySQL database and displays
    all values in the states table where name matches the given argument.
    """

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cur = db.cursor()

        cur.execute("SELECT * \
                    FROM `states` \
                    WHERE BINARY `name` = '{}'".format(sys.argv[4]))
        [print(state) for state in cur.fetchall()]
