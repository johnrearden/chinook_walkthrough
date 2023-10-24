import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
cursor.execute(f'SELECT * FROM "Artist" WHERE "Name" = {"Queen"}')

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
