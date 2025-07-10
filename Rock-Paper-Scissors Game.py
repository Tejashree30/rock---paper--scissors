import tkinter as tk
from tkinter import messagebox
import random
import time

# Game options
choices = ['Rock', 'Paper', 'Scissors']

# Score tracking
user_score = 0
computer_score = 0

# Main game logic
def determine_winner(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update UI
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")
    score_label.config(text=f"Score - You: {user_score}  |  Computer: {computer_score}")

# Play again function
def reset_game():
    result_label.config(text="Make your move!")
    score_label.config(text=f"Score - You: {user_score}  |  Computer: {computer_score}")

# Confirm exit
def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit the game?"):
        root.destroy()

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x400")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="darkblue")
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14), bg="#f0f0f0")
instruction_label.pack(pady=5)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 14), width=12, command=lambda: determine_winner("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 14), width=12, command=lambda: determine_winner("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 14), width=12, command=lambda: determine_winner("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Display
result_label = tk.Label(root, text="Make your move!", font=("Arial", 14, "italic"), bg="#f0f0f0", fg="black")
result_label.pack(pady=20)

# Score Display
score_label = tk.Label(root, text="Score - You: 0  |  Computer: 0", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="green")
score_label.pack(pady=10)

# Bottom Buttons
bottom_frame = tk.Frame(root, bg="#f0f0f0")
bottom_frame.pack(pady=20)

reset_btn = tk.Button(bottom_frame, text="🔄 Play Again", font=("Arial", 12), command=reset_game)
reset_btn.grid(row=0, column=0, padx=15)

exit_btn = tk.Button(bottom_frame, text="❌ Exit", font=("Arial", 12), command=exit_game)
exit_btn.grid(row=0, column=1, padx=15)

# Start GUI loop
root.mainloop()
