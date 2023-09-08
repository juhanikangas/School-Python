import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='JKmaria23',
    autocommit=True
)

# 1
def get_airport_name_and_location(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in res:
            print(row)
    return

#icao = input("Input ICAO: ")
#get_airport_name_and_locatio

# 2
def get_located_airports(area_code):
    sql = "SELECT name, type FROM airport WHERE iso_country='" + area_code + "' ORDER BY type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in res:
            print(row)
    return

#area_code = input("Input area code: ")
#get_located_airports(area_code)
def airport_distance(icao1, icao2):
    airport1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident='" + icao1 + "'"
    airport2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident='" + icao2 + "'"

    cursor = connection.cursor()
    cursor.execute(airport1)
    res = cursor.fetchall()[0]
    cursor.execute(airport2)
    res2 = cursor.fetchall()[0]
    print(distance.distance(res, res2).km)


#icao1 = input("Input icao1: ")
#icao2 = input("Input icao2: ")
#airport_distance(icao1, icao2)
