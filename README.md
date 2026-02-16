

# 🎲 Bankroll Game

A simple Monopoly-style terminal game built using Python.
This project uses ANSI escape codes to create a colorful board interface inside the terminal and includes dice-based gameplay logic for two players.

---

## 📌 Project Overview

This is a 2-player terminal-based mini Monopoly game where:

* Each player starts with ₹500
* Dice rolls are generated randomly (1–6)
* Players can choose to buy properties
* Money is deducted based on actions
* After 4 rounds, the winner is declared
* ASCII art is displayed for the winner 🎉

---

## 🚀 Features

* 🎨 Colored terminal UI using ANSI Escape Codes
* 🎲 Random dice roll logic
* 💰 Property buying system
* 🏦 Money deduction & transfer logic
* 🏆 Winner detection system
* 🖥 ASCII art result screen
* 🔁 4 rounds turn-based gameplay

---

## 🛠 Technologies Used

* Python 3
* `random` module
* ANSI Escape Codes (for colored terminal output)

---

## ▶ How to Run

1. Make sure Python is installed:

   ```bash
   python --version
   ```

2. Run the game file:

   ```bash
   python bankroll.py
   ```

---

## 🎮 Game Logic Summary

### Player Turn

* Dice is rolled (1–6)
* Based on dice value:

  * 1, 2, 3 → Option to buy (₹50)
  * 4 → Fine deduction (₹10)
  * 5, 6 → Option to buy premium (₹100)

### Special Condition

* If Player 2 rolls the same number as Player 1:

  * ₹100 is transferred from Player 2 to Player 1

---

## 📂 Project Structure

```
terminal-monopoly/
│
├── game.py
└── README.md
```

---

## 🔮 Future Improvements

* Add real board movement tracking
* Add property ownership system
* Add rent system
* Add player names input
* Add unlimited rounds mode
* Convert into GUI version (Tkinter / Web Version)

---

## 📸 Sample Output

Terminal-based board layout with city names and colorful UI elements.

---

