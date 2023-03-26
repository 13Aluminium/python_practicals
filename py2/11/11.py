import random

def guess_number():
    # generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # initialize guess to an invalid value to enter the loop
    guess = 0
    
    # loop until the guess is correct
    while guess != secret_number:
        try:
            # ask user to guess the number
            guess = int(input("Guess a number between 1 and 100: "))
            
            # check if guess is out of range
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100")
                
            
            # check if guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the number!")
            elif guess<secret_number:
                print("aim higher")
            else:
                print("aim lower")
                                    
                
        except ValueError as e:
            # handle invalid input from user
            print("Invalid input:", e)

if __name__ == '__main__':
    guess_number()
