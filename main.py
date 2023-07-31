from tkinter import * 
from tkinter import messagebox
import random

colors = ['red', 'green', 'blue', 'yellow','violet','purple','pink','black','white','brown','lightblue','cyan','crimson','indigo']
score = 0
timeleft = 60
       
def startGame(event):
    if timeleft == 60: #when the time equals to zero let the countdown begin
        countdown() #and after each seconds let the color should change always until the time is zero
    nextColor()

def nextColor():
    global score
    global timeleft
    if timeleft > 0:
        color_entry.focus_set() #focuses on the color entry field
        if color_entry.get().lower() == colors[1].lower(): #if the color typed on the entry field is equals to the color display on the screen
            score += 1  #let the score add by one 
        color_entry.delete(0,END) # and after delete the entry field for the next color to be typed by the player
        random.shuffle(colors)  #the random.shuffle() method chooses any color by the computer and displays it on the screen
        label.config(fg=str(colors[1]),text=str(colors[0])) 
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0: # if timeleft is greater than 0 it should reduce by 1
        timeleft -= 1
        timeLabel.config(text="Time left:" + str(timeleft))      
        timeLabel.after(1000,countdown) #countdown every seconds
    elif timeleft == 0: #if the timeleft is equal to 0 it should send a message that time is over
        messagebox.showinfo('Time',f'Time is over and your score is {score}')    
        return  
            

root = Tk()              
root.title("Color Game")
root.geometry("750x450")
root.config(background="Orange")

instruction = Label(root,text="Type the color of the word not the text;",font=('ariel',20,'bold'),bg='orange')   
instruction.pack()
scoreLabel = Label(root,text="Press Enter to begin",font=('ariel',20,'bold'),bg='orange')
scoreLabel.pack()
timeLabel  = Label(root,text="Time remaining:" + str(timeleft),font=('ariel',20),bg='orange')
timeLabel.pack()
label = Label(root,font=('ariel',70),bg='orange')
label.pack()
color_entry = Entry(root,font=30)
root.bind('<Return>',startGame)  
color_entry.pack()
color_entry.focus_set()
        
root.mainloop() 
        
    
""" import string
import random
characters = list(string.ascii_letters + string.digits + string.punctuation)
print(random.choice(characters))
 """