from requests import get
from random import shuffle
from time import sleep
from os import system


def play_game(): 
    while True:
        choice = input("Wanna play more (yes, no)? ")
        if choice == "yes": 
            data = choosing_question_type()
            preform_quiz(data)

        else: 
            system("clear")            
            print("Goodbye !")
            break

        return 0
        
        
CORRECT_ANSWERS = 0 


def loading_questions(amount, catagory, difficulty): 
    data = get("https://opentdb.com/api.php?amount=" + amount + "&category=" + catagory +  "&difficulty=" +  difficulty + "&type=multiple")
    data = data.json()
    data = data['results']
   
    return data


def choosing_question_type(): 
    catagory = {
                20: "Mythology",
                21: "Sports",
                22: "Geography",
                23: "History",
                24: "Politics",
                25: "Art",
                26: "Celebrities",
                27: "Animals",
                28: "Vehicles", 
            } 
    
    for i,j in catagory.items(): 
        print(i , j)
        
    Catagory = input("\nEnter your choise as the number : ")
    system("clear")
    Amount = input("Enter amount of questions : ")
    system("clear")
    Difficulty = input("Enter your desired difficulty (easy, medium, hard) : ")
    system("clear")
    
    data = loading_questions(Amount, Catagory, Difficulty)
    
    return data 


def preform_quiz(data): 
    
    global CORRECT_ANSWERS
    
    for q in data: 
        print(q['question']) 
        answers = []

        answers.append(q['correct_answer'])
        
        for i in q['incorrect_answers']: 
            answers.append(i)
            
        shuffle(answers)
        
        for i in answers: 
            print(i)
        
        choice = input("\nEnter your answer please : ")
        
        if choice.lower() == q['correct_answer'].lower(): 
            print("Correct answer !")
            CORRECT_ANSWERS += 1
        else: 
            print("Wrong answer !")
            print("Correct answer is : " + q['correct_answer'])
        sleep(2)
        system("clear")
        


if __name__ == "__main__": 
    data = choosing_question_type()
    preform_quiz(data)
    play_game()