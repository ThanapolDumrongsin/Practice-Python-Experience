import random
class DATA :
    def __init__(self):
        self.question_data = [
        {"text": "A slug's blood is green.", "answer": "True"},
        {"text": "The loudest animal is the African Elephant.", "answer": "False"},
        {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
        {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
        {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
        {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
        {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
        {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
        {"text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
        {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
        {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
        ]
        self.logo = """.___________..______       __    __   _______      ______   .______          _______    ___       __          _______. _______    
|           ||   _  \     |  |  |  | |   ____|    /  __  \  |   _  \        |   ____|  /   \     |  |        /       ||   ____|   
`---|  |----`|  |_)  |    |  |  |  | |  |__      |  |  |  | |  |_)  |       |  |__    /  ^  \    |  |       |   (----`|  |__      
    |  |     |      /     |  |  |  | |   __|     |  |  |  | |      /        |   __|  /  /_\  \   |  |        \   \    |   __|     
    |  |     |  |\  \----.|  `--'  | |  |____    |  `--'  | |  |\  \----.   |  |    /  _____  \  |  `----.----)   |   |  |____ __ 
    |__|     | _| `._____| \______/  |_______|    \______/  | _| `._____|   |__|   /__/     \__\ |_______|_______/    |_______(__)
    """
    def random_question(self):
        question = random.choices(self.question_data)
        return question

    def guest_answer(question_answer, score):
        while True :
            guest_answer = input("What is your answer 'True' or 'False'.\n").lower()
            if question_answer == guest_answer :
                
                print("That is correct!")
                print(f"Your score is {score+1}")
                return True
                
            else :
                print("That is incorrect")
                print(f"Your score is {score+1}")
                return False
                

        
        
        