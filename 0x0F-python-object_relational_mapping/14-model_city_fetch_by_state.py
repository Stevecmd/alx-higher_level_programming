#!/usr/bin/python3
"""
Fetch all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Database credentials
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connection string
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    try:
        # Query to fetch all cities sorted by id
        results = session.query(State, City).join(City).order_by(City.id).all()

        # Print results grouped by state name
        for state, city in results:
            print(f"{state.name}: ({city.id}) {city.name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
