import mysql.connector

conn = mysql.connector.connect( host="your_mysql_host", user="your_mysql_user",

password="your_mysql_password",

database="airports"

)

cursor = conn.cursor()

country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()

cursor.execute("SELECT ident, name, type FROM airport WHERE LEFT(ident, 2) = %s ORDER BY type", (country_code,))

results = cursor.fetchall()

if results:
 print(f"Airports in {country_code}:")

for ident, name, airport_type in results: print(f"{name} ({airport_type} airport) [{ident}]")
else:

 print(f"No airports found in {country_code}.")
 cursor.close()

conn.close()