#!/usr/bin/python3
"""
1-filter_states module
Lists all unique states with a name starting with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states():
    """
    Connects to the MySQL database and lists
    all unique states with a name starting with 'N'.
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

    # Execute the SQL query to list unique states with names starting with 'N'
    query = """
    SELECT DISTINCT id, name
    FROM states
    WHERE name LIKE 'N%'
    ORDER BY id ASC
    """
    cur.execute(query)

    # Fetch all the results and print them
    states = cur.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
