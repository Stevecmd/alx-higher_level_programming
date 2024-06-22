#!/usr/bin/python3
"""
5-filter_cities module
Lists all cities of a specified state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities():
    """
    Connects to the MySQL database and lists
    all cities of the specified state.
    """
    if len(sys.argv) != 5:
        print(
            "Usage: ./5-filter_cities.py <username> <pass> <DB> <state_name>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Execute the SQL query to list cities of the specified state
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cur.execute(query, (state_name,))

        # Fetch all the results
        rows = cur.fetchall()

        # Check if cities were found for the state
        if not rows:
            print(f"No cities found for state '{state_name}'")
        else:
            # Extract city names from the results
            city_names = [row[0] for row in rows]
            # Print the cities as comma-separated values
            print(", ".join(city_names))

        # Close the cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")


if __name__ == "__main__":
    filter_cities()
