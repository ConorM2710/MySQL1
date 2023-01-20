from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famour_for = Column(String)


Session = sessionmaker(db)

session = Session()


base.metadata.create_all(db)


ada_lovelace = Programmer(
    first_name="Ada",  
    last_name="Lovelace",
    gender="F",
    nationality="British", 
    famour_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",  
    last_name="Turing",
    gender="M",
    nationality="British", 
    famour_for="Modern Computing"
)


# session.add(ada_lovelace)


session.commit()


programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famour_for,
        sep=" | "
    )