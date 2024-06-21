#!/usr/bin/python3
"""
4-cities_by_state module
Lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def list_cities():
    """
    Connects to the MySQL database and lists
    all cities along with their respective states.
    """
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

        # Execute the SQL query to list cities and their states
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cur.execute(query)

        # Fetch all the results and print them
        cities = cur.fetchall()
        for city in cities:
            print(city)

        # Close the cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")


if __name__ == "__main__":
    list_cities()
