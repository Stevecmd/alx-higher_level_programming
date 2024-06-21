#!/usr/bin/python3
"""
2-my_filter_states module
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


if __name__ == "__main__":

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the SQL query with parameterized query
        name_pattern = sys.argv[4]
        query = (
            "SELECT * "
            "FROM states "
            "WHERE name LIKE BINARY '{}'".format(name_pattern)
        )

        cur.execute(query)

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
