#!/usr/bin/python3
"""
Define a State class
that inherits from sqlalchemy Base
"""
from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1],
        sys.argv[2],
        sys.argv[3]))

    # A session is like a workspace for making changes and interacting with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    state_names = session.query(State).order_by(State.id)

    for state in state_names:
        print('{}: {}'.format(state.id, state.name))
