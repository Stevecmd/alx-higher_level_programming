#!/usr/bin/python3
"""
Lists all State objects and corresponding
City objects contained in the database
hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database
    )
    engine = create_engine(db_uri, pool_pre_ping=True)

    # Bind the engine to the Base class which defines the models
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all State objects and their cities, sorted by state id and city id
    states = session.query(State)\
                    .options(joinedload(State.cities))\
                    .order_by(State.id)\
                    .all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda c: c.id):
            print("\t{}: {}".format(city.id, city.name))

    session.close()
