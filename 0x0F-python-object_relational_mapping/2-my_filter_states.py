#!/usr/bin/python3
"""
2-my_filter_states module
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def filter_states():
    """
    Connects to the MySQL database and displays
    all values in the states table where name matches the given argument.
    """
    # Check if all necessary arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py "
              "<username> <password> <database> <state_name>")

        return

    # Get MySQL credentials and database name from command-line arguments
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

        # Execute the SQL query to find states with the given name
        query = """
        SELECT id, name
        FROM states
        WHERE name = %s
        ORDER BY id ASC
        """
        cur.execute(query, (state_name,))

        # Fetch all the results and print them
        states = cur.fetchall()
        for state in states:
            print(state)

        # Close the cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")


if __name__ == "__main__":
    filter_states()
