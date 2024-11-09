# HANGMAN
#### Video Demo:  https://www.youtube.com/watch?v=t_ssJlrUO4M
#### Description: 
For my final project in the CS50x curriculum, I decided to implement the game of hangman using flask, python, and html. In applications.py, one can see the python script for the game, which includes comments detailing the steps of the code. 
In words.db, one can see a list of all of the words in a dictionary, all of the letters in a word, and all of the incorrect guesses the player has made. 
In the teplates, there are many html templates, including the main hangman file, a layout that may have been inspired by finance, and files for winning and losing. 
The game itself is pretty standard for hangman -- there are several underscores to represent each letter, and the player's goal is to correctly guess the name of the word within the alotted guesses. 
If the player guesses a wrong letter, the letter in question will be placed into the wrong letters section, and the alotted guesses will go down by 1 point. 
I was not able to program a dynamic stick figure to appear on screen with each incorrect guess, but instead, there is a number that represents lives. 
Once said number drops to 0, the game is considered over, and the player is sent to a different html. Similarly, winning sends the player to an html file for winners. 

From a technical perspective, the program recieves a letter input (the guess), and attempts to iterate through the entire word, looking for instances of said letter. 
Once it has found an occurance, the program replaces the letter spot with a placeholder, to signify that it has been found. If no occurrance is found, the letter is added to a database for incorrect guesses. 
In the first run, of course, there are no letters, so the program converts all of the letters into underscores. The program also puts each letter of the word into a database for future reference. 
The word itself is chosen from a dictionary sqlite database, one which includes all of the words in the english dictionary. This is to ensure that each game is unique, to a certain extent.
Aside from that, there are some other details and ideas that I had for this project. The first of these is the difficulty option. This would've included an option to select the amount of words in the mystery section, as well as the amount of guesses.
Easy difficulty would have had 8 guesses and 1 word to be guessed, medium or normal difficulty would've had 6 guesses and 1 or 2 words to be guessed, and difficult or hard difficulty would've had 4 guesses and 4 words. 
In the end, the idea was scrapped, as it was unnecessary and would take too much time to implement into the program. In the future if I choose to continue this project, I might, on my own, incorporate an actual stick figure to be drawn on screen, just like an actual game of hangman.
There is not much else that is worthy of note to mention here, only tiny details about the code that I changed.

This has been Hangman, and thank you for an amazing course!
\-- Devin
