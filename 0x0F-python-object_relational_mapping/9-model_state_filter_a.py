#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a():
    """
    Connects to the MySQL database and fetches all states containing 'a'.
    """
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Setup the database connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Bind the engine to the Base
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all State objects containing 'a' in their name
        states_with_a = session.query(State)\
                      .filter(State.name.like('%a%'))\
                      .order_by(State.id)\
                      .all()

        # Print the results
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    filter_states_with_a()
