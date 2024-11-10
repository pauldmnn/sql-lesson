from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# creating the intructions from our localhost "chinook" db
db = create_engine("posgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist"
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album"
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track"
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenderId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)

)

# making the connection
with db.connect() as connection:

    # query number 1: select all "Artist" from the table
    select_query = artist_table.select()

    # query number 2: Select only "Name" column from the "Artist" table
    select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query muber 3: Select only "Queen" from the "Artist" table
    select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query number 4: Select only by "ArtistId" #51 on the "Album" table
    

    results = connection.execute(select_query)
    for result in results:
        print(results)
