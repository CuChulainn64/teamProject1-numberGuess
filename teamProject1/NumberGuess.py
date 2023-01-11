#The computer selects a random number in a range, and the
#player has to guess the number.  The player has “n” number of guesses, and the
#computer will give hints about the number as the user guesses.  Try and come up
#with your own implementation
import random
class NumGame:
    def __init__(self, rounds, min, max):
        self.numberRounds = rounds
        self.maxNumber = max
        self.minNumber = min
        self.__randomNumber = random.randint(min, max)
    
    def startGame(self):
        for i in range(1, self.numberRounds):
            if(self.playerGuess() == self.__randomNumber):
                self.gameOver("You Win")
            else:
                self.giveHint(self.previousGuess)
        self.gameOver(f"Sorry, the number was {self.__randomNumber}. You Lose")
    def playerguess(self):
        guess = input("Guess a number: ")
        self.previousGuess = int(guess)
        return guess
    def giveHint(self, num):
        if(num > self.__randomNumber):
            print("smaller")
        else:
            print("bigger")
    def gameOver(result):
        print(result)