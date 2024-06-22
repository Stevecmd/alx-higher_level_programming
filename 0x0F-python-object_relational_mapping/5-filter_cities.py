#!/usr/bin/python3
"""
5-filter_cities module
Lists all cities of a specified state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username, password, database, state_name = argv[1:5]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )
    # queries to be run
    query = "SELECT cities.name\
            FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name = %s"
    conn = db.conn()
    conn.execute(query, (state_name, ))
    cities = [city[0] for city in conn.fetchall()]
    print(", ".join(cities))
    conn.close()
    db.close()
