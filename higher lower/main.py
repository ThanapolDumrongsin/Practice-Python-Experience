from art import *
from data import *
import random
import os



# random data
def start():
    random_people_for_player = random.choice(data)

    random_people_for_guess = random.choice(data)
    # random agian if duplicate
    while random_people_for_guess == random_people_for_player :
        random_people_for_guess = random.choice(data)

# battle
    player = random_people_for_player
    player_name = player['name']
    guess = random_people_for_guess
    guess_name = guess['name']
    print(f"\n\n{player_name}")
    print(vs)
    print(guess_name)
    
# check answer
    
    score = 0
    while True:
        #compare result
        result = player['follower_count'] > guess['follower_count']
        result = bool(result)
        # input the answer
        answer = input("'H' for higher , 'L' for lower.\n").upper()
        while True :
            if answer == "H" :
                answer = True
                print(player)
                print(guess)
                break
            elif answer == "L" :
                answer = False
                print(player)
                print(guess)
                break
            else :
                print("Please type 'H' or 'L'")
                continue

        # if win
        if answer == result :
            score += 1
            
            os.system('cls')
            print("\nYou win.")
            print(f"Your score is {score}.\n\n")
            # change player to guess
            player = guess
            guess = random.choice(data)
            # prevent from duplicate
            while player == guess :
                guess = random.choice(data)
            # play agian
            print(player["name"])
            print(vs)
            print(f"{guess['name']}\n")
            continue
            
        # if lose
        else :
            print("You lose.")
            print(f"Your score is {score}.")
            break




while True :
    print(logo)
    welcome = input("\n\nAre you ready to play a game 'Y' for yes 'N' for no.\n").upper()
    
    if welcome == "Y" :
        os.system('cls')
        start()
        
    elif welcome == "N":
        print("Good bye.")
        break
    else :
        continue