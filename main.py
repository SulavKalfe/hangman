import tkinter as tk
from tkinter import messagebox
import random

def select_category():
    valueusedtoreturndata = int()
    def return_options():
        nonlocal valueusedtoreturndata
        valueusedtoreturndata = var.get()
        # print(valueusedtoreturndata)
        root.destroy()

    full_options = [['football', 'cricket', 'basketball', 'tennis', 'golf'],
                    ['inception', 'goodfellas', 'intersteller', 'gladiator', 'momento'],
                    ['chernobyl', 'succession', 'dark', 'narcos', 'peacemaker'],
                    ['sekiro', 'bloodborne', 'doom', 'minecraft', 'undertale']]
    option = ['sports', 'movie', 'series', 'videogames']
    root = tk.Tk()
    root.title("Select an option")
    var = tk.StringVar()

    label = tk.Label(root, text="Select a category")
    label.pack(padx=10, pady=10)
    for i, option in enumerate(option):
        radio = tk.Radiobutton(root, text=option, variable=var, value=i)
        radio.pack(anchor='w')
    root.geometry("300x300")
    button = tk.Button(root, text="Show Selection", command=return_options)
    button.pack(pady=10)

    root.mainloop()
    return full_options[int(valueusedtoreturndata)]


def blank_words(optionlist):
    # word = "i dont know"
    word = random.choice(optionlist)
    #print(f'word: {word}')
    lengthofword = len(word)
    #print(f'length: {lengthofword}')
    numberofexposedletters = random.randint(1, round(lengthofword/2))
    #print(f'number of exposed letters: {numberofexposedletters}')
    exposedletter = random.sample(word, k=numberofexposedletters)
    #print(f'letters: {exposedletter}')
    #print(type(numberofexposedletters))
    blankcanvas = lengthofword * '_'
    #print(blankcanvas)
    #print(word.index(exposedletter[0]))
    listedcanvas = list(blankcanvas)
    count = int()
    listedcanvas = list(blankcanvas)
    for i in listedcanvas:
        if word[count] == " ":
            listedcanvas[count] = " "
        count+=1
    #print(listedcanvas)
    for i in exposedletter:
        #print(f' Word is: {i} index is:{word.index(i)}')
        listedcanvas[word.index(i)] = i
        #print(listedcanvas)
    #print(listedcanvas)
    finalform = ' '.join(listedcanvas)
    #print(finalform)
    return word, finalform, listedcanvas

# print(select_category())
# blank_words(select_category())

# print(a)
# print(b)
# print(c)

def final_game(data):
    chances = 5
    wrongdecision = 0
    indexlist = list()
    word, displayedpart, displayedpartinlist = data

    def input_guess(event=None):
        check_guess(entry.get()[0])
        entry.delete(0, tk.END)


    def check_guess(guess):
        nonlocal indexlist
        nonlocal word, displayedpart, displayedpartinlist

        if guess in word and word.index(guess) not in indexlist:
            for i in range(len(word)):
                if guess == word[i] :
                    indexlist.append(i)
                    displayedpartinlist[i] = word[i]
                    label_for_hint1.config(text=" ".join(displayedpartinlist))
                    if "".join(displayedpartinlist) == word:
                        messagebox.showinfo("Congratulations", "You've guessed the correct word")
                        entry.config(state=tk.DISABLED)
                        window.quit()
        else:
            # print("fuck")
            check_chances()


    def check_chances():
        nonlocal chances, wrongdecision
        # print(chances)
        print(wrongdecision)
        wrongdecision+=1
            # print(wrongdecision)
        if wrongdecision == 1:
            canvas.itemconfig(rope, state='normal')
        elif wrongdecision == 2:
            canvas.itemconfig(head, state='normal')
        elif wrongdecision == 3:
            canvas.itemconfig(body, state='normal')
        elif wrongdecision == 4:
            canvas.itemconfig(lefthand, state='normal')
            canvas.itemconfig(righthand, state='normal')
        elif wrongdecision == 5:
            canvas.itemconfig(leftleg, state='normal')
            canvas.itemconfig(rightleg, state='normal')
            messagebox.showinfo("Sorry", "You've ran out of chances")
            entry.config(state=tk.DISABLED)
            window.quit()

    window = tk.Tk()
    window.title("Guess the word")
    window.geometry("550x550")

    canvas = tk.Canvas(window, width=350, height=350, bg='white')
    canvas.pack()

    canvas.create_line(70, 50, 350, 50, fill='black', width=2)
    rope = canvas.create_line(200, 50, 200, 70, fill='black', width=2, state="hidden")
    radius = 30
    x = 200 - radius
    y = 100 - radius
    head = canvas.create_oval(x, y, x + 2 * radius, y + 2 * radius, outline='black', state='hidden')
    body = canvas.create_line(200, 130, 200, 250, fill='black', width=2, state="hidden")
    righthand = canvas.create_line(200, 150, 140, 200, fill='black', width=2, state="hidden")
    lefthand = canvas.create_line(200, 150, 260, 200, fill='black', width=2, state="hidden")
    rightleg = canvas.create_line(200, 250, 140, 300, fill='black', width=2, state="hidden")
    leftleg = canvas.create_line(200, 250, 240, 300, fill='black', width=2, state="hidden")

    label_for_hint1 = tk.Label(window, text=" ".join(displayedpartinlist))
    label_for_hint1.pack(padx=10, pady=10)

    input_frame = tk.Frame(window)
    input_frame.pack(pady=10)

    label = tk.Label(input_frame, text="Give the letter")
    label.pack(side=tk.LEFT)
    entry = tk.Entry(input_frame)
    entry.pack(side=tk.LEFT, padx=10)
    entry.bind('<Return>', input_guess)

    window.mainloop()


final_game(blank_words(select_category()))
