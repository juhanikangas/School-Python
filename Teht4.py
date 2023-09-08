import math as m
import random


# 1
def divisible_by_three():
    i = 3
    while i < 1000:
        print(i)
        i += 3


# 2
def inches_to_cm():
    inches = int(input("Input inches: "))
    while inches > 0:
        print(inches, "inches is", inches * 2.54, "cm")
        inches = int(input("Input inches: "))


# 3
def smallest_and_largest_num():
    run = True
    biggest_num = 0
    smallest_num = 0
    while run:
        num = input("Input num: ")
        try:
            int(num)
            num = int(num)
            if num > biggest_num:
                biggest_num = num
            elif num < smallest_num:
                smallest_num = num
        except ValueError:
            run = False
            print("Smallest given number was:", smallest_num, "\n Biggest given number was:", biggest_num)


def quess():
    randint = random.randint(1, 10)
    quess = 0
    while quess != randint:
        quess = int(input("Quess the number: "))
        if quess > randint:
            print("Too High")
        elif quess < randint:
            print("Too low")
    print("Correct")


# 5
def create_user():
    username = "python"
    password = "rules"
    logged_out = True
    attempt = 0
    while logged_out and attempt < 5:
        u = input("Please give username: ")
        p = input("Please give password: ")
        attempt += 1
        if u == username and password == p:
            logged_out = False
        else:
            print("username or password was incorrect")
    if logged_out:
        print("Access denied")
    else:
        print("Welcome")

# 6
def approx_of_pie():
    r = 1
    circle_area = m.pi * r**2
    s = 2
    square_area = s * s
    p = (circle_area / square_area) * 100
    approx = 4 * p/100
    print(approx)

yp = 0
while n <= pisteet
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if


pii = (4 * yp) / pisteet



