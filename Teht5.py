import random

import random as r

# 1
def sum_of_dice():
    dice_amount = int(input("How many dice to roll: "))
    full = 0
    for dice in range(dice_amount):
        dice_roll = r.randint(1,6)
        full += dice_roll
    print(full)


# 2
def five_gratest():
    nums = []
    run = True
    while run:
        num = input("Input num: ")
        try:
            int(num)
            nums.append(int(num))
        except ValueError:
            run = False

    nums.sort(reverse=True)
    f = 5
    if len(nums) < 4:
        f = len(nums)

    for i in range(f):
        print(nums[i])


# 3
def prime_number():
    num = int(input("Give number: "))
    flag = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")





