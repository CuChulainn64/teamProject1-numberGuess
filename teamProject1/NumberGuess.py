#The computer selects a random number in a range, and the
#player has to guess the number.  The player has “n” number of guesses, and the
#computer will give hints about the number as the user guesses.  Try and come up
#with your own implementation
import random
import yaml
class NumGame:
    def __init__(self, rounds, min, max):
        try:
            self.numberRounds = rounds
            self.maxNumber = max
            self.minNumber = min
            self.__randomNumber = random.randint(min, max)
        except ValueError:
            print("invalid starting values")
        self.__startGame()
    
    def __startGame(self):
        for i in range(1, self.numberRounds+1):
            guess = self.playerGuess()
            if( guess == self.__randomNumber):
                result = f"You Win. It only took {i} guesses"
                break
            else:
                self.giveHint(self.previousGuess)
                result = f"Sorry, the number was {self.__randomNumber}. You Lose"
        self.gameOver(result)
    def playerGuess(self):
        guess = input("Guess a number: ")
        self.previousGuess = int(guess)
        return int(guess)
    def giveHint(self, num):
        if(num > self.__randomNumber):
            print("smaller")
        else:
            print("bigger")
    def gameOver(self, result):
        with open("Nuber guess log.txt", 'a') as file:
            file.write(yaml.dump(result) + '\n')
        print(result)
        
NumGame(1, 1, 1)