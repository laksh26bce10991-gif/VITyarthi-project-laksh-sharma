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


## Algorithmic Core & Complexity

This project explicitly avoids built-in shortcut functions (e.g., `max()`, `.reverse()`) to demonstrate algorithmic fundamentals:

| Function | Module | Description | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :---: | :---: |
| `is_prime(n)` | `question_bank.py` | Prime verification via Trial Division | $O(\sqrt{n})$ | $O(1)$ |
| `reverse_array(arr)` | `utils.py` | Manual element order reversal via index manipulation | $O(n)$ | $O(n)$ |
| `generate_fibonacci(n)` | `utils.py` | Iterative Fibonacci sequence generation | $O(n)$ | $O(n)$ |
| `find_maximum(list)` | `utils.py` | Iterative linear search for highest score | $O(n)$ | $O(1)$ |

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/python-quiz-app.git](https://github.com/YOUR_USERNAME/python-quiz-app.git)
   cd python-quiz-app


python main.py
```[cite: 1]

### CLI Application Workflow:
1. **Register**: Select option `1` to create a new user profile[cite: 1].
2. **Login & Take Quiz**: Select option `2` to authenticate and take a 10-question randomized quiz[cite: 1].
3. **View Profile & Analytics**: Select option `3` to inspect your attempt history, highest score, and percentage average[cite: 1].
4. **Exit**: Select option `4` to end the session[cite: 1].

---

## Verification & Unit Testing

You can independently test the algorithmic utility functions from your terminal:

* **Test Manual Array Reversal:**
  ```bash
  python -c "from utils import reverse_array; print(reverse_array([10, 20, 30, 40]))"
  # Output: [40, 30, 20, 10]
  ```[cite: 1]

* **Test Prime Verification:**
  ```bash
  python -c "from question_bank import is_prime; print(is_prime(29))"
  # Output: True
  ```[cite: 1]

* **Test Fibonacci Sequence Generator:**
  ```bash
  python -c "from utils import generate_fibonacci; print(generate_fibonacci(7))"
  # Output: [0, 1, 1, 2, 3, 5, 8]
  ```[cite: 1]

* **Test Linear Max Search:**
  ```bash
  python -c "from utils import find_maximum; print(find_maximum([4, 9, 2, 10, 5]))"
  # Output: 10
  ```[cite: 1]

---

## Course Syllabus Alignment

- **Unit 3: Control Flow & Iteration**: Implemented via interactive loops, input validation blocks, and conditional branching in `quiz_engine.py` and `main.py`[cite: 1].
- **Unit 4: Compound Data Types & Factoring**: Implemented via dictionary/tuple usage for storing user credentials and trial division algorithms in `question_bank.py`[cite: 1].
- **Unit 5: Array Operations & Search Techniques**: Implemented via manual array reversal and linear maximum value search algorithms in `utils.py`[cite: 1].
