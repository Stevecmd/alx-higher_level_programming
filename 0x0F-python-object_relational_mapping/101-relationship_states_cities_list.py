#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa.
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
    engine = create_engine(db_uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch all states and their cities,
    # sorted by state.id and city.id
    # states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
