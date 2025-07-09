from tkinter import *
import random

user_total_score = 0
computer_total_score = 0
current_round_number = 1

def handle_user_choice_rock():
    handle_user_move("Rock", "🪨")

def handle_user_choice_paper():
    handle_user_move("Paper", "📄")

def handle_user_choice_scissors():
    handle_user_move("Scissors", "✂️")

def handle_user_move(player_choice_text, player_choice_symbol):
    global user_total_score, computer_total_score, current_round_number

    computer_choice_symbol = random.choice(["🪨", "📄", "✂️"])

    label_user_choice.config(text="You chose: " + player_choice_symbol)
    label_computer_choice.config(text="Computer chose: " + computer_choice_symbol)

    if player_choice_symbol == computer_choice_symbol:
        label_result.config(text=f"Round {current_round_number} Result: Tie", fg="gray")
    elif (player_choice_symbol == "🪨" and computer_choice_symbol == "✂️") or \
         (player_choice_symbol == "📄" and computer_choice_symbol == "🪨") or \
         (player_choice_symbol == "✂️" and computer_choice_symbol == "📄"):
        label_result.config(text=f"Round {current_round_number} Result: You Win", fg="green")
        user_total_score += 1
    else:
        label_result.config(text=f"Round {current_round_number} Result: Computer Wins", fg="red")
        computer_total_score += 1

    label_score.config(text=f"Score - You: {user_total_score} | Computer: {computer_total_score}")
    current_round_number += 1

    if user_total_score == 2 or computer_total_score == 2:
        if user_total_score > computer_total_score:
            label_result.config(text="🎉 You won the match (Best of 3)!", fg="green")
        else:
            label_result.config(text="💻 Computer won the match (Best of 3)!", fg="red")
        disable_all_game_buttons()

def reset_entire_game():
    global user_total_score, computer_total_score, current_round_number
    user_total_score = 0
    computer_total_score = 0
    current_round_number = 1
    label_user_choice.config(text="You chose: ")
    label_computer_choice.config(text="Computer chose: ")
    label_result.config(text="Result: ", fg="black")
    label_score.config(text="Score - You: 0 | Computer: 0")

main_window = Tk()
main_window.title("Rock Paper Scissors - Best of 3")
main_window.geometry("800x800")
main_window.configure(bg="#f0f0f0")

Label(main_window, text="Summer Internship Project", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(pady=5)
Label(main_window, text="Made by: Alok Singh Yadav", font=("Helvetica", 10), bg="#f0f0f0").pack(pady=2)
Label(main_window, text="Branch: CSE-DS | Year: 1st", font=("Helvetica", 10), bg="#f0f0f0").pack(pady=2)

Label(main_window, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

label_user_choice = Label(main_window, text="You chose: ", font=("Helvetica", 12), bg="#f0f0f0")
label_user_choice.pack()

label_computer_choice = Label(main_window, text="Computer chose: ", font=("Helvetica", 12), bg="#f0f0f0")
label_computer_choice.pack()

label_result = Label(main_window, text="Result: ", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
label_result.pack(pady=15)

label_score = Label(main_window, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#f0f0f0")
label_score.pack(pady=5)

button_rock = Button(main_window, text="🪨", font=("Arial", 24), width=5, height=2, command=handle_user_choice_rock)
button_rock.pack(pady=8)

button_paper = Button(main_window, text="📄", font=("Arial", 24), width=5, height=2, command=handle_user_choice_paper)
button_paper.pack(pady=8)

button_scissors = Button(main_window, text="✂️", font=("Arial", 24), width=5, height=2, command=handle_user_choice_scissors)
button_scissors.pack(pady=8)

Button(main_window, text="Reset Match", font=("Helvetica", 12), width=15, command=reset_entire_game).pack(pady=20)

main_window.mainloop()
