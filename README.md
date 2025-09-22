# PRODIGY_CS_03
# Password Complexity Checker

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Scoring Criteria](#scoring-criteria)
6. [Strength Levels](#strength-levels)
7. [Technologies Used](#technologies-used)
8. [Project Structure](#project-structure)
9. [Customization](#customization)
10. [License](#license)

---

## Overview

The Password Complexity Checker is a web-based tool that evaluates and scores passwords against strict security criteria. It uses a Python Flask backend and an HTML/CSS frontend to provide an interactive interface that analyzes password strength and offers actionable feedback.

---

## Features

* **Length Check**: Ensures the password is at least 12 characters long.
* **Character Diversity**: Checks for uppercase, lowercase, numbers, and special characters.
* **Common Words Detection**: Flags passwords containing common dictionary words or predictable sequences.
* **Repeating Characters Check**: Detects more than two consecutive identical characters.
* **Sequential Pattern Detection**: Identifies sequential patterns like "123" or "abc".
* **Scoring System**: Assigns points based on password strength.
* **Strength Classification**: Categorizes passwords as Very Weak, Weak, Moderate, Strong, or Very Strong.
* **Feedback**: Provides suggestions to improve password security.

---

## Installation

1. Clone or download the repository.
2. Ensure **Python 3.8+** is installed.
3. Install Flask:

```bash
pip install flask
```

4. Navigate to the project directory:

```bash
cd /path/to/project
```

5. Run the application:

```bash
python app.py
```

6. Open in your browser:

```
http://127.0.0.1:5000/
```

---

## Usage

1. Enter a password in the input field.
2. Click **Check Password**.
3. View results including:

   * **Score**
   * **Strength Level**
   * Detected **character types**
   * **Feedback**

---

## Scoring Criteria

* **+2 points** for password length ≥12.
* **+2 points** for each additional character type beyond one.
* **+3 points** if no common words are present.
* **+1 point** if no more than two consecutive identical characters.
* **-5 points** for obvious sequential patterns (e.g., "123", "abc").

## Strength Levels

* **Very Strong**: score ≥10
* **Strong**: 7–9
* **Moderate**: 4–6
* **Weak**: 1–3
* **Very Weak**: ≤0

---

## Technologies Used

* Python 3.8+
* Flask (Backend)
* HTML5, CSS3, JavaScript (Frontend)

---

## Project Structure

```
project_folder/
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend
└── README.md            # Project documentation
```

---

## Customization

* Expand the `COMMON_WORDS` list in `app.py`.
* Adjust scoring weights and feedback messages.
* Enhance frontend UI/UX with additional styling or frameworks.

---

## License

This project is open-source and free for educational and personal use.

