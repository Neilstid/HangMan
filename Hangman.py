#importing the time module
import time
import random
from datetime import datetime
import os
import termios, sys
#import termios, TERMIOS, sys

#____________________________________________________________________________________________________________________________________________

#return the key that have been pressed
TERMIOS = termios
def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
                c = os.read(fd, 1)
        finally:
                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

#____________________________________________________________________________________________________________________________________________

#modify the file parameter
def ModifyParameter(line, value):
    FileReading = open("parameter.txt", "r")#read the file
    Lines = FileReading.readlines()#get a copy of the file
    Lines[line] = value#modify the value wanted
    FileReading.close#close file
    
    FileWritting = open("parameter.txt", "w")#rewrite the file
    for x in Lines:#for each line
        FileWritting.write(str(x))#paste the copy into the file
        FileWritting.write("\n")
    FileWritting.close#close the file
    
#____________________________________________________________________________________________________________________________________________

#return the language
def Getlanguage():
    File = open("parameter.txt", "r")#open file in reading mode
    Lines = File.readlines()#get the content of the file line by line
    File.close()#close it
 
    #return the language 
    if int(Lines[0]) == 1:
        return "English"
    elif int(Lines[0]) == 2:
        return "French"
    elif int(Lines[0]) == 3:
        return "German"
    elif int(Lines[0]) == 4:
        return "Spanish"
    elif int(Lines[0]) == 5:
        return "Dutch"
    else :
        return "English"

#____________________________________________________________________________________________________________________________________________

#get the number of turn
def Getturns():
    File = open("parameter.txt", "r")#open file in reading mode
    Lines = File.readlines()
    File.close()
    return int(Lines[1])#return the number of turn
    
#____________________________________________________________________________________________________________________________________________

#modify the numbers if turns
def Parameter_Turns(): 
    turns = int(input("Number of turns : "))#ask the number of turn
    ModifyParameter(1, turns)#modify the value in the parameter file
    return turns

#____________________________________________________________________________________________________________________________________________

#Modify language
def Parameter_Language():
    
    #Choice of language
    print("Language of the word to guess")
    print("[1] : English")
    print("[2] : French")
    print("[3] : German")
    print("[4] : Spanish")
    print("[5] : Dutch")
    
    #Get the choice of user
    choice = input("Choice : ")
    
    if choice == "1" :
        language = "English"#set the language to english
        ModifyParameter(0, 1)#modify the value in the parameter file
    elif choice == "2" :
        language = "French"  #set the language to french
        ModifyParameter(0, 2)#modify the value in the parameter file
    elif choice == "3" :
        language = "German"  #set the language to german
        ModifyParameter(0, 3)#modify the value in the parameter file
    elif choice == "4" :
        language = "Spanish"  #set the language to spanish
        ModifyParameter(0, 4)#modify the value in the parameter file
    elif choice == "5" :
        language = "Dutch"  #set the language to dutch
        ModifyParameter(0, 5)#modify the value in the parameter file
    else : 
        language = "English"
    return language

#____________________________________________________________________________________________________________________________________________

#get a random word
def GetWord():
	#Open file in reading mode
    File = open(languageWord.get(language), "r")
    
    #read a random word   
    Lines = File.readlines()
    random.seed(datetime.now())#define a seed
    NumOfLine = random.randint(0, len(Lines)-1)#generate a random number
    
    WordChosen = Lines[NumOfLine].strip()#delete space to the chosen word
    
    File.close()
    
    return WordChosen

#____________________________________________________________________________________________________________________________________________

def WinningMessage():
    Message = ["\nYou won \U0001F525","\nGG bro \U0001F44A, you have the win", "\n\U0001F387 Wow you have win \U0001F387", "You rocks men \U0001F919"]
    Length = len(Message) - 1
    random.seed(datetime.now())#define a seed
    MessageToSend = random.randint(0, Length)#generate a random number
    print(Message[MessageToSend])

#____________________________________________________________________________________________________________________________________________

def Hangman(turns):
    print("Start guessing...")

    #here we set the word
    word = GetWord()
    #creates an variable with an empty value
    guesses = ''
    #create variable with the letter already uses
    LetterUsed = []

    # Create a while loop
    #check if the turns are more than zero
    while turns > 0:         

        # make a counter that starts with zero
        failed = 0           

        print("Word to guess : ", end = "")
        # for every character in secret_word    
        for char in word:      
        # see if the character is in the players guess
            if char in guesses:    
            # print then out the character
                print(char, end =""),    
            else:
            # if not found, print a dash
                print("_", end =" "),     
            # and increase the failed counter with one
                failed += 1    

        # if failed is equal to zero
        # print You Won
        if failed == 0:
            os.system('clear')        
            WinningMessage() 
            return 1
        # exit the script
            break              
        print()

        # ask the user go guess a character
        guess = input("guess a character:") 
        #set to lowercase
        guess.lower()
        # set the players guess to guesses
        guesses += guess                 

        #clear terminal
        os.system('clear') 

        # if the guess is not found in the secret word
        if guess not in word and guess not in LetterUsed:  
        # turns counter decreases with 1 (now 9)
            turns -= 1        
        # print wrong
            print("Wrong")    
        # how many turns are left
            print("You have", + turns, 'more guesses')
        # Add the last enter in the letter use
            LetterUsed.append(guess)       
        # if the turns are equal to zero
            if turns == 0:           
            # print "You Lose"
                print("You Lose \U0001F480, the word was " + word) 
                return 0
        elif guess in LetterUsed :
            print("The letter " + guess + " has already been tried. You still have", + turns , "more guesses")          


   
#-----------------------------------------------------------------------------------------------------------------------------------------------

#set the path for the different language 
languageWord = {"English" : "list_english.txt", "French" : "liste_francais.txt", "German" : "list_deutsch.txt", "Spanish" : "list_espanol.txt", "Dutch" : "list_nederlands.txt"}
#define the actual language
language = Getlanguage()
print("The language was set to " + language)
#determine the number of turns
turns = Getturns()

#welcoming the user
nameTemp = input("What is your name? ")
#set the first letter in uppercase and the other lower
name = nameTemp[0].upper() + nameTemp[1:].lower()

#check if the user want to modify the language or the number of turns
if name == "Language" :
    name = "Admin"#set the name to admin
    language = Parameter_Language()#get the language parameter
elif name == "Turns" :
    name = "Admin"#set the name to admin
    turns = Parameter_Turns()#get the number of turn parameter

print("Hello, " + name + "\U0001F44B")

print("Press any key to start a new game " + name)
KeyPressed = getkey()#wait for a key to be pressed

NewGame = 1
game = 0
win = 0
while(NewGame == 1) :
    game+=1
    score = Hangman(turns)#run the game
    win += score#update the score
    try :
        NewGame = int(input("Press [1] for a new game \n"))#ask for a new game
    except ValueError:
        break
print("You have", + win , "win \U0001F396 in", + game , "games")#print the score

