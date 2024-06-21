#!/usr/bin/python3
"""
2-my_filter_states module
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
        sys.exit(1)

    # Assign command line arguments to variables
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_pattern = sys.argv[4]

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

        # Execute the SQL query with parameterized query
        query = "SELECT * FROM states WHERE name LIKE BINARY %s"
        cur.execute(query, (name_pattern,))

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
