import mysql.connector

conn = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="airports"
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
