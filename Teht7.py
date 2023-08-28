
# 1

def get_month():
    month = int(input("Type month: "))

    # Calculate the season based on the month
    season_index = (month - 1) // 3
    seasons = ["winter", "spring", "summer", "autumn"]
    season = seasons[season_index]

    print(f"The corresponding season for month {month} is {season}.")


# 2
def print_names():

    n = input("Give name: ")
    name_list = []
    while n != "":
        if n in name_list:
            print(n, " is already in list")
        else:
            print(n, " is a new name")
            name_list.append(n)
        n = input("Give name: ")
    print(name_list)


# 3
def makeshift_airport_datbase():

    method = input("Type method GET, ADD or QUIT: ")
    data = {}
    while method != "QUIT":
        if method == "GET":
            get_icao = input("Input ICAO: ")
            print(data[get_icao])
        elif method == "ADD":
            icao = input("Give airport ICAO: ")
            airport_name = input("Give airport name: ")
            data[icao] = airport_name
        method = input("Type method GET, ADD or QUIT: ")

