Here’s a clean **README** for your code:

---

# README

## 📌 Overview

This is a simple Python program that asks the user to input their name.

* If the user presses **Enter** without typing anything, the program will display an error message and ask again.
* Once a valid name is entered, the program prints the name back to the user.

---

## 💻 How It Works

1. The program prompts the user:

   ```python
   name = input("What is your name: ")
   ```
2. If the input is empty (`""`), the program prints a warning message and repeats the prompt:

   ```python
   while name == "":
       print("You did not type anything!")
       name = input("What is your name: ")
   ```
3. Once a non-empty name is provided, it confirms the input:

   ```python
   print(f"Your name is {name}")
   ```

---

## ▶️ Example Run

```
What is your name: 
You did not type anything!
What is your name: Victor
Your name is Victor
```

---

## 🛠️ Requirements

* Python 3.x

---

## 🚀 How to Run

1. Save the code into a file, e.g., `ask_name.py`.
2. Open a terminal or command prompt.
3. Run the program:

   ```bash
   python ask_name.py
   ```

---

Would you like me to **add explanations with comments directly inside your code** so it’s beginner-friendly as well?
