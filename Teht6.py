import random as r
import math as m

# 1 Rolls dice until it lands on the biggest possible number, Params( sides: amount of sides the dice will have)
def random_diceroll(sides):
    roll = 0
    while roll != sides:
        roll = r.randint(1, sides)
        print(roll)


# 2 Asks for liters and converts them into gallons
def gallons_to_liters():
    def magic(ls):
        g = 0.2199693
        return ls * g

    liters = int(input("Liters to be converted: "))
    while liters > 0:
        gallons = magic(liters)
        print("~", round(gallons, 2), " gallons")
        liters = int(input("Liters to be converted: "))


# 3-4 Asks user for number to put in a list then u choose if you want to get the sum
# of the list or if you want to remove the uneven numbers from the list
def create_list_and_sum_it_up():
    def sum_of_list(nl):
        return sum(nl)

    def remove_uneven(nl):
        return [i for i in nl if i % 2 == 0]

    num_list = []
    num = 0
    while num != "":
        num = input("Input num for list: ")
        try:
            int(num)
            num_list.append(int(num))
        except ValueError:
            break
    if len(num_list) > 0:
        option = int(input("If you want the sum of the list type 1 \nIf you want to remove all uneven numbers from the list type 2 \n"))

        if option == 1:
            print("Sum of the list is: ", sum_of_list(num_list))
        elif option == 2:
            print("The original list:", num_list,"list where uneven numbers have been removed:", remove_uneven(num_list))


# 5
def compare_pizza_prices():

    def pizza_cost_per_square_meter(diameter, price):
        a = round((m.pi*(diameter/2)**2) / 100, 2)
        cost_per_square_meter = round(price / a, 2)
        return cost_per_square_meter

    fd = int(input("Type first pizzas diameter: "))
    fc = int(input("Type first pizzas cost: "))
    sf = int(input("Type second pizzas diameter: "))
    sc = int(input("Type second pizzas cost: "))

    fp = {"name": "First pizza", "cost": pizza_cost_per_square_meter(fd, fc)}
    sp = {"name": "Second pizza", "cost": pizza_cost_per_square_meter(sf, sc)}
    w = fp["cost"] > sp["cost"] and sp["cost"] or fp["cost"]

    print("First pizza costs", fp["cost"], "euros per square meter")
    print("Second pizza costs", sp["cost"], "euros per square meter")
    print("That means", w, "is more worth the cost")


