import psycopg2

# Connect to Chenook databsae
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# fetch the results(multiple)
results = cursor.fetchall()

# Query 1 - Select all records from the "Artists" table
cursor.execute('SELECT * FROM "Artist"' )

# Query  - Select only the "Name" column from the "Artists" table
cursor.execute('SELECT "Name" FROM "Artist"' )

# to fetch for results(single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)