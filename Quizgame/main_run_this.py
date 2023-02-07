from data import *
import os
data = DATA()
score = 0
# random question and answer
while True :
    os.system('cls')
    print(data.logo)
    print(f"Your current score is {score}")
    question = data.random_question()
    question_part = question[0]['text']
    question_answer = (question[0]['answer']).lower()
    print(question_part)

    # let the guest guess answer
    # check answer
    # score 
    check_answer = DATA.guest_answer(question_answer  , score)
# continue
    if check_answer == False :
        print("See you agian !")
        break
    else :
        score += 1
        play_more = input("Do you want to continue ? 'Y' for yes 'anykey' for no.\n").lower()
        if play_more == 'y' :
            os.system('cls')
            continue
        
        else :
            print("Good bye.\n")
            break