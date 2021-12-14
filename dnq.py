from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pygame, os, random
from joblib import load
import numpy as np
import webbrowser

#-----------FUNCTIONS----------------------------------------------------------

def stats_b():
    
    def lolw():
        url = "https://www.youtube.com/watch?v=Gnsq2lseMk0"
        webbrowser.open(url,new=1)
        
    def resetw():
        goldEB.delete(0, END)
        goldER.delete(0, END)
        creepEB.delete(0, END)
        creepER.delete(0, END)
        killEB.delete(0, END)
        killER.delete(0, END)
        choiceB.delete(0, END)
        choiceR.delete(0, END)
        p3.destroy()

    def ML_b():
        model = load('GBC_DNQ_15.joblib')
        
        blueGold = int(goldEB.get())
        blueMinionsKilled = int(creepEB.get())
        redGold = int(goldER.get())
        redMinionsKilled = int(creepER.get())
        blueChampKills = int(killEB.get())
        blueTowersDestroyed = int(choiceB.get())
        redChampKills = int(killER.get())
        redTowersDestroyed = int(choiceR.get())
        
        X = np.array(([[blueGold, blueMinionsKilled, redGold, redMinionsKilled, blueChampKills, blueTowersDestroyed,
                        redChampKills, redTowersDestroyed]]))
        print(X)
        prediction = model.predict(X)
        
        if int(prediction[0]) == 0:
            chaine = "RED TEAM\n"
            flag = 0
        else:
            chaine = "BLUE TEAM\n"
            flag = 1
            
        basic_chaine = " The winner should be :\n "
        percent = "with 78% precision rate \n"
        
        
        result1 = Label(p3, text = basic_chaine)
        result1.config(bg = "grey30", fg = "white", font = labelfont4)
        result1.grid(row = 0, column = 0, sticky = E)
        
        result2 = Label(p3, text = chaine)
        if flag == 1:
            result2.config(bg = "grey30", fg = "dodger blue", font = labelfont4)
        else:
            result2.config(bg = "grey30", fg = "brown3", font = labelfont4)
        result2.grid(row = 0, column = 1, sticky = E)
        
        result3 = Label(p3, text = percent)
        result3.config(bg = "grey30", fg = "white", font = labelfont4)
        result3.grid(row = 0, column = 2, sticky = E)
         
        print(prediction) 
        
    

    window1 = Toplevel(window)
    window1.title('dnq ml program')
    # window1.geometry('460x330+65+260')
    center_screen(window1)
    window1.config(bg = 'grey30')
    window1.resizable(False, False)
    
    p1 = PanedWindow(window1)
    p1.config(bg = "grey30")
    p1.grid(row = 0, column = 0)
    p2 = PanedWindow(window1)
    p2.config(bg = "grey30")
    p2.grid(row = 1, column = 0)
    p3 = PanedWindow(window1)
    p3.config(bg = "grey30")
    p3.grid(row = 2, column = 0)
    p4 = PanedWindow(window1)
    p4.config(bg = "grey30")
    p4.grid(row = 3, column = 0)

    title = Label(p1, text = "\n  DNQ's PREDICTOR  \n")
    title.config(font = labelfont2, bg = 'grey30',  fg = 'white')
    title.grid(row = 0, column = 1, columnspan = 2, sticky = W+E)

    back = 'ramus.png'
    open_file = Image.open(back)
    file = open_file.resize((80, 80), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(file)
    label_image_accueil = Label(p1, image = image)
    label_image_accueil.image = image
    label_image_accueil.config(bg = 'grey30',  fg = 'white')
    label_image_accueil.grid(row = 0, column = 0, sticky = W)

    back2 = 'mouton.png'
    open_file = Image.open(back2)
    file = open_file.resize((80,90), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(file)
    label_image_accueil2 = Label(p1, image = image2)
    label_image_accueil2.image = image2
    label_image_accueil2.config(bg = 'grey30',  fg = 'white')
    label_image_accueil2.grid(row = 0, column = 4, sticky = E)

    blank = Label(p1, text = ' \n ')
    blank.config(font = labelfont3, bg = 'grey30',  fg = 'white')
    blank.grid(row = 1, column = 0, columnspan = 5)
    
    #TEAM BLUE

    goldB = Label(p2, text = 'gold       = ')
    goldB.config(font = labelfont3, bg = 'grey30',  fg = 'dodger blue')
    goldB.grid(row = 0, column = 0, sticky = E)

    minB = Label(p2, text = 'minions    = ')
    minB.config(font = labelfont3, bg = 'grey30',  fg = 'dodger blue')
    minB.grid(row = 1, column = 0, sticky = E)

    champB = Label(p2, text = 'champions  = ')
    champB.config(font = labelfont3, bg = 'grey30',  fg = 'dodger blue')
    champB.grid(row = 2, column = 0, sticky = E)
    
    towB = Label(p2, text ='tower shut = ')
    towB.config(font = labelfont3, bg = 'grey30',  fg = 'dodger blue')
    towB.grid(row = 3, column = 0, sticky = E)
    
    goldEB = Entry(p2)
    goldEB.config(width = 5)
    goldEB.grid(row = 0, column = 1, sticky = W)
    goldEB.focus_force()

    creepEB = Entry(p2)
    creepEB.config(width = 5)
    creepEB.grid(row = 1, column = 1, sticky = W)

    killEB = Entry(p2)
    killEB.config(width = 5)
    killEB.grid(row = 2, column = 1, sticky = W)
    
    values_towers = [i for i in range(0,12)]
    choiceB = ttk.Combobox(p2, values = values_towers)
    choiceB.config(width = 2)
    choiceB.grid(row = 3, column = 1, sticky = W)
    
    blankv = Label(p2, text = '')
    blankv.config(font = labelfont4, bg = 'grey30',  fg = 'white')
    blankv.grid(column = 2)
    
    #TEAM RED
    
    goldR = Label(p2, text = ' gold       = ')
    goldR.config(font = labelfont3, bg = 'grey30',  fg = 'brown3')
    goldR.grid(row = 0, column = 3, sticky = E)

    minR = Label(p2, text = ' minions    = ')
    minR.config(font = labelfont3, bg = 'grey30',  fg = 'brown3')
    minR.grid(row = 1, column = 3, sticky = E)

    champR = Label(p2, text = ' champions  = ')
    champR.config(font = labelfont3, bg = 'grey30',  fg = 'brown3')
    champR.grid(row = 2, column = 3, sticky = E)
    
    towR = Label(p2, text = ' tower shut = ')
    towR.config(font = labelfont3, bg = 'grey30',  fg = 'brown3')
    towR.grid(row = 3, column = 3, sticky = E)

    blank3 = Label(p2, text = ' \n ')
    blank3.config(font = labelfont3, bg = 'grey30',  fg = 'white')
    blank3.grid(row = 4, column = 0, columnspan = 5)
    
    goldER = Entry(p2)
    goldER.config(width = 5)
    goldER.grid(row = 0, column = 4, sticky = W)
    goldER.focus_force()

    creepER = Entry(p2)
    creepER.config(width = 5)
    creepER.grid(row = 1, column = 4, sticky = W)

    killER = Entry(p2)
    killER.config(width = 5)
    killER.grid(row = 2, column = 4, sticky = W)
    
    choiceR = ttk.Combobox(p2, values = values_towers)
    choiceR.config(width = 2)
    choiceR.grid(row = 3, column = 4, sticky = W)
        
    ML = Button(p4, text = ' Start Prediction ', command = ML_b)
    ML.config(font = labelfont3, bg = 'grey30',  fg = 'white')
    ML.grid(row = 1, column = 2, sticky = W+E)
    
    reset = Button(p4, text = ' Reset ', command = resetw)
    reset.config(font = labelfont3, bg = 'grey30',  fg = 'white')
    reset.grid(row = 1, column = 1, sticky = W+E)
    
    lol = Button(p4, text = " What's LoL ? ", command = lolw)
    lol.config(font = labelfont3, bg = 'grey30',  fg = 'white')
    lol.grid(row = 1, column = 0, sticky = W+E)
    

def help_b():
    texte = []
    with open("help.txt", "r") as file:
        lines = file.readlines()
        chain = ''
        for i in range(len(lines)):
            print(lines[i])
            texte.append(lines[i])
            chain = chain + str(texte[i])
            # print(chain)
        aligned_chain = "{:<10}".format(chain)
        
        
    # window2 = Toplevel(window)
    # window2.title('help')
    # center_screen(window2)
    # window2.resizable(0,0)    
        
    label_text = Label(window, text = aligned_chain)
    label_text.config(font = labelfont4, fg = 'white', bg = 'grey30')
    label_text.grid(row = 1, column = 1, columnspan = 3)

def kill(name_of_the_window):
    name_of_the_window.destroy()

def center_screen(name_of_the_window):
    # Gets the requested values of the height and widht.
    windowWidth = name_of_the_window.winfo_reqwidth()
    windowHeight = name_of_the_window.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(name_of_the_window.winfo_screenwidth()/3 - windowWidth/2)
    positionDown = int(name_of_the_window.winfo_screenheight()/3 - windowHeight/2)
    
    # Positions the window in the center of the page.
    name_of_the_window.geometry("+{}+{}".format(positionRight, positionDown))

    # name_of_the_window.winfo_height()
    # name_of_the_window.winfo_width()


#-----------WINDOW-------------------------------------------------------------

window = Tk()
window.title('dnq ml program')
window.config(bg = 'grey30')
window.resizable(False, False)
center_screen(window)

#-----------LABELS-------------------------------------------------------------

labelfont = ('OCR A Extended', 20)
labelfont2 = ('OCR A Extended', 19)
labelfont3 = ('OCR A Extended', 14)
labelfont4 = ('OCR A Extended', 10)


title = Label(window, text = "\n  DNQ's INTERFACE  \n")
title.config(font = labelfont, bg = 'grey30',  fg = 'white')
title.grid(row = 0, column = 1, columnspan = 3)


#-----------IMAGES-------------------------------------------------------------
back = 'logo.png'
open_file = Image.open(back)
file = open_file.resize((70, 70), Image.ANTIALIAS)
image = ImageTk.PhotoImage(file)
label_image_accueil = Label(window, image = image)
label_image_accueil.image = image
label_image_accueil.config(bg = 'grey30',  fg = 'white')
label_image_accueil.grid(row = 0, column = 0, sticky = W+E)

back2 = 'riot.png'
open_file = Image.open(back2)
file = open_file.resize((80, 70), Image.ANTIALIAS)
image2 = ImageTk.PhotoImage(file)
label_image_accueil2 = Label(window, image = image2)
label_image_accueil2.image = image2
label_image_accueil2.config(bg = 'grey30',  fg = 'white')
label_image_accueil2.grid(row = 0, column = 4, sticky = W+E)

#-----------BOTTOM-LABELS------------------------------------------------------

# choix_team = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinium', 'Diamond', 'Master', 'Grandmaster', 'Challenger']
# c1 = ttk.Combobox(window, values = choix_team, text = 'Elo Rank of the game')
# c1.grid(row = 1, column = 0, columnspan = 3)

blank = Label(window, text = ' \n ')
blank.config(font = labelfont3, bg = 'grey30',  fg = 'white')
blank.grid(row = 2, column = 0, columnspan = 3)

search = Button(window, text = ' Predict From Input ', command = stats_b)
search.config(font = labelfont3, bg = 'grey30',  fg = 'white')
search.grid(row = 3, column = 0, columnspan = 3, sticky = W+E)

help = Button(window, text = '  Need help ?  ', command = help_b)
help.config(font = labelfont3, bg = 'grey30',  fg = 'white')
help.grid(row = 3, column = 3, columnspan= 2, sticky = W+E)

# live = Button(window, text = ' Predict Live Games ', command = live_b)
# live.config(font = labelfont3, bg = 'grey30',  fg = 'white')
# live.grid(row = 3, column = 3, columnspan = 2)

#------------------------------------------------------------------------------

window.mainloop()