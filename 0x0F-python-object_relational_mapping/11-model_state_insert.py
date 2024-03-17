#!/usr/bin/python3
"""script that adds the State object “Louisiana” 
to the database hbtn_0e_6_usa:"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create Session
    Session = sessionmaker(bind=engine)
    session = Session()
    newState  = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print("{0}".format(newState.id))
