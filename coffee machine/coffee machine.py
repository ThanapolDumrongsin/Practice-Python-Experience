from data import *
#MENU
# resources
water_left= resources['water']
milk_left = resources['milk']
coffee_left = resources['coffee']
# ask for coffee
while True :
    ask_coffee = input("Hello welcome to Coffee Machine, We have Espresso , Latte , Cappuccino. Please type in the menu.\n").lower()
    if ask_coffee == "off":
        print("Turn off")
        break
    elif ask_coffee not in (coffee for coffee in MENU) :
        print("Not in Menu")
        continue
    # Check for ingredient left in machine
    

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
    if bool(check_water) and bool(check_milk) and bool(check_coffee) :
        check_price = MENU[ask_coffee]['cost']
        
        while True:
            print(f"{ask_coffee} Price is {check_price}$.")
            ask_pennies = int(input("How many coin of Pennies (0.01 for each coin).\n"))
            ask_pennies = float(ask_pennies*0.01)
            print(f"Total money = {round(ask_pennies,2)}")
            
            ask_nickle = int(input("How many coin of Nickles(0.05 for each coin).\n"))
            ask_nickle = float(ask_nickle*0.05)
            print(f"Total money = {round(ask_pennies+ask_nickle,2)}")
            
            ask_dimes = int(input("How many coin of Dimes(0.1 for each coin).\n"))
            ask_dimes = float(ask_dimes*0.1)
            print(f"Total money = {round(ask_pennies+ask_nickle+ask_dimes,2)}")
            
            ask_quarter = int(input("How many coin of Quarters(0.25 for each coin).\n"))
            ask_quarter = float(ask_quarter*0.25)

            total_money = ask_pennies + ask_nickle + ask_dimes + ask_quarter
            calculate = total_money >= check_price
            if bool(calculate) :
                change = total_money - check_price
                break
            else :
                agian = input("Not enough money, Do you want to try agian or cancle. 'Y' for Yes 'anykey' for cancel.\n").lower()
                if agian == "y" :
                    continue
                else :
                    change = False
                    break 
    else :
        try_agian = input("Please try agian 'Y' for yes, 'anykey' for no.\n").lower()
        if try_agian == 'y' :
            continue
        else :
            break
    # serve coffee
    if change != False :
        print(f"\nThis is your {ask_coffee}, Please enjoy.")
        # give change to customer
        print(f"Your Change is {round(change,2)}$.\n")

    # check ingredient left
    print(f"\namount of water left = {water_left}ml.")
    print(f"amount of coffee left = {coffee_left}g.")
    print(f"amount of milk left = {milk_left}ml.\n")

    more_order = input("\nAny more order ? 'Y' for yes, 'anykey' for no.\n").lower()
    if more_order == 'y' :
        continue
    else :
        break
