import random
import time

def again():
    repeat = input("Would you like to ask another question? (y/n): ").lower()
    if repeat == "y":
        magic_eight_ball()

        
def magic_eight_ball():
    response = ["Not likely.", "That's quite possible.", "Who knows.", "What kind of question is that?", "No."]
    input("What is your question?: ")
    print("Hold up...")
    time.sleep(3)
    print(random.choice(response))
    time.sleep(3)
    again()





    
    


magic_eight_ball()
