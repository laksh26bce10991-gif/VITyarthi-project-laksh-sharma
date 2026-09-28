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
