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
    # Get MySQL credentials, database name,
    # and state name from command-line arguments
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
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        """
        cur.execute(query, (state_name,))

        # Fetch the result
        cities_result = cur.fetchone()[0]

        # Print the result if cities are found for the state
        if cities_result:
            print(cities_result)
        else:
            print(f"No cities found for state '{state_name}'")

        # Close the cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")


if __name__ == "__main__":
    filter_cities()
