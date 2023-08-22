def zander():
    zander_len = int(input("Input length of the zander: "))
    if zander_len < 42:
        print("Your zander was not big enough, it needs to be", 42-zander_len, "cm longer.\n Release the fish back in to the lake")


def cabin_class():
    given_class = input("Please enter your cabin class: ")
    if given_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif given_class == "A":
        print("Above the car deck, equipped with a window.")
    elif given_class == "B":
        print("Windowless cabin above the car deck.")
    elif given_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")


def hemoglobin_value():
    gender = input("Please type your gender: ")
    hemoglobin = int(input("Please enter your hemoglobin: "))
    if gender != "Male" and gender != "Female":
        print("Not valid gender, valid genders: Male / Female")
    elif (gender == "Male" and hemoglobin > 167) or (gender == "Female" and hemoglobin > 155):
        print("Your hemoglobin is high")
    elif (gender == "Male" and hemoglobin < 134) or (gender == "Female" and hemoglobin < 117):
        print("Your hemoglobin is low")
    else:
        print("Your hemoglobin is normal")


def check_if_leap_year():
    y = int(input("Enter year to check if it is a leap year: "))
    if (y % 100 == 0 and y % 400 == 0) or y % 4 == 0 and y % 100 != 0:
        print("The year is a leap year")
    else:
        print("Not a leap year")



