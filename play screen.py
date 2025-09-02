from tkinter import *
from tkinter import messagebox
import random
from datetime import date

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def show_rules():
    rules = Tk()

    rules.title("RULES OF THE GAME")

    Label(rules, text="HOW TO PLAY", font=("Georgia", 50), fg="#6A5ACD", ).pack(pady=10)
    Label(rules, text="Guess the Wordle in 5 tries.", font=("Georgia", 20), fg="#6A5ACD", ).pack(pady=5)
    Label(rules, text="1. Each guess must be a valid 5-letter word.", font=("Georgia", 20), fg="#6A5ACD", ).pack(pady=5)
    Label(rules, text="2. The color of the tiles will change to show how close your guess was to the word.", font=("Georgia", 20), fg="#6A5ACD", ).pack(pady=5)

    Label(rules, text="Green letters indicate that the letter is in the word and in the correct spot.", font=("Georgia", 20), fg="#C1E1C1", ).pack(pady=5)
    Label(rules, text="Yellow letters indicate that the letter is in the word but in the wrong spot.", font=("Georgia", 20), fg="#FFFAA0", ).pack(pady=5)
    Label(rules, text="Red letters indicate that the letter is not in the word in any spot.", font=("Georgia", 20), fg="#FAA0A0", ).pack(pady=5)

    ok_button = Button(rules, text="OK", command=lambda: [rules.destroy(), playscreen()], font=("Georgia", 20))
    ok_button.pack(pady=20)

    center_window(rules, 800, 400)

def playscreen():
    fh = open("validwords.txt", 'r')
    w = fh.read()
    valid_words = []
    vw = w.split()
    for i in vw:
        valid_words.append(i.upper())

    fh1 = open("targets.txt", 'r')
    w1 = fh1.read()
    targets = w1.split()

    frameworkm = Tk()
    frameworkm.title("PLAY")

    def validate(alpha):
        if len(alpha) == 0:
            return True
        elif len(alpha) == 1:
            if alpha.isalpha() == True and alpha.isupper() == True:
                return True
            else:
                return False
        else:
            return False

    vcmd = (frameworkm.register(validate), '%P')

    framework = Frame(frameworkm)
    framework.place(relx=0.5, rely=0.5, anchor="center")

    Label(framework, text="WORDLE COMPACT", font=("Georgia", 50)).grid(row=0, columnspan=10)

    entry1 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry1.grid(row=1, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry2 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry2.grid(row=1, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry3 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry3.grid(row=1, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry4 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry4.grid(row=1, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry5 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry5.grid(row=1, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry6 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry6.grid(row=2, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry7 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry7.grid(row=2, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry8 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry8.grid(row=2, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry9 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                   font=("Georgia", 25))
    entry9.grid(row=2, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry10 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry10.grid(row=2, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry11 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry11.grid(row=3, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry12 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry12.grid(row=3, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry13 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry13.grid(row=3, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry14 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry14.grid(row=3, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry15 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry15.grid(row=3, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry16 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry16.grid(row=4, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry17 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry17.grid(row=4, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry18 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry18.grid(row=4, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry19 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry19.grid(row=4, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry20 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry20.grid(row=4, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry21 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry21.grid(row=5, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry22 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry22.grid(row=5, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry23 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry23.grid(row=5, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry24 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry24.grid(row=5, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry25 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))
    entry25.grid(row=5, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry26 = Entry(framework, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#6A5ACD",
                    font=("Georgia", 25))

    entries = [
        entry1, entry2, entry3, entry4, entry5,
        entry6, entry7, entry8, entry9, entry10,
        entry11, entry12, entry13, entry14, entry15,
        entry16, entry17, entry18, entry19, entry20,
        entry21, entry22, entry23, entry24, entry25,
        entry26]

    canvas_width = 600
    canvas_height = 220

    canvas = Canvas(framework, width=canvas_width, height=canvas_height, bg="#C3B1E1")
    canvas.grid(row=8, columnspan=5, pady=20)

    keyboard_layout = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ]
    key_width = 50
    key_height = 50
    key_padding = 10

    entry1.focus()

    def show_message_box():
        messagebox.showinfo(" ", "Good Job!")

    def clicked(event, key):
        focused_entry = framework.focus_get()
        if isinstance(focused_entry, Entry):
            focused_entry.insert(END, key)
            current_index = entries.index(focused_entry)

            if current_index < len(entries) - 1:
                entries[current_index + 1].focus()

                if current_index == 4:
                    global req_word
                    req_word = random.choice(targets).upper()
                    print(req_word)
                    word = ''.join([entry.get() for entry in [entry1, entry2, entry3, entry4, entry5]])

                    if word in valid_words:
                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#C1E1C1")
                        elif word[0] in req_word:
                            entries[current_index - 4].config(background="#FFFAA0")
                        else:
                            entries[current_index - 4].config(background="#FAA0A0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#C1E1C1")
                        elif word[1] in req_word:
                            entries[current_index - 3].config(background="#FFFAA0")
                        else:
                            entries[current_index - 3].config(background="#FAA0A0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#C1E1C1")
                        elif word[2] in req_word:
                            entries[current_index - 2].config(background="#FFFAA0")
                        else:
                            entries[current_index - 2].config(background="#FAA0A0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#C1E1C1")
                        elif word[3] in req_word:
                            entries[current_index - 1].config(background="#FFFAA0")
                        else:
                            entries[current_index - 1].config(background="#FAA0A0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#C1E1C1")
                        elif word[4] in req_word:
                            entries[current_index].config(background="#FFFAA0")
                        else:
                            entries[current_index].config(background="#FAA0A0")

                        frameworkm.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#C1E1C1" and
                                     entries[current_index - 3].cget('background') == "#C1E1C1" and
                                     entries[current_index - 2].cget('background') == "#C1E1C1" and
                                     entries[current_index - 1].cget('background') == "#C1E1C1" and
                                     entries[current_index].cget('background') == "#C1E1C1")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "Word not in List. Try Again.")

                if current_index == 9:
                    word = ''.join([entry.get() for entry in [entry6, entry7, entry8, entry9, entry10]])
                    if word in valid_words:
                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#C1E1C1")
                        elif word[0] in req_word:
                            entries[current_index - 4].config(background="#FFFAA0")
                        else:
                            entries[current_index - 4].config(background="#FAA0A0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#C1E1C1")
                        elif word[1] in req_word:
                            entries[current_index - 3].config(background="#FFFAA0")
                        else:
                            entries[current_index - 3].config(background="#FAA0A0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#C1E1C1")
                        elif word[2] in req_word:
                            entries[current_index - 2].config(background="#FFFAA0")
                        else:
                            entries[current_index - 2].config(background="#FAA0A0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#C1E1C1")
                        elif word[3] in req_word:
                            entries[current_index - 1].config(background="#FFFAA0")
                        else:
                            entries[current_index - 1].config(background="#FAA0A0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#C1E1C1")
                        elif word[4] in req_word:
                            entries[current_index].config(background="#FFFAA0")
                        else:
                            entries[current_index].config(background="#FAA0A0")

                        framework.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#C1E1C1" and
                                     entries[current_index - 3].cget('background') == "#C1E1C1" and
                                     entries[current_index - 2].cget('background') == "#C1E1C1" and
                                     entries[current_index - 1].cget('background') == "#C1E1C1" and
                                     entries[current_index].cget('background') == "#C1E1C1")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "Word not in List. Try Again.")

                if current_index == 14:
                    word = ''.join([entry.get() for entry in [entry11, entry12, entry13, entry14, entry15]])
                    if word in valid_words:
                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#C1E1C1")
                        elif word[0] in req_word:
                            entries[current_index - 4].config(background="#FFFAA0")
                        else:
                            entries[current_index - 4].config(background="#FAA0A0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#C1E1C1")
                        elif word[1] in req_word:
                            entries[current_index - 3].config(background="#FFFAA0")
                        else:
                            entries[current_index - 3].config(background="#FAA0A0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#C1E1C1")
                        elif word[2] in req_word:
                            entries[current_index - 2].config(background="#FFFAA0")
                        else:
                            entries[current_index - 2].config(background="#FAA0A0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#C1E1C1")
                        elif word[3] in req_word:
                            entries[current_index - 1].config(background="#FFFAA0")
                        else:
                            entries[current_index - 1].config(background="#FAA0A0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#C1E1C1")
                        elif word[4] in req_word:
                            entries[current_index].config(background="#FFFAA0")
                        else:
                            entries[current_index].config(background="#FAA0A0")

                        framework.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#C1E1C1" and
                                     entries[current_index - 3].cget('background') == "#C1E1C1" and
                                     entries[current_index - 2].cget('background') == "#C1E1C1" and
                                     entries[current_index - 1].cget('background') == "#C1E1C1" and
                                     entries[current_index].cget('background') == "#C1E1C1")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "Word not in List. Try Again.")

                if current_index == 19:
                    word = ''.join([entry.get() for entry in [entry16, entry17, entry18, entry19, entry20]])
                    if word in valid_words:
                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#C1E1C1")
                        elif word[0] in req_word:
                            entries[current_index - 4].config(background="#FFFAA0")
                        else:
                            entries[current_index - 4].config(background="#FAA0A0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#C1E1C1")
                        elif word[1] in req_word:
                            entries[current_index - 3].config(background="#FFFAA0")
                        else:
                            entries[current_index - 3].config(background="#FAA0A0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#C1E1C1")
                        elif word[2] in req_word:
                            entries[current_index - 2].config(background="#FFFAA0")
                        else:
                            entries[current_index - 2].config(background="#FAA0A0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#C1E1C1")
                        elif word[3] in req_word:
                            entries[current_index - 1].config(background="#FFFAA0")
                        else:
                            entries[current_index - 1].config(background="#FAA0A0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#C1E1C1")
                        elif word[4] in req_word:
                            entries[current_index].config(background="#FFFAA0")
                        else:
                            entries[current_index].config(background="#FAA0A0")

                        framework.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#C1E1C1" and
                                     entries[current_index - 3].cget('background') == "#C1E1C1" and
                                     entries[current_index - 2].cget('background') == "#C1E1C1" and
                                     entries[current_index - 1].cget('background') == "#C1E1C1" and
                                     entries[current_index].cget('background') == "#C1E1C1")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "Word not in List. Try Again.")

                if current_index == 24:
                    word = ''.join([entry.get() for entry in [entry21, entry22, entry23, entry24, entry25]])
                    if word in valid_words:
                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#C1E1C1")
                        elif word[0] in req_word:
                            entries[current_index - 4].config(background="#FFFAA0")
                        else:
                            entries[current_index - 4].config(background="#FAA0A0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#C1E1C1")
                        elif word[1] in req_word:
                            entries[current_index - 3].config(background="#FFFAA0")
                        else:
                            entries[current_index - 3].config(background="#FAA0A0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#C1E1C1")
                        elif word[2] in req_word:
                            entries[current_index - 2].config(background="#FFFAA0")
                        else:
                            entries[current_index - 2].config(background="#FAA0A0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#C1E1C1")
                        elif word[3] in req_word:
                            entries[current_index - 1].config(background="#FFFAA0")
                        else:
                            entries[current_index - 1].config(background="#FAA0A0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#C1E1C1")
                        elif word[4] in req_word:
                            entries[current_index].config(background="#FFFAA0")
                        else:
                            entries[current_index].config(background="#FAA0A0")

                        framework.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#C1E1C1" and
                                     entries[current_index - 3].cget('background') == "#C1E1C1" and
                                     entries[current_index - 2].cget('background') == "#C1E1C1" and
                                     entries[current_index - 1].cget('background') == "#C1E1C1" and
                                     entries[current_index].cget('background') == "#C1E1C1")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                        else:
                            messagebox.showinfo(" ", "The word was " + req_word + ".")

                    else:
                        messagebox.showinfo(" ", "Word not in List. Try Again.")


    canvas.create_rectangle(50, 30, 100, 80, fill="white", outline="black")
    key1 = canvas.create_text(75, 55, text="Q", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key1, "<Button-1>", lambda event: clicked(event, "Q"))

    canvas.create_rectangle(100, 30, 150, 80, fill="white", outline="black")
    key2 = canvas.create_text(125, 55, text="W", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key2, "<Button-1>", lambda event: clicked(event, "W"))

    canvas.create_rectangle(150, 30, 200, 80, fill="white", outline="black")
    key3 = canvas.create_text(175, 55, text="E", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key3, "<Button-1>", lambda event: clicked(event, "E"))

    canvas.create_rectangle(200, 30, 250, 80, fill="white", outline="black")
    key4 = canvas.create_text(225, 55, text="R", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key4, "<Button-1>", lambda event: clicked(event, "R"))

    canvas.create_rectangle(250, 30, 300, 80, fill="white", outline="black")
    key5 = canvas.create_text(275, 55, text="T", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key5, "<Button-1>", lambda event: clicked(event, "T"))

    canvas.create_rectangle(300, 30, 350, 80, fill="white", outline="black")
    key6 = canvas.create_text(325, 55, text="Y", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key6, "<Button-1>", lambda event: clicked(event, "Y"))

    canvas.create_rectangle(350, 30, 400, 80, fill="white", outline="black")
    key7 = canvas.create_text(375, 55, text="U", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key7, "<Button-1>", lambda event: clicked(event, "U"))

    canvas.create_rectangle(400, 30, 450, 80, fill="white", outline="black")
    key8 = canvas.create_text(425, 55, text="I", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key8, "<Button-1>", lambda event: clicked(event, "I"))

    canvas.create_rectangle(450, 30, 500, 80, fill="white", outline="black")
    key9 = canvas.create_text(475, 55, text="O", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key9, "<Button-1>", lambda event: clicked(event, "O"))

    canvas.create_rectangle(500, 30, 550, 80, fill="white", outline="black")
    key10 = canvas.create_text(525, 55, text="P", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key10, "<Button-1>", lambda event: clicked(event, "P"))

    canvas.create_rectangle(70, 90, 120, 140, fill="white", outline="black")
    key11 = canvas.create_text(95, 115, text="A", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key11, "<Button-1>", lambda event: clicked(event, "A"))

    canvas.create_rectangle(120, 90, 170, 140, fill="white", outline="black")
    key12 = canvas.create_text(145, 115, text="S", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key12, "<Button-1>", lambda event: clicked(event, "S"))

    canvas.create_rectangle(170, 90, 220, 140, fill="white", outline="black")
    key13 = canvas.create_text(195, 115, text="D", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key13, "<Button-1>", lambda event: clicked(event, "D"))

    canvas.create_rectangle(220, 90, 270, 140, fill="white", outline="black")
    key14 = canvas.create_text(245, 115, text="F", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key14, "<Button-1>", lambda event: clicked(event, "F"))

    canvas.create_rectangle(270, 90, 320, 140, fill="white", outline="black")
    key15 = canvas.create_text(295, 115, text="G", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key15, "<Button-1>", lambda event: clicked(event, "G"))

    canvas.create_rectangle(320, 90, 370, 140, fill="white", outline="black")
    key16 = canvas.create_text(345, 115, text="H", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key16, "<Button-1>", lambda event: clicked(event, "H"))

    canvas.create_rectangle(370, 90, 420, 140, fill="white", outline="black")
    key17 = canvas.create_text(395, 115, text="J", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key17, "<Button-1>", lambda event: clicked(event, "J"))

    canvas.create_rectangle(420, 90, 470, 140, fill="white", outline="black")
    key18 = canvas.create_text(445, 115, text="K", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key18, "<Button-1>", lambda event: clicked(event, "K"))

    canvas.create_rectangle(470, 90, 520, 140, fill="white", outline="black")
    key19 = canvas.create_text(495, 115, text="L", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key19, "<Button-1>", lambda event: clicked(event, "L"))

    canvas.create_rectangle(90, 150, 140, 200, fill="white", outline="black")
    key20 = canvas.create_text(115, 175, text="Z", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key20, "<Button-1>", lambda event: clicked(event, "Z"))

    canvas.create_rectangle(140, 150, 190, 200, fill="white", outline="black")
    key21 = canvas.create_text(165, 175, text="X", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key21, "<Button-1>", lambda event: clicked(event, "X"))

    canvas.create_rectangle(190, 150, 240, 200, fill="white", outline="black")
    key22 = canvas.create_text(215, 175, text="C", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key22, "<Button-1>", lambda event: clicked(event, "C"))

    canvas.create_rectangle(240, 150, 290, 200, fill="white", outline="black")
    key23 = canvas.create_text(265, 175, text="V", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key23, "<Button-1>", lambda event: clicked(event, "V"))

    canvas.create_rectangle(290, 150, 340, 200, fill="white", outline="black")
    key24 = canvas.create_text(315, 175, text="B", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key24, "<Button-1>", lambda event: clicked(event, "B"))

    canvas.create_rectangle(340, 150, 390, 200, fill="white", outline="black")
    key25 = canvas.create_text(365, 175, text="N", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key25, "<Button-1>", lambda event: clicked(event, "N"))

    canvas.create_rectangle(390, 150, 440, 200, fill="white", outline="black")
    key26 = canvas.create_text(415, 175, text="M", font=("Georgia", 20), fill="black")
    canvas.tag_bind(key26, "<Button-1>", lambda event: clicked(event, "M"))

    canvas.create_rectangle(440, 150, 490, 200, fill="white", outline="black")
    key27 = canvas.create_text(465, 175, text="Close ", font=("Georgia", 12), fill="black")
    canvas.tag_bind(key27, "<Button-1>", lambda event: frameworkm.destroy())

    center_window(frameworkm, 800, 900)

root=Tk()

root.title("WORDLE COMPACT")

Label(root, text="WORDLE", font=("Georgia",50)).pack()
Label(root, text="Get 5 chances to guess a 5-letter word,",font=20).pack()
Label(root, text="without the internet.",font=20).pack()
Label(root, text=date.today().strftime("%B %d, %Y"),font=20).pack()

Button(root, text = "Play",command=show_rules).pack()
Button(root, text = "Close", command = root.destroy).pack()

center_window(root, 425, 230)

root.mainloop()

