from data import *
#MENU
# resources

# ask for coffee
ask_coffee = input("Hello welcome to Coffee Machine, We have Espresso , Latte , Cappuccino. Please type in the menu.\n").lower()

# Check for ingredient left in machine
water_left= resources['water']
milk_left = resources['milk']
coffee_left = resources['coffee']

# check for menu needed
for _ in MENU :
    water_need = MENU[ask_coffee]['ingredients']['water']
    cofee_need = MENU[ask_coffee]['ingredients']['coffee']
    try :
        milk_need = MENU[ask_coffee]['ingredients']['milk']
    except :
        milk_need = 0

#compare ingredient
check_water = water_left > water_need
if bool(check_water) :
    water_left -= water_need
else :
    print("Sorry we run out of Water")

check_milk = milk_left > milk_need
if bool(check_milk) :
    milk_left -= milk_need
else :
    print("Sorry we ran out of Milk")

check_coffee = coffee_left > cofee_need
if bool(check_coffee) :
    coffee_left -= cofee_need
else :
    print("Sorry we ran out of Coffee")
# ask for coin
# serve coffee
# give change to customer