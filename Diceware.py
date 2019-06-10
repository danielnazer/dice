#Diceware

import random

#choose a number of die

number_of_die = int(input("How many die do you wish to roll?: "))

#chose the number of sides

number_of_sides = int(input("How many sides should the die have?: "))

def dice(n):
    print (random.randrange(1,n))

for i in range (0, number_of_die):
    dice(number_of_sides)
