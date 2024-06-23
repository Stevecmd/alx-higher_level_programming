#!/usr/bin/python3
"""
Lists all State objects and corresponding
City objects contained in the database
hbtn_0e_101_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, database = argv[1:4]
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database
    )
    engine = create_engine(db_uri)

    # Create the required tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch all states and their cities,
    # sorted by state.id and city.id
    # states = session.query(State).order_by(State.id).all()

    for state_instance in session.query(State).order_by(State.id):
        print(state_instance.id, state_instance.name, sep=": ")

        for city_instance in state_instance.cities:
            print("    ", end="")
            print(city_instance.id, city_instance.name, sep=": ")

    session.close()
