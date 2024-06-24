#!/usr/bin/python3
"""
Prints the State and City objects from the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    # Database connection parameters
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_connection_string = (
        f'mysql+mysqldb://{db_user}:{db_password}@'
        f'localhost:3306/{db_name}'
    )

    # Create a database engine
    engine = create_engine(db_connection_string)

    # Create the required tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State and associated City objects
    states = (
        session.query(State)
        .options(joinedload(State.cities))
        .order_by(State.id)
        .all()
    )

    for state_instance in states:
        print(f"{state_instance.id}: {state_instance.name}")
        for city_instance in state_instance.cities:
            print(f"    {city_instance.id}: {city_instance.name}")

    session.close()
