import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="Tanya",
    password="Rst100",
    database="flight_game"
)

cursor = conn.cursor()

country_code = input("Type in the country code (for example, FI for Finland): ").strip().upper()

cursor.execute("SELECT ident, name, type FROM airport WHERE LEFT(ident, 2) = %s ORDER BY type", (country_code,))

results = cursor.fetchall()

if results:
 print(f"The airports in {country_code}:")

for ident, name, airport_type in results: print(f"{name} ({airport_type} airport) [{ident}]")
else:

 print(f"Sorry, but no airports are found in the country with the country code {country_code}.")
 cursor.close()

conn.close()