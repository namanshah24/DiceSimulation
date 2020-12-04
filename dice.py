import random
from tkinter import Tk, Label, Button, Entry

root = Tk()
root.geometry("800x350")
l1 = Label(root,font=("times",200))
Label(root, text="Enter Number of Dice").place(x=0,y=0)
e1 = Entry(root)
e1.place(x=120,y=0)

four_dice_message =  Label(root, text="Maximum of 4 dice are allowed")
zero_dice_message = Label(root, text="Number of Dice is set to zero or less than zero")

def roll():
    number_of_dice = int(e1.get())
    if number_of_dice > 4:
       four_dice_message.place(x=0,y=320) 
       return
    elif number_of_dice <= 0:
        zero_dice_message.place(x=0,y=295)
        return
    number = ['\u2680','\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    config_text =""
    for i in range(number_of_dice):
        config_text += f"{random.choice(number)}"
    # placing warning message labels out of the frame
    four_dice_message.place(x= -2000, y= -1000)  
    zero_dice_message.place(x= -2000, y= -1000)

    l1.config(text = config_text)
    l1.pack()

roll_button = Button(root,text= "Roll Dice",command = roll)
roll_button.place(x =310, y = 0)

root.mainloop()

