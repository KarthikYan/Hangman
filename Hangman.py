import random
import json
import pandas as pd

df = pd.DataFrame(columns=['Name','Score'])

class player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def hangman():
    
    f = open('words.json',) 
    data = json.load(f) 
    words = data['words']
    f.close()
    name = input("What is your name? ")
    p = player(name,0)
    print("Good Luck ! ", name)

    word = random.choice(words).lower()

    print("Guess the characters")

    guesses = ''
    wrongGuesses = ''

    turns = 5
    while turns > 0:
    
        failed = 0
        current_guess = ''
        for char in word:
            if char in guesses:
                current_guess += char
                
            else:
                current_guess += "-"
                failed += 1
        print("Current Guess:", current_guess) 	    

        if failed == 0:
            p.score += 10
            print("You Win")
            print("The word is: ", word)
            return p
        guess = input("guess a character:").lower()
        guesses += guess
        
        if guess not in word:		        
        
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose, the word is ", word)
                return p
while True:
        playerDetails = hangman()
        
        if playerDetails.name in df.values:
            df.loc[df.Name == playerDetails.name, 'Score']+=10
        else:
            df = df.append({'Name' : playerDetails.name, 'Score' : playerDetails.score} , ignore_index=True)
        df = df.sort_values('Score', ascending=False)
        print(df.head(10).to_string(index=False))
        restart = input('do you want to restart Y/N?').upper()
        if restart == 'N':
            break
        elif restart == 'Y':
            continue

