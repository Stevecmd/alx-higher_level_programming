"""
5-filter_cities module
Lists all cities of a specified state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to the MySQL database and lists
    all cities of the specified state.
    """

    # Get MySQL credentials,
    db = db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
                  ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
