#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine to connect to the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object where id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name attribute of the State object
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    # Close the session
    session.close()
