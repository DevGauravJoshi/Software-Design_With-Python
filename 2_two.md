# Guessing Game
This Python program is a simple guessing game where the user has to guess a number between a certain range. The program has two different methods to play the game:

## Method 1 - guesss()
The first method uses a while loop to repeatedly prompt the user to guess a number until the correct number is guessed. The program initializes the correct number to be guessed and the range of the number to be between 0 and 100. If the user's guess is under the correct number, the program will print "Your guess was under". If the user's guess is over the correct number, the program will print "Your guess was over". When the correct number is guessed, the program will print "You guessed it in X guesses", where X is the number of guesses it took to correctly guess the number.

## Method 2 - Guessnumber class
The second method defines a class called Guessnumber that takes in the number to be guessed and the range of the number as parameters. This class has three methods: get_guess(), valid_number(), and play(). The get_guess() method prompts the user to enter a number within the specified range until a valid number is entered. The valid_number() method checks whether the input is a valid number within the specified range. The play() method uses a while loop to repeatedly prompt the user to guess a number until the correct number is guessed. When the correct number is guessed, the program will print "You guessed it in X guesses", where X is the number of guesses it took to correctly guess the number.

Both methods allow the user to input a range of numbers to guess from, which makes the game more customizable. However, the second method is more object-oriented, allowing the user to create multiple instances of the guessing game with different parameters.
