#!/usr/bin/python3
"""
5-filter_cities module
Lists all cities of a specified state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> \
                <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database
    )

    # Create a cursor object
    cur = db.cursor()
    # Execute the query
    query = "SELECT cities.name\
            FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name = %s"
    # Fetch and print results
    cities = [city[0] for city in cur.fetchall()]
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()
