from tkinter import *

def button_click(event):
    button_text = event.widget["text"]
    current_expression = input_field.get()

    if button_text == "=":
        try:
            result = eval(current_expression)
            input_field.delete(0, END)
            input_field.insert(END, str(result))
        except:
            input_field.delete(0, END)
            input_field.insert(END, "Error")
    elif button_text == "C":
        input_field.delete(0, END)
    else:
        input_field.insert(END, button_text)

root = Tk()
root.title("Simple Calculator")
root.geometry("800x800")

Label(root, text="Summer Internship Project", font=("Arial", 12, "bold")).pack(pady=5)
Label(root, text="Made by: Alok Singh Yadav", font=("Arial", 10)).pack(pady=2)
Label(root, text="Branch: CSE-DS | Year: 1st", font=("Arial", 10)).pack(pady=2)

input_field = Entry(root, font=("Arial", 20), justify="right")
input_field.pack(fill=X, padx=10, pady=10, ipadx=8, ipady=10)

button_frame = Frame(root)
button_frame.pack()

button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]

for row in button_rows:
    row_frame = Frame(button_frame)
    row_frame.pack()
    for btn_text in row:
        btn = Button(row_frame, text=btn_text, font=("Arial", 14), width=5, height=2)
        btn.pack(side=LEFT, padx=3, pady=3)
        btn.bind("<Button-1>", button_click)

root.mainloop()
