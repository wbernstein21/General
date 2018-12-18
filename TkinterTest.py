# make sure to notice where you save your .py files (I saved mine in desktop)
# open Terminal
# cd Desktop  (or wherever your file was saved)
# python filename.py (to run the file)

#imports: tkinter (our gui library), and some helper libraries
import Tkinter as tk
from PIL import ImageTk, Image
from functools import partial
from random import *
import time

#function that happens when any button is pressed
def pickplace(guess, gold, trap, win, pan, p1, p2, p3):
	#if it was the index 2 button pressed they win (hardcoded!!)
	if guess == gold:
		win.title("Correct!") #change the title of the window
		pan.config(image=p3) #change the image in the label to the car
	#if it was another button, it's a goat.
		endgame = guess
	else:
		if guess == trap:
			win.title("Trap :(")#change the title of the window
			pan.config(image=p1)#change the image in the label to a goat
			endgame = guess
		elif guess > gold:
			win.title("Too high off the starboard bow me matey!")
			pan.config(image=p2)
		elif guess < gold:
			win.title("Yer too low!")
			pan.config(image=p2)

#the main game window		
myWindow = tk.Tk()

#setting the title of the window 
myWindow.title('Guess a place')

#You MUST save all images like this in variables.
#image files must be in same folder as code file
photo0 = ImageTk.PhotoImage(Image.open("test3.jpg"))
photo1 = ImageTk.PhotoImage(Image.open("test1.jpg"))
photo2 = ImageTk.PhotoImage(Image.open("test2.jpg"))
photo3 = ImageTk.PhotoImage(Image.open("test4.jpg"))
photo4 = ImageTk.PhotoImage(Image.open("test6.jpg"))

#Labels are just basic non-clickable widgets for text or images
panel = tk.Label(myWindow, image=photo3, width = 600, height = 500, anchor=tk.S)
#pack arranges it on the window
panel.pack()

#here I add three buttons to the window with text Door # 0-2
island = [" "]*10 #set up the island Here (make it all " " not 0's)
gold = randrange(0,9)
trap = randrange(0,9)
for i in range(10): 
	button = tk.Button(myWindow, text='Square # '+str(i), width = 60)
	#add the function to the button as: partial(functionName, arg1, arg2 ...)
	button.config(command=partial(pickplace, i, gold, trap, myWindow, panel, photo1, photo2, photo0)) 
	button.pack() 

#you have to have this at the bottom of your code 
#for your gui window to pop up when you run the code!
myWindow.mainloop()

