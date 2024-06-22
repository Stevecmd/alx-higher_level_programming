#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine and bind the Base metadata
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all City objects with their associated State objects
        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            # Access the State object through the relationship 'state'
            state_name = city.state.name
            print(f"{city.id}: {city.name} -> {state_name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
