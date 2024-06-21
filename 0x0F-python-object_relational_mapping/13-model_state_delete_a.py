#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
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

    # Query and delete all State objects with name containing 'a'
    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
