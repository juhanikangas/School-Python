from flask import Flask, request
from Teht8 import get_airport_name_and_location
import mysql.connector

app = Flask(__name__)
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='',
    password='',
    autocommit=True
)


# 1
@app.route('/prime_number/<n>')
def prime_number(n):
    flag = False
    num = int(n)
    is_prime = "error"
    if num == 1:
        is_prime = False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            is_prime = False
        else:
            is_prime = True

    response = {
        "prime_number": {"Number": num, "isPrime": is_prime}
    }

    return response


# 2
@app.route('/airport/<ICAO>')
def airport(ICAO):
    res = get_airport_name_and_location(ICAO)
    response = {
        "ICAO": ICAO,
        "Name": res[0][0],
        "Location": res[0][1],
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
