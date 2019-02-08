from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import random
import math

@app.route('/')
def main():
    
    return render_template("rps.html")

@app.route("/process", methods=["POST"])
def process():
    print(request.form["player_choice"])
    player_choice = request.form["player_choice"]
    computer = math.floor(random.random() * 3)
    computer_choice = ''
    if computer == 0:
        computer_choice = "rock"
    if computer == 1:
        computer_choice = "paper"
    if computer == 2:
        computer_choice = "scissors"
    choice = request.form["player_choice"]
    outcome = ''
    if player_choice == computer_choice:
        outcome = "It's a draw!"
    if player_choice == "rock":
        if computer_choice == "paper":
            outcome = "You Lose!"
        if computer_choice == "scissors":
            outcome = "You Win!"
    if player_choice == "paper":
        if computer_choice == "rock":
            outcome = "You win!"
        if computer_choice == "scissors":
            outcome = "You lose!"
    if player_choice == "scissors":
        if computer_choice == "rock":
            outcome = "You Lose!"
        if computer_choice == "paper":
            outcome = "You Win!"


    return render_template("rps.html", player_choice = player_choice, computer_choice=computer_choice, outcome = outcome)





if __name__ == "__main__":
    app.run(debug=True)
