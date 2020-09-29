"""
Xinyi Wu
Rock, Paper, Scissors, Lizard, Spock (RPSL)
The program randomly generates a number 1, 2, 3, 4, or 5 representing Rock, Paper, Scissors, Lizard, and Spock. The program then prompts user to enter a number 1, 2, 3, 4, or 5 and decides who wins, user or the computer.
"""

import random


def getName(value):

    value = str(value)
    if value == "1":
        return "Rock"
    elif value == '2':
        return "Paper"
    elif value == '3':
        return "Scissors"
    elif value == "4":
        return "Lizard"
    elif value == "5":
        return "Spock"
    else:
        return "Undefined"

def getComputer():
    x = random.randint(1,5)
    result = getName(x)
    return result
   
def getHuman():
    num = int(input("Entry:"))
    result = getName(num)
    return result


def getMessage(winner, loser):
    
    if loser == "U":
        print("The computer is "+str(winner)+". You are Undefined. Invalid game. Outcome is undefined.")

    elif winner == "C" and loser == "Paper":
        print("The computer is Scissors. You are Paper. Scissors cut Paper. The computer win.")
    elif winner =="H" and loser =="Paper":
        print("The computer is Paper. You are Scissors. Scissors cut Paper. The human wins.")
        
    elif winner == "C" and loser == "Rock":
        print("The computer is Paper. You are Rock. Paper covers Rock. The computer win.")
    elif winner == "H" and loser == "Rock":
        print("The computer is Rock. You are Paper. Paper covers Rock. The human win.")        
        
    elif winner == "C" and loser == "Lizard":
        print("The computer is Rock. You are Lizard. Rock crushes Lizard. The computer win.")
    elif winner == "H" and loser == "Lizard":
        print("The computer is Lizard. You are Rock. Rock crushes Lizard. The human win.")    
        
    elif  winner == "C" and loser == "Spock":
        print("The computer is Lizard. You are Spock. Lizard poisons Spock. The computer win.")
    elif  winner == "H" and loser == "Spock":
        print("The computer is Spock. You are Lizard. Lizard poisons Spock. The human win.")    
    
    elif winner == "C" and loser == "Scissors":
        print("The computer is Spock. You are Scissors. Spock smashes Scissors. The computer win.")
    elif winner == "H" and loser == "Scissors":
        print("The computer is Scissors. You are Spock. Spock smashes Scissors. The human win.")          
        
    elif winner == "C" and loser == "Lizard":
        print("The computer is Scissors. You are Lizard. Scissors decapitate Lizard. The computer win.")
    elif winner == "H" and loser == "Lizard":
        print("The computer is Lizard. You are Scissors. Scissors decapitate Lizard. The human win.")           
    
    elif winner == "C" and loser == "Paper":
        print("The computer is Scissors. You are Paper. Lizard eats Paper. The computer win.")
    elif winner == "H" and loser == "Paper":
        print("The computer is Paper. You are Scissors. Lizard eats Paper. The human win.")          
        
    elif winner == "C" and loser == "Spock":
        print("The computer is Paper. You are Spock. Paper disproves Spock. The computer win.")
    elif winner == "H" and loser == "Spock":
        print("The computer is Spock. You are Paper. Paper disproves Spock. The human win.")        
        
    elif winner == "C" and loser == "Rock" :
        print("The computer is Spock. You are Spock. Spock vaporizes Rock. The computer win.")
    elif winner == "H" and loser == "Rock" :
        print("The computer is Rock. You are Rock. Spock vaporizes Rock. The human win.")       
        
    elif winner == "C" and loser == "Scissors" :
        print("The computer is Rock. You are Scissors. Rock crushes Scissors. The computer win.")
    elif winner == "H" and loser == "Scissors" :
        print("The computer is Scissors. You are Rock. Rock crushes Scissors. The human win.")        
        
    elif winner == "Rock" and loser == "Rock" :
        print("The computer is Rock. You are Rock. Draw. Neither win.")
        
    elif winner == "Scissors" and loser == "Scissors" :
        print("The computer is Scissors. You are Scissors. Draw. Neither win.")
        
    elif winner == "Lizard" and loser == "Lizard" :
        print("The computer is Lizard. You are Lizard. Draw. Neither win.")
        
    elif winner == "Paper" and loser == "Paper" :
        print("The computer is Paper. You are Paper. Draw. Neither win.")
        
    elif winner == "Spock" and loser == "Spock" :
        print("The computer is Spock. You are Spock. Draw. Neither win.")
        
    else:
        print("Invalid Game")
        
def playGame(computer, human):

    c = "C"
    h = "H"
    if human == "Undefined":
        winner = computer
        loser = "U"
        return getMessage(winner, loser)
    
    elif computer == "Scissors" and human =="Paper":
        # winner parameter => c or h
        # loser parameter => name of thing
        winner = c
        loser = "Paper"
        return getMessage(winner, loser)
       
    elif human =="Scissors" and computer =="Paper":
        winner = h
        loser = "Paper"
        return getMessage(winner, loser)       

    elif computer == "Paper" and human =="Rock":
        winner = c
        loser = "Rock"
        return getMessage(winner, loser)
       
    elif human =="Paper" and computer =="Rock": 
        winner = h
        loser = "Rock"
        return getMessage(winner, loser)        
 
    elif computer == "Rock" and human =="Lizard":
        winner = c
        loser = "Lizard"
        return getMessage(winner, loser)           
    elif human =="Rock" and computer =="Liazrd":  
        winner = h
        loser = "Lizard" 
        return getMessage(winner, loser) 

    elif computer == "Lizard" and human =="Spock":
        winner = c
        loser = "Spock" 
        return getMessage(winner, loser)         
    elif human =="Lizard" and computer =="Spock": 
        winner = h
        loser = "Spock" 
        return getMessage(winner, loser)         

    elif computer == "Spock" and human =="Scissors":
        winner = c
        loser = "Scissors" 
        return getMessage(winner, loser)         
    elif human =="Spock" and computer =="Scissors":   
        winner = h
        loser = "Scissors" 
        return getMessage(winner, loser)            
       
    elif computer == "Scissors" and human =="Lizard":
        winner = c
        loser = "Lizard" 
        return getMessage(winner, loser)            
    elif human =="Scissors" and computer =="Lizard":
        winner = h
        loser = "Lizard" 
        return getMessage(winner, loser)              
       
    elif computer == "Lizard" and human =="Paper":
        winner = c
        loser = "Paper" 
        return getMessage(winner, loser)              
    elif human =="Lizard" and computer =="Paper": 
        winner = h
        loser = "Paper" 
        return getMessage(winner, loser)         
       
    elif computer == "Paper" and human =="Spock":
        winner = c
        loser = "Spock" 
        return getMessage(winner, loser)         
    elif human =="Paper" and computer =="Spock":
        winner = h
        loser = "Spock" 
        return getMessage(winner, loser)         
 
    elif computer == "Spock" and human =="Rock":
        winner = s
        loser = "Rock" 
        return getMessage(winner, loser)         
    elif human =="Spock" and computer =="Rock": 
        winner = h
        loser = "Rock" 
        return getMessage(winner, loser)          
       
    elif computer == "Rock" and human =="Scissors":
        winner = c
        loser = "Scissors" 
        return getMessage(winner, loser)          
    
    elif human =="Rock" and computer =="Scissors": 
        winner = h
        loser = "Scissors" 
        return getMessage(winner, loser) 
    
       
    elif human == computer:
        winner = human
        loser = computer
        return getMessage(winner,loser)     
    





def main():
    print("Enter one of the following:")
    print("       1)Rock")
    print("       2)Paper")
    print("       3)Scissors")
    print("       4)Lizard")
    print("       5)Spock")  
   
    computer = getComputer()
    human = getHuman()
   
    playGame(computer, human)



main()
