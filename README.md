# Quiz Game

A multiple-choice quiz game written in Python that was created by object-oriented programming and a dictionary of questions pulled from an external source. This project was created to simulate an online quiz or trivia type of game. In this game, there are several questions along with their answers stored into a dictionary. If a player answers the questions correctly, they will gain a point, otherwise they will move onto the next question with no point. I wanted to see how I could incorporate "outside" data into my code with this project.

# Goal of my project:

The idea was to create an interactive text-based game that:
- Presents trivia questions while accepting user input. The user's score will be tracked as they answer the questions and listed as they continue onward.
- The score is presented in the format (# of Questions answered Correctly) / (# of Questions Presented to the user thus far).
- The person playing the game will be told whether or not their answer was correct right after they submit an input. The questions are in a True or False format.

# Core Logic:

- A `Question` class stores each question's text and correct answer.
- A `QuizBrain` class handles progression through the question list, including moving to the next question,
checking if the answer is correct or false, and determining whether or not the quiz has any remaining questions.
- The game checks the user's answers, updates the score, and moves to the next question until complete.
- Data.py holds all of the questions that the quiz has to offer, if one should choose to use their own questions, data.py must be replaced with
a custom Python file that has key-pairs of questions and answers.

# Data Handling:

- The question list was stored as a JSON/dictionary structure, this can be replaced with another question bank of the same format.
- My code can be adapted to pull data from an API or file should a user choose to customize their quiz questions.

# Concepts used:
- Simple classes and methods
- Loops and conditional logic
- Input/output in the console
- Modular design (question model, quiz logic, main script)
