import sqlite3

# Connect to the database
waifu = sqlite3.connect("anime_database.db")

# Create a table
waifu.execute("CREATE TABLE IF NOT EXISTS waifus (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Get the database version
# print(f"Current database version: {waifu.version}")
# Get the database version
cursor = waifu.cursor()
cursor.execute("PRAGMA user_version")
db_version = cursor.fetchone()[0]
print(f"Current database version: {db_version}")

# Insert data into the table
waifu.execute("INSERT INTO waifus (name, age) VALUES ('Nami', 21)")
waifu.execute("INSERT INTO waifus (name, age) VALUES ('Robin', 18)")
waifu.execute("INSERT INTO waifus (name, age) VALUES ('hinata', 18)")

waifu.commit()

# Select data from the table
cursor = waifu.execute("SELECT * FROM waifus")
for row in cursor:
    print(row)

# Update data in the table
waifu.execute("UPDATE waifus SET age = 20 WHERE name = 'Robin'")
waifu.commit()

# Delete data from the table
waifu.execute("DELETE FROM waifus WHERE name = 'Nami'")
waifu.commit()

# Close the connection to the database
waifu.close()
