# Program Goal
The program's goal is to print a list of words delimited by commas.

# Input
The input to the program is a list of words.

```
list_of_words = ["hello", "yes", "goodbye", "last"]
```

Output
The output of the program is a string containing the words from the list separated by commas.

Methods
The program provides three different methods to achieve the program goal:

## Method 1
The first method sortt() uses a for loop to iterate over the words in the list. It checks if the current word is the last word in the list. If it is not, it prints the word followed by a comma. If it is the last word, it prints the word without the comma.

## Method 2
The second method sortt2() uses the join() method to concatenate the words in the list with a comma delimiter.

## Method 3
The third method sortt3() is similar to the second method but uses a constant variable to hold the delimiter string.
