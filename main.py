from tkinter import *
from PIL import Image, ImageTk
import random

#****************************************************************************

Quit = False
score = 0
total = 0

def check_answer(choice):
    global score
    global total 
    if choice == countries.get(generated_country):
        score += 1
        total += 1
        print("Correct!")
        generate_countries()
        main()
    else:
        print("Wrong!")
        total += 1
    
def generate_countries():
    global generated_country
    global shuffled_options

    generated_country = random.choice(list(countries.keys()))

    new_countries = [i[1] for i in list(countries.items()) if i[1] != countries.get(generated_country)]
    option1 = random.choice(new_countries)
    new_countries.remove(option1)
    option2 = random.choice(new_countries)
    new_countries.remove(option2)
    option3 = random.choice(new_countries)

    options = [countries.get(generated_country), option1, option2, option3]
    shuffled_options = random.sample(options, len(options))

#*****************************************************************************

window = Tk()
window.config(bg = 'white')

#*****************************************************************************

Ac = ImageTk.PhotoImage(Image.open('AC.png'))
Af = ImageTk.PhotoImage(Image.open('AF.png'))
Ag = ImageTk.PhotoImage(Image.open('AG.png'))
Aj = ImageTk.PhotoImage(Image.open('AJ.png'))
Al = ImageTk.PhotoImage(Image.open('AL.png'))
Am = ImageTk.PhotoImage(Image.open('AM.png'))
An = ImageTk.PhotoImage(Image.open('AN.png'))
Ao = ImageTk.PhotoImage(Image.open('AO.png'))
Ar = ImageTk.PhotoImage(Image.open('AR.png'))
As = ImageTk.PhotoImage(Image.open('AS.png'))
Au = ImageTk.PhotoImage(Image.open('AU.png'))

countries = {Ac: 'Antigua and Barbuda', 
             Af: 'Afghanistan',
             Ag: 'Algeria', 
             Aj: 'Azerbaijan', 
             Al: 'Albania', 
             Am: 'Armenia', 
             An: 'Andorra', 
             Ao: 'Angola', 
             Ar: 'Argentina', 
             As: 'Australia', 
             Au: 'Austria'}

#*****************************************************************************

generate_countries()

def main():
        for widget in window.winfo_children():
            widget.destroy()

        Label(window, 
                text=f"Welcome to the flag guessing game!\nClue: they all begin with the letter 'a'\nScore: {score}/{total}",
                background='white').grid(row=0, column=0)

        Label(window, image=generated_country).grid(row=1, column=0)

        a = Button(window, 
                text=shuffled_options[0], 
                font=('Helvetica', '20'),
                command=lambda: check_answer(shuffled_options[0]),
                background='white')
        a.grid(row=2, column=0, sticky=W)

        b = Button(window, 
                text=shuffled_options[1], 
                font=('Helvetica', '20'),
                command=lambda: check_answer(shuffled_options[1]),
                background='white')
        b.grid(row=2, column=0, sticky=E)

        c = Button(window, 
                text=shuffled_options[2],
                font=('Helvetica', '20'), 
                command=lambda: check_answer(shuffled_options[2]),
                background='white')
        c.grid(row=3, column=0, sticky=W)

        d = Button(window, 
                text=shuffled_options[3], 
                font=('Helvetica', '20'),
                command=lambda: check_answer(shuffled_options[3]),
                background='white')
        d.grid(row=3, column=0, sticky=E)

        Quit = Button(window,
                text='Quit',
                font=('Helvetica', '20'),
                command=window.destroy,
                background='white')
        Quit.grid(row=4, column=0, sticky=W)

        if Quit == True:
                window.destroy()
main()



#*****************************************************************************

window.mainloop()
