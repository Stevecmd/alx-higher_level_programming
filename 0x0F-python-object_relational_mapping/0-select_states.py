#!/usr/bin/python3
"""
0-select_states module
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the MySQL database and lists all states.
    """
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the SQL query to list all states
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results and print them
    states = cur.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
