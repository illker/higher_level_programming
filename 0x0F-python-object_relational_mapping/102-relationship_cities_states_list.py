#!/usr/bin/python3
"""lists all City objects from a database"""


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(argv[1],
                                argv[2],
                                argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    rows = session.query(City).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
