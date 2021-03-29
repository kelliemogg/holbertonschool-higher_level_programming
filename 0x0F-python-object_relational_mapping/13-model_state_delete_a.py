#!/usr/bin/python3
""" Lists the first state objects from the database hbtn_0e_6_usa """

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import MySQLdb
    from sys import argv
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)

    session.commit()
    session.close()
