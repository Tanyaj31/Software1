from geopy.distance import great_circle

airport_coordinates = {
    'KAUS': (30.197535,-97.662015),  #latitude_deg,longitude_deg for KAUS (Austin Bergstrom International Airport)
    'EGPH': (55.950145,-3.372288),  #latitude_deg,longitude_deg for EGPH (Edinburgh Airport)
}

def get_distance(icao1, icao2):
    if icao1 not in airport_coordinates or icao2 not in airport_coordinates:
        return None

    coord1 = airport_coordinates[icao1]
    coord2 = airport_coordinates[icao2]

    distance = great_circle(coord1, coord2).kilometers
    return distance

def main():
    icao1 = input("Type in the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Type in the ICAO code of the second airport: ").strip().upper()

    distance = get_distance(icao1, icao2)

    if distance is not None:
        print(f"The distance between {icao1} and {icao2} is approximately {distance:.2f} kilometers.")
    else:
        print("Sorry, but this ICAO code is not found in the database.")

if __name__ == "__main__":
    main()
