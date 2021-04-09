#!/usr/bin/python3
""" This is to join the states and cities """

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import MySQLdb
    from sys import argv
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state, city in session.query(State, City).join(City).order_by(City.id)\
                                                            .all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()