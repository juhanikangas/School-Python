import random as r


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


# 3 Asks user for number to put in a list then adds them up
def create_list_and_sum_it_up():
    def sum_of_list(nl):
        return sum(nl)
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
        print("Sum of the list is: ", sum_of_list(num_list))


create_list_and_sum_it_up()
