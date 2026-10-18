#Import with exception handling
#use cus, if try isn't work except will
from tkinter import *
from tkinter.messagebox import *

#defing objects
def print_text():
	print(root,"Hi! i r r s s u e ")
def clicktoexit():
	exit()
def messagebox():
	showinfo("Developmer", "This basic program is develop by IRRSSUE \n which is 15 years old beginner programmer \n ------have fun------ :)")

#creating tkinter window
root = Tk()
root.geometry('250x250')
root.title("Irrssue")

#making menu bar

menu_bar = Menu(root)
root.config(menu=menu_bar)

help_menu = Menu(menu_bar, tearoff=0, bg='#B8A898')
menu_bar.add_cascade(label="About", menu=help_menu,background='#C3B8AD')
help_menu.add_command(label="About", command=messagebox)

#making some buttons
idk = Button(root, text = ' C L I C K ! ', bd = 1, bg='#52626A', command = print_text)
idk.place(x=100 , y=50)

idk2 = Button(root, text= "Exit", bg= '#F4CDD5'
, command = clicktoexit)
idk2.place(x=117, y =10)


#run mainloop
root.mainloop()