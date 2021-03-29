#!/usr/bin/python3
"""script safe from MySQL injections!"""

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
    burger = session.query(State).order_by(State.id).all()
    for bu in burger:
        print("{}: {}".format(bu.id, bu.name))
    session.close()
