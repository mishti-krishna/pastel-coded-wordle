from tkinter import *
from tkinter import messagebox
import random
from datetime import date
from tkinter import font
from collections import Counter

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def show_rules():
    rules = Tk()

    rules.title("rules of the game")
    rules.configure(bg="#A7C7E7")

    Label(rules, text="how to play:",
          font=("honey beauty", 80), fg="#444444", bg="#A7C7E7").pack(fill="x", pady=20)

    Label(rules, text="guess the string in 5 tries.",
          font=("monospace", 20,"bold"), fg="#444444", bg="#A7C7E7").pack(fill="x", pady=5)

    Label(rules, text="1. each guess must be a valid 5-letter string.",
          font=("monospace", 20,"bold"), fg="#444444",bg="#A7C7E7" ).pack(fill="x", pady=5)

    Label(rules, text="2. the color of the tiles will change to show how close your guess was to the word.",
          font=("monospace", 20,"bold"), fg="#444444", bg="#A7C7E7").pack(fill="x", pady=5)

    Label(rules, text="green letters indicate that the letter is in the word and in the correct spot.",
          font=("monospace", 20,"bold"), fg="#004D40", bg="#A8E6CF"
          ).pack(fill="x", pady=5, anchor="center")

    Label(rules, text="yellow letters indicate that the letter is in the word but in the wrong spot.",
          font=("monospace", 20,"bold"), fg="#004D40", bg="#FFF5A5"
          ).pack(fill="x", pady=5, anchor="center")

    Label(rules, text="red letters indicate that the letter is not in the word in any spot.",
          font=("monospace", 20,"bold"), fg="#AD1457", bg="#FFD6E0"
          ).pack(fill="x", pady=5, anchor="center")

    ok_button = Button(rules, text="ok", command=lambda: [rules.destroy(), playscreen(),], font=("monospace", 20,"bold"),highlightbackground="#CDB4DB")
    ok_button.pack(pady=30)

    center_window(rules, 1020, 470)

def playscreen():

    fh = open("validwords.txt", 'r')
    w = fh.read()
    valid_words = []
    vw = w.split()
    for i in vw:
        valid_words.append(i.lower())

    fh1 = open("targets.txt", 'r')
    w1 = fh1.read()
    targets = w1.split()

    frameworkm = Tk()
    frameworkm.title("play")
    frameworkm.configure(bg="#A7C7E7")

    def validate(alpha):
        if len(alpha) == 0:
            return True
        elif len(alpha) == 1:
            if alpha.isalnum():
                return True
            else:
                return False
        else:
            return False

    vcmd = (frameworkm.register(validate), '%P')

    global framework
    framework = Frame(frameworkm, bg="#A7C7E7")
    framework.pack(fill="both", expand=True)

    framework.grid_columnconfigure(0, weight=1)
    framework.grid_columnconfigure(1, weight=1)
    framework.grid_rowconfigure(0, weight=1)

    left_frame = Frame(framework, bg="#A7C7E7")
    right_frame = Frame(framework, bg="#A7C7E7")

    left_frame.grid(row=0, column=0, sticky="nsew")
    right_frame.grid(row=0, column=1, sticky="nsew")

    grid_holder = Frame(left_frame, bg="#A7C7E7")
    grid_holder.place(relx=0.5, rely=0.5, anchor="center")

    kb_holder = Frame(right_frame, bg="#A7C7E7")
    kb_holder.place(relx=0.5, rely=0.5, anchor="center")

    grid_label = Label(grid_holder, text="guess the word ✨", font=("honey beauty", 40), bg="#A7C7E7", fg="#444444")
    grid_label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

    entry1 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry1.grid(row=1, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry2 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry2.grid(row=1, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry3 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry3.grid(row=1, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry4 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry4.grid(row=1, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry5 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry5.grid(row=1, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry6 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry6.grid(row=2, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry7 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry7.grid(row=2, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry8 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry8.grid(row=2, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry9 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                   font=("monospace", 25, "bold"))
    entry9.grid(row=2, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry10 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry10.grid(row=2, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry11 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry11.grid(row=3, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry12 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry12.grid(row=3, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry13 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry13.grid(row=3, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry14 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry14.grid(row=3, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry15 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry15.grid(row=3, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry16 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry16.grid(row=4, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry17 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry17.grid(row=4, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry18 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry18.grid(row=4, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry19 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry19.grid(row=4, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry20 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry20.grid(row=4, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry21 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry21.grid(row=5, column=0, padx=4, pady=4, ipadx=24, ipady=24)

    entry22 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry22.grid(row=5, column=1, padx=4, pady=4, ipadx=24, ipady=24)

    entry23 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry23.grid(row=5, column=2, padx=4, pady=4, ipadx=24, ipady=24)

    entry24 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry24.grid(row=5, column=3, padx=4, pady=4, ipadx=24, ipady=24)

    entry25 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))
    entry25.grid(row=5, column=4, padx=4, pady=4, ipadx=24, ipady=24)

    entry26 = Entry(grid_holder, width=3, justify="center", validate="key", validatecommand=vcmd, foreground="#2C3E50", background="#FDE2A2",
                    font=("monospace", 25, "bold"))

    entries = [
        entry1, entry2, entry3, entry4, entry5,
        entry6, entry7, entry8, entry9, entry10,
        entry11, entry12, entry13, entry14, entry15,
        entry16, entry17, entry18, entry19, entry20,
        entry21, entry22, entry23, entry24, entry25,
        entry26]

    canvas_width = 610
    canvas_height = 270

    canvas = Canvas(kb_holder, width=canvas_width, height=canvas_height, bg="#A7C7E7", highlightthickness=0)
    canvas.grid(row=8, columnspan=6, pady=20)

    entry1.focus()

    rect1 = canvas.create_rectangle(0, 0, 60, 60, fill="#CDB4DB", outline="#8A6DB8")
    key1 = canvas.create_text(30, 30, text="1", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect2 = canvas.create_rectangle(60, 0, 120, 60, fill="#CDB4DB", outline="#8A6DB8")
    key2 = canvas.create_text(90, 30, text="2", font=("monospace", 25,"bold"), fill="#2C3E50")

    rect3 = canvas.create_rectangle(120, 0, 180, 60, fill="#CDB4DB", outline="#8A6DB8")
    key3 = canvas.create_text(150, 30, text="3", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect4 = canvas.create_rectangle(180, 0, 240, 60, fill="#CDB4DB", outline="#8A6DB8")
    key4 = canvas.create_text(210, 30, text="4", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect5 = canvas.create_rectangle(240, 0, 300, 60, fill="#CDB4DB", outline="#8A6DB8")
    key5 = canvas.create_text(270, 30, text="5", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect6 = canvas.create_rectangle(300, 0, 360, 60, fill="#CDB4DB", outline="#8A6DB8")
    key6 = canvas.create_text(330, 30, text="6", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect7 = canvas.create_rectangle(360, 0, 420, 60, fill="#CDB4DB", outline="#8A6DB8")
    key7 = canvas.create_text(390, 30, text="7", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect8 = canvas.create_rectangle(420, 0, 480, 60, fill="#CDB4DB", outline="#8A6DB8")
    key8 = canvas.create_text(450, 30, text="8", font=("monospace", 25,"bold"), fill="#2C3E50")

    rect9 = canvas.create_rectangle(480, 0, 540, 60, fill="#CDB4DB", outline="#8A6DB8")
    key9 = canvas.create_text(510, 30, text="9", font=("monospace", 25, "bold"), fill="#2C3E50")

    rect0 = canvas.create_rectangle(540, 0, 600, 60, fill="#CDB4DB", outline="#8A6DB8")
    key0 = canvas.create_text(570, 30, text="0", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectq = canvas.create_rectangle(0, 60, 60, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyq = canvas.create_text(30, 90, text="q", font=("monospace", 25,"bold"), fill="#2C3E50")

    rectw = canvas.create_rectangle(60, 60, 120, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyw = canvas.create_text(90, 90, text="w", font=("monospace", 25, "bold"), fill="#2C3E50")

    recte = canvas.create_rectangle(120, 60, 180, 120, fill="#CDB4DB", outline="#8A6DB8")
    keye = canvas.create_text(150, 90, text="e", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectr = canvas.create_rectangle(180, 60, 240, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyr = canvas.create_text(210, 90, text="r", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectt  = canvas.create_rectangle(240, 60, 300, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyt = canvas.create_text(270, 90, text="t", font=("monospace", 25, "bold"), fill="#2C3E50")

    recty =canvas.create_rectangle(300, 60, 360, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyy = canvas.create_text(330, 90, text="y", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectu = canvas.create_rectangle(360, 60, 420, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyu = canvas.create_text(390, 90, text="u", font=("monospace", 25,"bold"), fill="#2C3E50")

    recti = canvas.create_rectangle(420, 60, 480, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyi = canvas.create_text(450, 90, text="i", font=("monospace", 25, "bold"), fill="#2C3E50")

    recto  = canvas.create_rectangle(480, 60, 540, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyo = canvas.create_text(510, 90, text="o", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectp = canvas.create_rectangle(540, 60, 600, 120, fill="#CDB4DB", outline="#8A6DB8")
    keyp = canvas.create_text(570, 90, text="p", font=("monospace", 25,"bold"), fill="#2C3E50")

    recta = canvas.create_rectangle(30, 120, 90, 180, fill="#CDB4DB", outline="#8A6DB8")
    keya = canvas.create_text(60, 150, text="a", font=("monospace", 25, "bold"), fill="#2C3E50")

    rects = canvas.create_rectangle(90, 120, 150, 180, fill="#CDB4DB", outline="#8A6DB8")
    keys = canvas.create_text(120, 150, text="s", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectd = canvas.create_rectangle(150, 120, 210, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyd = canvas.create_text(180, 150, text="d", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectf = canvas.create_rectangle(210, 120, 270, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyf = canvas.create_text(240, 150, text="f", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectg = canvas.create_rectangle(270, 120, 330, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyg = canvas.create_text(300, 150, text="g", font=("monospace", 25, "bold"), fill="#2C3E50")

    recth = canvas.create_rectangle(330, 120, 390, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyh = canvas.create_text(360, 150, text="h", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectj = canvas.create_rectangle(390, 120, 450, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyj = canvas.create_text(420, 150, text="j", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectk = canvas.create_rectangle(450, 120, 510, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyk = canvas.create_text(480, 150, text="k", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectl = canvas.create_rectangle(510, 120, 570, 180, fill="#CDB4DB", outline="#8A6DB8")
    keyl = canvas.create_text(540, 150, text="l", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectz= canvas.create_rectangle(90, 180, 150, 240, fill="#CDB4DB", outline="#8A6DB8")
    keyz = canvas.create_text(120, 210, text="z", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectx = canvas.create_rectangle(150, 180, 210, 240, fill="#CDB4DB", outline="#8A6DB8")
    keyx = canvas.create_text(180, 210, text="x", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectc = canvas.create_rectangle(210, 180, 270, 240, fill="#CDB4DB", outline="#8A6DB8")
    keyc = canvas.create_text(240, 210, text="c", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectv = canvas.create_rectangle(270, 180, 330, 240, fill="#CDB4DB", outline="#8A6DB8")
    keyv = canvas.create_text(300, 210, text="v", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectb = canvas.create_rectangle(330, 180, 390, 240, fill="#CDB4DB", outline="#8A6DB8")
    keyb = canvas.create_text(360, 210, text="b", font=("monospace", 25, "bold"), fill="#2C3E50")

    rectn = canvas.create_rectangle(390, 180, 450, 240, fill="#CDB4DB", outline="#8A6DB8")
    keyn = canvas.create_text(420, 210, text="n", font=("monospace", 25,"bold"), fill="#2C3E50")

    rectm = canvas.create_rectangle(450, 180, 510, 240, fill="#CDB4DB", outline="#8A6DB8")
    keym = canvas.create_text(480, 210, text="m", font=("monospace", 25,"bold"), fill="#2C3E50")

    kb_label = Label(kb_holder, text="choose your letter 🎶", font=("honey beauty", 40),
                     bg="#A7C7E7", fg="#444444")
    canvas.create_window(300, 270, window=kb_label)

    keyboard = {
        "1": (rect1, key1), "2": (rect2, key2), "3": (rect3, key3), "4": (rect4, key4), "5": (rect5, key5),
        "6": (rect6, key6), "7": (rect7, key7), "8": (rect8, key8), "9": (rect9, key9), "0": (rect0, key0),

        "q": (rectq, keyq), "w": (rectw, keyw), "e": (recte, keye), "r": (rectr, keyr), "t": (rectt, keyt),
        "y": (recty, keyy), "u": (rectu, keyu), "i": (recti, keyi), "o": (recto, keyo), "p": (rectp, keyp),

        "a": (recta, keya), "s": (rects, keys), "d": (rectd, keyd), "f": (rectf, keyf), "g": (rectg, keyg),
        "h": (recth, keyh), "j": (rectj, keyj), "k": (rectk, keyk), "l": (rectl, keyl),

        "z": (rectz, keyz), "x": (rectx, keyx), "c": (rectc, keyc), "v": (rectv, keyv), "b": (rectb, keyb),
        "n": (rectn, keyn), "m": (rectm, keym),
    }

    def lock_row(start_index, end_index):
        for i in range(start_index, end_index):
            e = entries[i]
            bg = e.cget("background")
            fg = e.cget("foreground")

            e.config(state="disabled", disabledbackground=bg, disabledforeground=fg)

    def show_message_box():
        messagebox.showinfo(" ", "good job!",)
        answer = messagebox.askyesno(" ", "play another game?")
        if answer:
            frameworkm.destroy()
        else:
            frameworkm.destroy()

    def update_key(letter, colour):
        if letter in keyboard:
            rect, text = keyboard[letter]
            canvas.itemconfig(rect, fill=colour)
            canvas.itemconfig(text, fill="#444444")

    def clicked(event, key):
        focused_entry = framework.focus_get()
        if isinstance(focused_entry, Entry):
            focused_entry.insert(END, key)
            current_index = entries.index(focused_entry)

            if current_index < len(entries) - 1:
                entries[current_index + 1].focus()

                global req_word

                if current_index == 4:
                    global req_word
                    req_word = random.choice(targets).lower()
                    print(req_word)
                    word = ''.join([entry.get() for entry in [entry1, entry2, entry3, entry4, entry5]])

                    if word in valid_words:
                        letter_counts = Counter(req_word)

                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#A8E6CF")
                        elif word[0] in req_word and letter_counts[word[0]] > 0:
                            entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#FFF5A5")
                        else:
                            entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[0], "#FFD6E0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#A8E6CF")
                        elif word[1] in req_word and letter_counts[word[1]] > 0:
                            entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#FFF5A5")
                        else:
                            entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[1], "#FFD6E0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#A8E6CF")
                        elif word[2] in req_word and letter_counts[word[2]] > 0:
                            entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#FFF5A5")
                        else:
                            entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[2], "#FFD6E0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#A8E6CF")
                        elif word[3] in req_word and letter_counts[word[3]] > 0:
                            entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#FFF5A5")
                        else:
                            entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[3], "#FFD6E0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#A8E6CF")
                        elif word[4] in req_word and letter_counts[word[4]] > 0:
                            entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#FFF5A5")
                        else:
                            entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[4], "#FFD6E0")

                        frameworkm.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                     entries[current_index - 3].cget('background') == "#A8E6CF" and
                                     entries[current_index - 2].cget('background') == "#A8E6CF" and
                                     entries[current_index - 1].cget('background') == "#A8E6CF" and
                                     entries[current_index].cget('background') == "#A8E6CF")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "word not in list. try again.")

                    lock_row(current_index - 4, current_index + 1)

                if current_index == 9:
                    word = ''.join([entry.get() for entry in [entry6, entry7, entry8, entry9, entry10]])

                    if word in valid_words:
                        letter_counts = Counter(req_word)

                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#A8E6CF")
                        elif word[0] in req_word and letter_counts[word[0]] > 0:
                            entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#FFF5A5")
                        else:
                            entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[0], "#FFD6E0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#A8E6CF")
                        elif word[1] in req_word and letter_counts[word[1]] > 0:
                            entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#FFF5A5")
                        else:
                            entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[1], "#FFD6E0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#A8E6CF")
                        elif word[2] in req_word and letter_counts[word[2]] > 0:
                            entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#FFF5A5")
                        else:
                            entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[2], "#FFD6E0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#A8E6CF")
                        elif word[3] in req_word and letter_counts[word[3]] > 0:
                            entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#FFF5A5")
                        else:
                            entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[3], "#FFD6E0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#A8E6CF")
                        elif word[4] in req_word and letter_counts[word[4]] > 0:
                            entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#FFF5A5")
                        else:
                            entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[4], "#FFD6E0")

                        frameworkm.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                     entries[current_index - 3].cget('background') == "#A8E6CF" and
                                     entries[current_index - 2].cget('background') == "#A8E6CF" and
                                     entries[current_index - 1].cget('background') == "#A8E6CF" and
                                     entries[current_index].cget('background') == "#A8E6CF")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "word not in list. try again.")

                    lock_row(current_index - 4, current_index + 1)

                if current_index == 14:
                    word = ''.join([entry.get() for entry in [entry11, entry12, entry13, entry14, entry15]])

                    if word in valid_words:
                        letter_counts = Counter(req_word)

                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#A8E6CF")
                        elif word[0] in req_word and letter_counts[word[0]] > 0:
                            entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#FFF5A5")
                        else:
                            entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[0], "#FFD6E0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#A8E6CF")
                        elif word[1] in req_word and letter_counts[word[1]] > 0:
                            entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#FFF5A5")
                        else:
                            entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[1], "#FFD6E0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#A8E6CF")
                        elif word[2] in req_word and letter_counts[word[2]] > 0:
                            entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#FFF5A5")
                        else:
                            entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[2], "#FFD6E0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#A8E6CF")
                        elif word[3] in req_word and letter_counts[word[3]] > 0:
                            entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#FFF5A5")
                        else:
                            entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[3], "#FFD6E0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#A8E6CF")
                        elif word[4] in req_word and letter_counts[word[4]] > 0:
                            entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#FFF5A5")
                        else:
                            entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[4], "#FFD6E0")

                        frameworkm.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                     entries[current_index - 3].cget('background') == "#A8E6CF" and
                                     entries[current_index - 2].cget('background') == "#A8E6CF" and
                                     entries[current_index - 1].cget('background') == "#A8E6CF" and
                                     entries[current_index].cget('background') == "#A8E6CF")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "word not in list. try again.")

                    lock_row(current_index - 4, current_index + 1)

                if current_index == 19:
                    word = ''.join([entry.get() for entry in [entry16, entry17, entry18, entry19, entry20]])

                    if word in valid_words:
                        letter_counts = Counter(req_word)

                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#A8E6CF")
                        elif word[0] in req_word and letter_counts[word[0]] > 0:
                            entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#FFF5A5")
                        else:
                            entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[0], "#FFD6E0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#A8E6CF")
                        elif word[1] in req_word and letter_counts[word[1]] > 0:
                            entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#FFF5A5")
                        else:
                            entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[1], "#FFD6E0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#A8E6CF")
                        elif word[2] in req_word and letter_counts[word[2]] > 0:
                            entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#FFF5A5")
                        else:
                            entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[2], "#FFD6E0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#A8E6CF")
                        elif word[3] in req_word and letter_counts[word[3]] > 0:
                            entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#FFF5A5")
                        else:
                            entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[3], "#FFD6E0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#A8E6CF")
                        elif word[4] in req_word and letter_counts[word[4]] > 0:
                            entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#FFF5A5")
                        else:
                            entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[4], "#FFD6E0")

                        frameworkm.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                     entries[current_index - 3].cget('background') == "#A8E6CF" and
                                     entries[current_index - 2].cget('background') == "#A8E6CF" and
                                     entries[current_index - 1].cget('background') == "#A8E6CF" and
                                     entries[current_index].cget('background') == "#A8E6CF")

                        if all_green:
                            frameworkm.after(500, show_message_box)

                    else:
                        messagebox.showinfo(" ", "word not in list. try again.")

                    lock_row(current_index - 4, current_index + 1)

                if current_index == 24:
                    word = ''.join([entry.get() for entry in [entry21, entry22, entry23, entry24, entry25]])

                    if word in valid_words:
                        letter_counts = Counter(req_word)

                        if word[0] == req_word[0]:
                            entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#A8E6CF")
                        elif word[0] in req_word and letter_counts[word[0]] > 0:
                            entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[0]] -= 1
                            update_key(word[0], "#FFF5A5")
                        else:
                            entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[0], "#FFD6E0")

                        if word[1] == req_word[1]:
                            entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#A8E6CF")
                        elif word[1] in req_word and letter_counts[word[1]] > 0:
                            entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[1]] -= 1
                            update_key(word[1], "#FFF5A5")
                        else:
                            entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[1], "#FFD6E0")

                        if word[2] == req_word[2]:
                            entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#A8E6CF")
                        elif word[2] in req_word and letter_counts[word[2]] > 0:
                            entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[2]] -= 1
                            update_key(word[2], "#FFF5A5")
                        else:
                            entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[2], "#FFD6E0")

                        if word[3] == req_word[3]:
                            entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#A8E6CF")
                        elif word[3] in req_word and letter_counts[word[3]] > 0:
                            entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[3]] -= 1
                            update_key(word[3], "#FFF5A5")
                        else:
                            entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[3], "#FFD6E0")

                        if word[4] == req_word[4]:
                            entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#A8E6CF")
                        elif word[4] in req_word and letter_counts[word[4]] > 0:
                            entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                            letter_counts[word[4]] -= 1
                            update_key(word[4], "#FFF5A5")
                        else:
                            entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                            update_key(word[4], "#FFD6E0")

                        frameworkm.update_idletasks()

                        all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                     entries[current_index - 3].cget('background') == "#A8E6CF" and
                                     entries[current_index - 2].cget('background') == "#A8E6CF" and
                                     entries[current_index - 1].cget('background') == "#A8E6CF" and
                                     entries[current_index].cget('background') == "#A8E6CF")

                        if all_green:
                            frameworkm.after(500, show_message_box)
                            return "break"

                else:
                        messagebox.showinfo(" ", "word not in list.")

                        messagebox.showinfo(" ", "the word was " + req_word + ".")
                        answer = messagebox.askyesno(" ", "play another game?")
                        if answer:
                            frameworkm.destroy()
                        else:
                            frameworkm.destroy()

    def physical_key_pressed(event):

        if event.keysym in ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"):
            return

        if event.keysym == "BackSpace":
            focused_entry = framework.focus_get()
            if isinstance(focused_entry, Entry):
                try:
                    current_index = entries.index(focused_entry)
                except ValueError:
                    return "break"
                focused_entry.delete(0, END)
                if current_index > 0:
                    entries[current_index - 1].focus_set()
            return "break"

        ch = event.char
        if not ch or not ch.isalnum():
            return

        key = ch.lower()

        focused_entry = framework.focus_get()
        if not isinstance(focused_entry, Entry):
            return "break"

        focused_entry.insert(END, key)

        try:
            current_index = entries.index(focused_entry)
        except ValueError:
            return "break"

        if current_index < len(entries) - 1:
            entries[current_index + 1].focus_set()

            if current_index == 4:
                global req_word
                req_word = random.choice(targets).lower()
                print(req_word)
                word = ''.join([entry.get() for entry in [entry1, entry2, entry3, entry4, entry5]])

                if word in valid_words:
                    letter_counts = Counter(req_word)

                    if word[0] == req_word[0]:
                        entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[0]] -= 1
                        update_key(word[0], "#A8E6CF")
                    elif word[0] in req_word and letter_counts[word[0]] > 0:
                        entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[0]] -= 1
                        update_key(word[0], "#FFF5A5")
                    else:
                        entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[0], "#FFD6E0")

                    if word[1] == req_word[1]:
                        entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[1]] -= 1
                        update_key(word[1], "#A8E6CF")
                    elif word[1] in req_word and letter_counts[word[1]] > 0:
                        entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[1]] -= 1
                        update_key(word[1], "#FFF5A5")
                    else:
                        entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[1], "#FFD6E0")

                    if word[2] == req_word[2]:
                        entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[2]] -= 1
                        update_key(word[2], "#A8E6CF")
                    elif word[2] in req_word and letter_counts[word[2]] > 0:
                        entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[2]] -= 1
                        update_key(word[2], "#FFF5A5")
                    else:
                        entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[2], "#FFD6E0")

                    if word[3] == req_word[3]:
                        entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[3]] -= 1
                        update_key(word[3], "#A8E6CF")
                    elif word[3] in req_word and letter_counts[word[3]] > 0:
                        entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[3]] -= 1
                        update_key(word[3], "#FFF5A5")
                    else:
                        entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[3], "#FFD6E0")

                    if word[4] == req_word[4]:
                        entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[4]] -= 1
                        update_key(word[4], "#A8E6CF")
                    elif word[4] in req_word and letter_counts[word[4]] > 0:
                        entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[4]] -= 1
                        update_key(word[4], "#FFF5A5")
                    else:
                        entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[4], "#FFD6E0")

                    frameworkm.update_idletasks()

                    all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                 entries[current_index - 3].cget('background') == "#A8E6CF" and
                                 entries[current_index - 2].cget('background') == "#A8E6CF" and
                                 entries[current_index - 1].cget('background') == "#A8E6CF" and
                                 entries[current_index].cget('background') == "#A8E6CF")

                    if all_green:
                        frameworkm.after(500, show_message_box)

                else:
                    messagebox.showinfo(" ", "word not in list. try again.")

                lock_row(current_index - 4, current_index + 1)

        if current_index == 9:
            word = ''.join([entry.get() for entry in [entry6, entry7, entry8, entry9, entry10]])

            if word in valid_words:
                letter_counts = Counter(req_word)

                if word[0] == req_word[0]:
                    entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[0]] -= 1
                    update_key(word[0], "#A8E6CF")
                elif word[0] in req_word and letter_counts[word[0]] > 0:
                    entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[0]] -= 1
                    update_key(word[0], "#FFF5A5")
                else:
                    entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[0], "#FFD6E0")

                if word[1] == req_word[1]:
                    entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[1]] -= 1
                    update_key(word[1], "#A8E6CF")
                elif word[1] in req_word and letter_counts[word[1]] > 0:
                    entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[1]] -= 1
                    update_key(word[1], "#FFF5A5")
                else:
                    entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[1], "#FFD6E0")

                if word[2] == req_word[2]:
                    entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[2]] -= 1
                    update_key(word[2], "#A8E6CF")
                elif word[2] in req_word and letter_counts[word[2]] > 0:
                    entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[2]] -= 1
                    update_key(word[2], "#FFF5A5")
                else:
                    entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[2], "#FFD6E0")

                if word[3] == req_word[3]:
                    entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[3]] -= 1
                    update_key(word[3], "#A8E6CF")
                elif word[3] in req_word and letter_counts[word[3]] > 0:
                    entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[3]] -= 1
                    update_key(word[3], "#FFF5A5")
                else:
                    entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[3], "#FFD6E0")

                if word[4] == req_word[4]:
                    entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[4]] -= 1
                    update_key(word[4], "#A8E6CF")
                elif word[4] in req_word and letter_counts[word[4]] > 0:
                    entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[4]] -= 1
                    update_key(word[4], "#FFF5A5")
                else:
                    entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[4], "#FFD6E0")

                frameworkm.update_idletasks()

                all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                             entries[current_index - 3].cget('background') == "#A8E6CF" and
                             entries[current_index - 2].cget('background') == "#A8E6CF" and
                             entries[current_index - 1].cget('background') == "#A8E6CF" and
                             entries[current_index].cget('background') == "#A8E6CF")

                if all_green:
                    frameworkm.after(500, show_message_box)

            else:
                messagebox.showinfo(" ", "word not in list. try again.")

            lock_row(current_index - 4, current_index + 1)

        if current_index == 14:
            word = ''.join([entry.get() for entry in [entry11, entry12, entry13, entry14, entry15]])

            if word in valid_words:
                letter_counts = Counter(req_word)

                if word[0] == req_word[0]:
                    entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[0]] -= 1
                    update_key(word[0], "#A8E6CF")
                elif word[0] in req_word and letter_counts[word[0]] > 0:
                    entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[0]] -= 1
                    update_key(word[0], "#FFF5A5")
                else:
                    entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[0], "#FFD6E0")

                if word[1] == req_word[1]:
                    entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[1]] -= 1
                    update_key(word[1], "#A8E6CF")
                elif word[1] in req_word and letter_counts[word[1]] > 0:
                    entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[1]] -= 1
                    update_key(word[1], "#FFF5A5")
                else:
                    entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[1], "#FFD6E0")

                if word[2] == req_word[2]:
                    entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[2]] -= 1
                    update_key(word[2], "#A8E6CF")
                elif word[2] in req_word and letter_counts[word[2]] > 0:
                    entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[2]] -= 1
                    update_key(word[2], "#FFF5A5")
                else:
                    entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[2], "#FFD6E0")

                if word[3] == req_word[3]:
                    entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[3]] -= 1
                    update_key(word[3], "#A8E6CF")
                elif word[3] in req_word and letter_counts[word[3]] > 0:
                    entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[3]] -= 1
                    update_key(word[3], "#FFF5A5")
                else:
                    entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[3], "#FFD6E0")

                if word[4] == req_word[4]:
                    entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[4]] -= 1
                    update_key(word[4], "#A8E6CF")
                elif word[4] in req_word and letter_counts[word[4]] > 0:
                    entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[4]] -= 1
                    update_key(word[4], "#FFF5A5")
                else:
                    entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[4], "#FFD6E0")

                frameworkm.update_idletasks()

                all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                             entries[current_index - 3].cget('background') == "#A8E6CF" and
                             entries[current_index - 2].cget('background') == "#A8E6CF" and
                             entries[current_index - 1].cget('background') == "#A8E6CF" and
                             entries[current_index].cget('background') == "#A8E6CF")

                if all_green:
                    frameworkm.after(500, show_message_box)

            else:
                messagebox.showinfo(" ", "word not in list. try again.")

            lock_row(current_index - 4, current_index + 1)

        if current_index == 19:
            word = ''.join([entry.get() for entry in [entry16, entry17, entry18, entry19, entry20]])

            if word in valid_words:
                letter_counts = Counter(req_word)

                if word[0] == req_word[0]:
                    entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[0]] -= 1
                    update_key(word[0], "#A8E6CF")
                elif word[0] in req_word and letter_counts[word[0]] > 0:
                    entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[0]] -= 1
                    update_key(word[0], "#FFF5A5")
                else:
                    entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[0], "#FFD6E0")

                if word[1] == req_word[1]:
                    entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[1]] -= 1
                    update_key(word[1], "#A8E6CF")
                elif word[1] in req_word and letter_counts[word[1]] > 0:
                    entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[1]] -= 1
                    update_key(word[1], "#FFF5A5")
                else:
                    entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[1], "#FFD6E0")

                if word[2] == req_word[2]:
                    entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[2]] -= 1
                    update_key(word[2], "#A8E6CF")
                elif word[2] in req_word and letter_counts[word[2]] > 0:
                    entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[2]] -= 1
                    update_key(word[2], "#FFF5A5")
                else:
                    entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[2], "#FFD6E0")

                if word[3] == req_word[3]:
                    entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[3]] -= 1
                    update_key(word[3], "#A8E6CF")
                elif word[3] in req_word and letter_counts[word[3]] > 0:
                    entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[3]] -= 1
                    update_key(word[3], "#FFF5A5")
                else:
                    entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[3], "#FFD6E0")

                if word[4] == req_word[4]:
                    entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                    letter_counts[word[4]] -= 1
                    update_key(word[4], "#A8E6CF")
                elif word[4] in req_word and letter_counts[word[4]] > 0:
                    entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                    letter_counts[word[4]] -= 1
                    update_key(word[4], "#FFF5A5")
                else:
                    entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                    update_key(word[4], "#FFD6E0")

                frameworkm.update_idletasks()

                all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                             entries[current_index - 3].cget('background') == "#A8E6CF" and
                             entries[current_index - 2].cget('background') == "#A8E6CF" and
                             entries[current_index - 1].cget('background') == "#A8E6CF" and
                             entries[current_index].cget('background') == "#A8E6CF")

                if all_green:
                    frameworkm.after(500, show_message_box)

            else:
                messagebox.showinfo(" ", "word not in list. try again.")

            lock_row(current_index - 4, current_index + 1)

        if current_index == 24:
            word = ''.join([entry.get() for entry in [entry21, entry22, entry23, entry24, entry25]])

            if word in valid_words:
                letter_counts = Counter(req_word)

                if word in valid_words:
                    letter_counts = Counter(req_word)

                    if word[0] == req_word[0]:
                        entries[current_index - 4].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[0]] -= 1
                        update_key(word[0], "#A8E6CF")
                    elif word[0] in req_word and letter_counts[word[0]] > 0:
                        entries[current_index - 4].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[0]] -= 1
                        update_key(word[0], "#FFF5A5")
                    else:
                        entries[current_index - 4].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[0], "#FFD6E0")

                    if word[1] == req_word[1]:
                        entries[current_index - 3].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[1]] -= 1
                        update_key(word[1], "#A8E6CF")
                    elif word[1] in req_word and letter_counts[word[1]] > 0:
                        entries[current_index - 3].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[1]] -= 1
                        update_key(word[1], "#FFF5A5")
                    else:
                        entries[current_index - 3].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[1], "#FFD6E0")

                    if word[2] == req_word[2]:
                        entries[current_index - 2].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[2]] -= 1
                        update_key(word[2], "#A8E6CF")
                    elif word[2] in req_word and letter_counts[word[2]] > 0:
                        entries[current_index - 2].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[2]] -= 1
                        update_key(word[2], "#FFF5A5")
                    else:
                        entries[current_index - 2].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[2], "#FFD6E0")

                    if word[3] == req_word[3]:
                        entries[current_index - 1].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[3]] -= 1
                        update_key(word[3], "#A8E6CF")
                    elif word[3] in req_word and letter_counts[word[3]] > 0:
                        entries[current_index - 1].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[3]] -= 1
                        update_key(word[3], "#FFF5A5")
                    else:
                        entries[current_index - 1].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[3], "#FFD6E0")

                    if word[4] == req_word[4]:
                        entries[current_index].config(background="#A8E6CF", foreground="#004D40")
                        letter_counts[word[4]] -= 1
                        update_key(word[4], "#A8E6CF")
                    elif word[4] in req_word and letter_counts[word[4]] > 0:
                        entries[current_index].config(background="#FFF5A5", foreground="#004D40")
                        letter_counts[word[4]] -= 1
                        update_key(word[4], "#FFF5A5")
                    else:
                        entries[current_index].config(background="#FFD6E0", foreground="#AD1457")
                        update_key(word[4], "#FFD6E0")

                    frameworkm.update_idletasks()

                    all_green = (entries[current_index - 4].cget('background') == "#A8E6CF" and
                                 entries[current_index - 3].cget('background') == "#A8E6CF" and
                                 entries[current_index - 2].cget('background') == "#A8E6CF" and
                                 entries[current_index - 1].cget('background') == "#A8E6CF" and
                                 entries[current_index].cget('background') == "#A8E6CF")

                    if all_green:
                        frameworkm.after(500, show_message_box)
                        return "break"

            else:
                messagebox.showinfo(" ", "word not in list.")

                messagebox.showinfo(" ", "the word was " + req_word + ".")
                answer = messagebox.askyesno(" ", "play another game?")
                if answer:
                    frameworkm.destroy()
                else:
                    frameworkm.destroy()

    framework.bind_all("<KeyPress>", physical_key_pressed)

    canvas.tag_bind(key1, "<Button-1>", lambda event: clicked(event, "1"))

    canvas.tag_bind(key2, "<Button-1>", lambda event: clicked(event, "2"))

    canvas.tag_bind(key3, "<Button-1>", lambda event: clicked(event, "3"))

    canvas.tag_bind(key4, "<Button-1>", lambda event: clicked(event, "4"))

    canvas.tag_bind(key5, "<Button-1>", lambda event: clicked(event, "5"))

    canvas.tag_bind(key6, "<Button-1>", lambda event: clicked(event, "6"))

    canvas.tag_bind(key7, "<Button-1>", lambda event: clicked(event, "7"))

    canvas.tag_bind(key8, "<Button-1>", lambda event: clicked(event, "8"))

    canvas.tag_bind(key9, "<Button-1>", lambda event: clicked(event, "9"))

    canvas.tag_bind(key0, "<Button-1>", lambda event: clicked(event, "0"))

    canvas.tag_bind(keyq, "<Button-1>", lambda event: clicked(event, "q"))

    canvas.tag_bind(keyw, "<Button-1>", lambda event: clicked(event, "w"))

    canvas.tag_bind(keye, "<Button-1>", lambda event: clicked(event, "e"))

    canvas.tag_bind(keyr, "<Button-1>", lambda event: clicked(event, "r"))

    canvas.tag_bind(keyt, "<Button-1>", lambda event: clicked(event, "t"))

    canvas.tag_bind(keyy, "<Button-1>", lambda event: clicked(event, "y"))

    canvas.tag_bind(keyu, "<Button-1>", lambda event: clicked(event, "u"))

    canvas.tag_bind(keyi, "<Button-1>", lambda event: clicked(event, "i"))

    canvas.tag_bind(keyo, "<Button-1>", lambda event: clicked(event, "o"))

    canvas.tag_bind(keyp, "<Button-1>", lambda event: clicked(event, "p"))

    canvas.tag_bind(keya, "<Button-1>", lambda event: clicked(event, "a"))

    canvas.tag_bind(keys, "<Button-1>", lambda event: clicked(event, "s"))

    canvas.tag_bind(keyd, "<Button-1>", lambda event: clicked(event, "d"))

    canvas.tag_bind(keyf, "<Button-1>", lambda event: clicked(event, "f"))

    canvas.tag_bind(keyg, "<Button-1>", lambda event: clicked(event, "g"))

    canvas.tag_bind(keyh, "<Button-1>", lambda event: clicked(event, "h"))

    canvas.tag_bind(keyj, "<Button-1>", lambda event: clicked(event, "j"))

    canvas.tag_bind(keyk, "<Button-1>", lambda event: clicked(event, "k"))

    canvas.tag_bind(keyl, "<Button-1>", lambda event: clicked(event, "l"))

    canvas.tag_bind(keyz, "<Button-1>", lambda event: clicked(event, "z"))

    canvas.tag_bind(keyx, "<Button-1>", lambda event: clicked(event, "x"))

    canvas.tag_bind(keyc, "<Button-1>", lambda event: clicked(event, "c"))

    canvas.tag_bind(keyv, "<Button-1>", lambda event: clicked(event, "v"))

    canvas.tag_bind(keyb, "<Button-1>", lambda event: clicked(event, "b"))

    canvas.tag_bind(keyn, "<Button-1>", lambda event: clicked(event, "n"))

    canvas.tag_bind(keym, "<Button-1>", lambda event: clicked(event, "m"))

    center_window(frameworkm, 1300, 600)

root=Tk()

root.title("segfaultle main game")
root.configure(background="#A7C7E7")

root.lift()
root.attributes('-topmost', True)
root.after(100, lambda: root.attributes('-topmost', False))

Label(root, text="segfaultle", font=("honey beauty",100), bg="#A7C7E7",fg="#444444").pack()
Label(root, text="get 5 chances to guess a 5-letter string,",font= ("monospace",23,"bold"), bg ="#A7C7E7",fg="#444444").pack()
Label(root, text="related to computer science.",font= ("monospace",23,"bold"),  bg="#A7C7E7",fg="#444444").pack()
Label(root, text=date.today().strftime("%B %d, %Y").lower(),font=("monospace",20,"bold"),  bg="#A7C7E7",fg="#444444").pack()

Button(root, text = "play", font= ("monospace", 15, "bold"), highlightbackground="#CDB4DB", fg="#2C3E50",command=show_rules).pack()
Button(root, text = "close", font= ("monospace", 15, "bold"),  highlightbackground="#FFD6E0",fg="#AD1457",command = root.destroy).pack()

center_window(root, 600, 300)

root.mainloop()