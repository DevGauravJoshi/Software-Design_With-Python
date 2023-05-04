# Method 1

def guesss():
    guess = 1
    correct_num = 45
    range_num = 101
    while True:
        num = int(input(f"Please guess the number (between 0- {range_num}): "))

        if num < correct_num:
            print("Your guess was under")
        elif num > correct_num:
            print("Your guess was over")
        else:
            break

        guess += 1
    print(f"You guessed it in {guess} guessess")


# guesss()

# Method 2


class Guessnumber:

    def __init__(self, number, mn=0, max=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = max

    def get_guess(self):
        guess = input(f"Please enter a number ({self.min} - {self.max}): ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False

        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("You guess was under")
            elif guess > self.number:
                print("Your guess was over.")
            else:
                break

        print(f"You guesses it in {self.guesses} guesses.")


game = Guessnumber(56, 0, 100)
game.play()
