#!/usr/bin/python3
"""prints the State object name passed as arg"""

from sys import argv
from model_state import Base, State
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
    burger = session.query(State).filter(State.name == argv[4]).first()
    if burger is None:
        print("Not found")
    else:
        print("{}".format(burger.id))
    session.close()
