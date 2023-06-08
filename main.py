import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rock Paper Scissors")

# Create a label to display the result with large text
result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.grid(row=0, column=0, columnspan=3)

# Create a function to handle button clicks
def play_rps(player_choice):
    # Generate a random choice for the computer
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    # Update the result label
    result_label.config(text=f"You chose {player_choice}. The computer chose {computer_choice}. {result}")

# Load and resize the images using PIL
rock_image = Image.open("rock.jpg")
rock_image = rock_image.resize((800, 150))
rock_photo = ImageTk.PhotoImage(rock_image)

paper_image = Image.open("paper.jpg")
paper_image = paper_image.resize((300, 150))
paper_photo = ImageTk.PhotoImage(paper_image)

scissors_image = Image.open("scissors.jpg")
scissors_image = scissors_image.resize((300, 150))
scissors_photo = ImageTk.PhotoImage(scissors_image)

# Create buttons with resized images and large text
rock_button = tk.Button(root, image=rock_photo, text="Rock", compound="top", font=("Helvetica", 24), command=lambda: play_rps("rock"))
rock_button.grid(row=1, column=0)

paper_button = tk.Button(root, image=paper_photo, text="Paper", compound="top", font=("Helvetica", 24), command=lambda: play_rps("paper"))
paper_button.grid(row=1, column=1)

scissors_button = tk.Button(root, image=scissors_photo, text="Scissors", compound="top", font=("Helvetica", 24), command=lambda: play_rps("scissors"))
scissors_button.grid(row=1, column=2)

root.mainloop()
