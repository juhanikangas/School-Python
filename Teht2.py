import math as m
import random as r


# 1
def name_input():
    name = input("Please enter your name: ")
    print("Hello, " + name + "!")


# 2
def circle_rad():
    rad = float(input("Please enter the radius of the given circle: "))
    print("The area of the given circle is: ", m.pi * rad * rad)


# 3
def rec_per_and_area():
    rec_len = int(input("Please enter the length of the given rectangle: "))
    rec_wid = int(input("Please enter the width of the given rectangle: "))
    rec_per = rec_len * 2 + rec_wid * 2
    rec_area = rec_len * rec_wid
    print("The Perimeter of the given rectangle is ", rec_per, " and the area is ", rec_area)


# 4
def sum_product_avarage():
    f = int(input("Type first digit: "))
    s = int(input("Type second digit: "))
    t = int(input("Type third digit: "))
    print("The sum of the digits:", f + s + t, "The product is:", f * s * t, "The average is:", (f + s + t) / 3)


# 5
def calculate_mass():
    t = float(input("Enter talents: "))
    p = float(input("Enter pounds: "))
    l = float(input("Enter lots: "))
    total_grams = l * 13.3 + p * 425.6 + t * 8512
    grams = round(float(total_grams % 1000), 2)
    kg = total_grams / 1000
    print("The weight in modern units:\n", int(kg), " kilograms and ", grams, " grams.")


# 6
def combination_locs():
    comb_lock1 = [r.randint(0,9),r.randint(0,9),r.randint(0,9)]
    comb_lock2 = [r.randint(1, 6), r.randint(1, 6), r.randint(1, 6),r.randint(1, 6)]
    print("combination lock 1: ",*comb_lock1, sep="")
    print("combination lock 2: ",*comb_lock2, sep="")

