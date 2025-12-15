🧠 Day 17 – Quiz Game Project
📌 Project Overview

This project is a console-based Quiz Game built using Object-Oriented Programming (OOP) in Python.
The quiz asks True/False questions, checks user answers, and keeps track of the score.

This project focuses on:

Classes & Objects

Methods & attributes

Lists of custom objects

User input handling

Game flow logic

🗂 Project Structure
day-17-quiz-game/
│
├── main.py
├── question_model.py
├── data.py
├── quiz_brain.py
└── README.md

📄 File Explanation
main.py

Entry point of the program

Creates question objects

Starts the quiz loop

question_model.py

Contains the Question class

Stores question text and correct answer

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

data.py

Holds quiz questions in dictionary format

question_data = [
    {"text": "The sky is blue.", "answer": "True"},
    {"text": "2 + 2 equals 5.", "answer": "False"}
]

quiz_brain.py

Contains the main quiz logic

Controls question flow, scoring, and answer checking

Key responsibilities:

Display questions

Collect user answers

Check correctness

Track score

Determine when quiz ends

▶️ How the Quiz Works

Questions are loaded from data.py

Each question is converted into a Question object

QuizBrain manages:

Current question number

Correct answer checking

User score

Quiz continues until all questions are answered

Final score is displayed

🧪 Sample Output
Q1: A slug's blood is green. (True/False): True
You got it right!
The correct answer was: True
Your current score is: 1/1

🧠 Concepts Practiced

Object-Oriented Programming (OOP)

Classes and methods

Instance attributes (self)

Lists of objects

Input validation

Control flow with loops
