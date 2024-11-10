from sqlalchemy import(
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

#create a class-base model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly wi will request for a session  
# create a new instance of a sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using decleratibe_base subclass
base.metadata.create_all(db)

# creating recored on our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"

)
paul_dominan = Programmer(
    first_name = "Paul",
    last_name = "Dominan",
    gender = "M",
    nationality = "Romanian",
    famous_for = "Programmer"

)

# add each instance of our programmer to our session
session.add(ada_lovelace)
session.add(paul_dominan)

# commit our session to the database
#session.commit()

# updating a single record
#programmer = session.query(Programmer).firlter_by(id=7).first()
#programmer.famous_for = "World President"

# commit our session to the database
#session.commit()


# updating multiple records
people = session.query(Programer)
for person in people:
    if person.gender == "F":
        person.genger == "Female"
    elif person.gender == "M":
        person.gender == "Male"
    else:
        print("Gender not defined")
    session.commit()


# deleting a single record
name = input("Enter a first name")
name = input("Enter a last name")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delet this record(y/n) ")
    if confirmation.lower()== "y":
        session.delete(programer)
        session.commit()
        print("Programmer was deleted")
    else:
        print("Programmer not deleted")
else:
    print("No recored found")


# query to find all programers 
programers = session.query(Programmer)
for programer in programers:
    print(
        programer.id,
        programer.first_name + " " + programer.last_name,
        programer.gender,
        programer.nationality,
        programer.famous_for,
        sep=" | "
    )


