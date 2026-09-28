# VITyarthi-project-laksh-sharma
# Algorithmic & Assessment Engine Quiz System

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-VITyarthi-green)

An interactive, terminal-based Command Line Interface (CLI) Quiz Application built in Python. Developed for **CSE1021: Introduction to Problem Solving and Programming** under the **VITyarthi** project guidelines, this application evaluates programming knowledge while showcasing fundamental computer science algorithms.

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Repository Architecture](#repository-architecture)
- [Algorithmic Core & Complexity](#algorithmic-core--complexity)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Verification & Unit Testing](#verification--unit-testing)
- [Course Syllabus Alignment](#course-syllabus-alignment)

---

## Overview
Traditional assessment systems often rely on static evaluation without illustrating underlying computational principles. This application bridges that gap by combining:
1. **Dynamic Quiz Engine**: Randomly samples 10 Python questions out of a 50-question JSON database on every attempt.
2. **User Profile Management**: Full CRUD operations for user registration, authentication, and historical attempt tracking in memory.
3. **Syllabus Algorithms**: Manual implementations of prime number verification, array order reversal, Fibonacci sequence generation, and peak score searching without relying on built-in helper methods.

---

## Key Features

- 👤 **User Management System (CRUD)**
  - **Create**: Register new user profiles with secure password handling.
  - **Read**: Authenticate user credentials and retrieve historical submission logs[cite: 1].
  - **Update**: Record quiz scores, calculate percentage accuracy, and maintain attempt history[cite: 1].

- 🎯 **Dynamic Quiz Engine**
  - Loads 50 structured questions from external `questions.json`[cite: 1].
  - Uses non-repeating random sampling (`random.sample`) to pick 10 questions per quiz[cite: 1].
  - Gracefully handles non-numeric and out-of-bounds user inputs without crashing.

- 📊 **Performance Analytics**
  - Computes personal highest scores and cumulative percentage averages across all attempts using pure algorithmic loops[cite: 1].

---

## Repository Architecture

```text
QuizApp/
├── main.py             # Main CLI entry point & menu orchestration[cite: 1]
├── quiz_engine.py      # Quiz execution flow, dynamic sampling & analytics[cite: 1]
├── question_bank.py    # JSON reader & prime number trial division algorithm[cite: 1]
├── user_manager.py     # User registration, authentication & history state[cite: 1]
├── utils.py            # Core algorithms (Fibonacci, Array Reversal, Max Search)[cite: 1]
├── questions.json      # Question bank containing 50 Python questions[cite: 1]
├── statement.md        # Problem statement & scope document[cite: 1]
└── README.md           # Project documentation[cite: 1]
```


Algorithmic Core & Complexity

This project explicitly avoids built-in shortcut functions such as max() and .reverse() to demonstrate fundamental algorithmic concepts and implementation techniques.

Function	Module	Description	Time Complexity	Space Complexity
is_prime(n)	question_bank.py	Prime number verification using Trial Division	O(√n)	O(1)
reverse_array(arr)	utils.py	Manually reverses element order using index manipulation	O(n)	O(n)
generate_fibonacci(n)	utils.py	Generates a Fibonacci sequence iteratively	O(n)	O(n)
find_maximum(list)	utils.py	Iterative linear search to find the highest score	O(n)	O(1)
Installation & Setup
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/python-quiz-app.git
cd python-quiz-app

2. Verify File Layout

Make sure questions.json is located in the exact same directory as main.py.

Example:

python-quiz-app/
├── main.py
├── questions.json
├── question_bank.py
└── utils.py

3. Requirements

Python 3.8 or higher

No external third-party dependencies are required.

The project uses Python's standard library modules, including:

json

os

random

How to Run

Launch the main application by running:

python main.py


On some systems, you may need to use:

python3 main.py


The application will start in the terminal and load the quiz questions from questions.json.
