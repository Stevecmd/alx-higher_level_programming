#!/usr/bin/python3
"""
empty-db.py
Script to delete all content from the 'states' table in the 'hbtn_0e_0_usa' database.
"""

import MySQLdb
import sys

def empty_states_table(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create cursor object
        cur = db.cursor()

        # Delete all rows from states table
        delete_query = """
        DELETE FROM states
        """
        cur.execute(delete_query)

        # Commit changes
        db.commit()

        print("All content deleted from 'states' table in database '{}'.".format(database))

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./empty-db.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    empty_states_table(username, password, database)
