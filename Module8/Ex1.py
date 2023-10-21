import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="Tanya",
    password="Rst100",
    database="flight_game"
)

cursor = conn.cursor()

icao_code = input("Enter the ICAO code of an airport: ").strip().upper()

cursor.execute("SELECT name, location FROM airport WHERE ident = %s", (icao_code,))

result = cursor.fetchone()

if result:
    airport_name, location = result
    print(f"Airport Name: {airport_name}")
    print(f"Location (Town): {location}")
else:
    print("Airport not found in the database.")

cursor.close()
conn.close()
