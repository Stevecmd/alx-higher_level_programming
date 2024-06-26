#!/usr/bin/python3
"""
3-my_safe_filter_states module
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument (safe from SQL injection).
"""
import MySQLdb
import sys


def filter_states():
    """
    Connects to the MySQL database and displays
    all values in the states table where name matches the given argument.
    """
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py "
              "<username> <password> <database> <state_name>")

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

        # Execute the SQL query with parameters to
        # find states with the exact given name
        query = """
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY id ASC
        """
        # Using parameters to avoid SQL injection
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
        sys.exit(1)


if __name__ == "__main__":
    filter_states()
