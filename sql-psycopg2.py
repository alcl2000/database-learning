import psycopg2

# connecting the db to python and psyco
connection = psycopg2.connect(database="chinook")

# used to gather results from the table
cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist"')
cursor.execute('SELECT * FROM "Track" WHERE "Composer"="Queen"')

# fetching results from the cursor (all results)
results = cursor.fetchall()
# results = cursor.fetchone() - fetching results from the cursor (just one)

connection.close()

for result in results:
    print(result)
