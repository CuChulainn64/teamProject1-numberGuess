#The computer selects a random number in a range, and the
#player has to guess the number.  The player has “n” number of guesses, and the
#computer will give hints about the number as the user guesses.  Try and come up
#with your own implementation
import random
import yaml
import get_input
class NumGame:
    def __init__(self):
        self.getValues()
        self.__randomNumber = random.randint(self.min, self.max)
        self.startGame()
    
    def startGame(self):
        print("\n******************************************************************************")
        print("Welcome to the number guess game")
        
        
        for i in range(1, self.numberRounds+1):
            guess = self.playerGuess()
            if( guess == self.__randomNumber):
                result = f"You Win. It only took {i} guesses"
                break
            else:
                if(i < self.numberRounds):
                    self.giveHint(self.previousGuess)
                result = f"Sorry, the number was {self.__randomNumber}. You Lose"
        self.gameOver(result)
    def playerGuess(self):
        while True:
            guess = get_input.get_int("Guess an integer: ") 
            self.previousGuess = guess
            return guess
            
    
    def giveHint(self, num):
        if(num > self.__randomNumber):
            print("smaller")
        else:
            print("bigger")
            
    def gameOver(self, result):
        with open("Nuber guess log.txt", 'a') as file:
            file.write(yaml.dump(result) + '\n')
        print(result)
        print("******************************************************************************\n")
    def getValues(self):
        while True:
            try:
                self.numberRounds = get_input.get_int("Please enter the number of rounds: ", min = 1)
                self.min = get_input.get_int("Please enter the minumum value: ")
                self.max = get_input.get_int("Please enter the maximum value: ", min = self.min + 1)
            except:
                pass
            else:
                break