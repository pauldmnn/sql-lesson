from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")

base = declarative_base()

# create a class=base model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class=base model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = (Integer, ForeignKey("Artist.ArtostId"))

# create a class=base model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenderId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly wi will request for a session  
# create a new instance of a sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using decleratibe_base subclass
base.metadata.create_all(db)

# query number 1: select all "Artist" from the table
artist = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")

# query number 2: Select only "Name" column from the "Artist" table
artist = session.query(Artist)
for artist in artists:
    print(artist.Name)

# query muber 3: Select only "Queen" from the "Artist" table
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")

# query number 4: Select only by "ArtistId" #51 on the "Album" table
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ")
