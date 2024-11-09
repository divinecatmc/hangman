import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
app = Flask(__name__)
#from helper import apology
app.config["TEMPLATES_AUTO_RELOAD"] = True

# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

db = SQL("sqlite:///words.db")


# pulls out a random word
random = db.execute("SELECT word FROM dict ORDER BY RANDOM() LIMIT 1")

word = random[0]["word"]

word = word.replace("'", "")

# print(word)

# print(random)

db.execute("DELETE FROM game")
db.execute("DELETE FROM guess")

# how many lives (subject to change)
lives = 6

# @app.route("/", methods=["GET", "POST"])
# def main():
    
#     if request.method == "GET":
#         print("hello")
        
    
#     return render_template("menu.html")
    


@app.route("/", methods=["GET", "POST"])
def menu():
    
    gues = 6   
        
    wrd = word
    
    counter = 0
    
    # separate path for post at first
    if request.method == "POST":
        
        single = request.form.get("single")
        
        # update letter to true where it exists if correct
        db.execute("UPDATE game SET guessed = TRUE WHERE letter = ?", single)
        
        if len(db.execute("SELECT letter FROM game WHERE letter = ?", single)) == 0:
            
            # store incorrect guesses
            db.execute("INSERT INTO guess (letter) VALUES (?)", single)

    # iterate through letters of word    
    for i in range(len(word)):
        
        #print("_", end=" ")
        
        #print(word[i])
        
        #print(word)
        
        # wrd = wrd.replace(word[i], "_")
        
        if request.method == "POST":
            
            # find all unique correct letters
            letter = db.execute("SELECT DISTINCT letter FROM game WHERE guessed = 1")
            
            for j in range(len(letter)):
                
                if letter[j]["letter"] == word[i]:
                    
                    # replace underscore with placeholder
                    wrd = wrd.replace(letter[j]["letter"], "#")
                    
                    # up the counter
                    counter += 1
            
        else:
            
            # implement letter into game database
            db.execute("INSERT INTO game (letter) VALUES (?)", word[i])
        
        # change all non-guessed letters into underscores
        wrd = wrd.replace(word[i], "_")
        
        # replace placeholder with correct letter
        wrd = wrd.replace("#", word[i])
    
    guess = db.execute("SELECT DISTINCT letter FROM guess")   
    
    
    # use the difficulty from earlier
    
    
    # set up lives
    lives = (8 - len(guess))
    
    # endings
    if lives == 0:
        return render_template("youlose.html", word=word)
        
    if wrd == word:
        return render_template("youwin.html", word=word)
    
        
    return render_template("hangman.html", word=word, wrd=wrd, guess=guess, lives=lives)