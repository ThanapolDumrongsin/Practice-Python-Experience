from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menu_for_order = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# welcome
# ask for menu
while True :
    while True :
        welcome = input(f"Hello welcome to coffee shop, We have {menu_for_order}. \nWhat is your order, Please type coffee name.\n ").lower()
        customer_order = menu.find_drink(welcome)
        if bool(customer_order) :
            cost = customer_order.cost
            break
        else :
            continue

    # check ingredient
    check_ingredient = coffee_maker.is_resource_sufficient(customer_order)
    print(f"{welcome} cost is {cost}")
    if check_ingredient :
        # coin insert
        # calculate change
        change_calculate = money_machine.make_payment(cost)
        if change_calculate :   
            # compare ingredient and subtract
            # serve
            make_coffee = coffee_maker.make_coffee(customer_order)
    # report
    print("")
    coffee_report = coffee_maker.report()
    
    # more order ?
    order_agian = input("Do you want to order agian. 'Y' for yes 'anykey' for no\n").lower()
    if order_agian == 'y' :
        continue
    else :
        print("Thank you, have a nice day.")
        print(f" Profit = {money_machine.profit}$.")
        break




