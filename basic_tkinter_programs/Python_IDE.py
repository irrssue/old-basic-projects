from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename, asksaveasfile
from tkinter.messagebox import *
import subprocess 

compiler = Tk()
compiler.title('Python IDE by Austin Rolert')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout = subprocess.PIPE,
                                        stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def The_Creater():
    showinfo("From The creater of this Program", "This Python IDE editor is written by IRRSSUE \nWish y'll the best /Irrssue")

def help():
    showinfo("Help", "You needs to save your file before you run your code \nEditor doen't work in input function apologize about that it's what it's \nIf you have more qus DM me in austinrolert@gmail.com")

def follow_me():
    showinfo("Social Media accounts", "Instagram - irrssue \nTwitter - @irrssue \nGmail - austinrolert@gmail.com")

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Opne', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='The_Creater', command=The_Creater)
about_menu.add_command(label='Help', command=help)
about_menu.add_command(label='Follow_Me', command=follow_me)
menu_bar.add_cascade(label='About', menu=about_menu)

compiler.config(menu=menu_bar)
editor= Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()
compiler.mainloop()

#I hope you can learn new tipe from this 
#and you can make your own too !!! 
#wunna better at code? go to code war and train daily for 100 days and 12+hours per day you can master python by that way 
#wish y'll the best 
# \IRRSSUE 