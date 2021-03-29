#!/usr/bin/python3
"""Delete states"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    burger = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for beer, fries in burger:
        print("{}: ({}) {}".format(fries.name, beer.id, beer.name))
    session.close()
