#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state():
    """
    Connects to the MySQL database and fetches the first state by id.
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
        # Query the first State object based on the id
        state = session.query(State).order_by(State.id).first()

        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    fetch_first_state()
