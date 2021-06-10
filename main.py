import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def startup_dialog(labeltext):
    result = None  # helps program exit if ok is hit without input
    root_dialog = tk.Tk()
    frame = ttk.Frame(root_dialog)
    root_dialog.title("File Manager")
    frame.pack(fill='both', expand=True)

    def on_ok():
        nonlocal result  # so it shows up outside on_ok

        result = entry.get()
        root_dialog.destroy()  # stops root_dialog.mainloop()

    label = ttk.Label(frame, text=labeltext)
    label.place(relx=0.5, rely=0.3, anchor='center')
    label.config(font=('New Times Roman', 10))
    entry = ttk.Entry(frame)
    entry.place(relx=0.5, rely=0.5, anchor='center')
    entry.focus_set()
    okbutton = ttk.Button(frame, text="OK", command=on_ok)
    okbutton.place(relx=0.5, rely=0.8, anchor='center')

    w = 275  # width for the Tk root
    h = 175  # height for the Tk root

    # get screen width and height
    ws = root_dialog.winfo_screenwidth()  # width of the screen
    hs = root_dialog.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root_dialog.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root_dialog.bind('<Return>', lambda event=None: okbutton.invoke())

    root_dialog.mainloop()

    return result


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x + '  ' + str(os.path.getsize(x)) + ' bytes')


def listDir():
    txt_edit.delete('1.0', END)
    global current_dir
    os.chdir(current_dir)
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


def sortList():
    txt_edit.delete('1.0', END)
    global current_dir
    os.chdir(current_dir)
    dirlist = os.listdir(os.getcwd())
    dirlist.sort(key=lambda f: os.stat(f).st_size, reverse=True)
    for x in dirlist:
        txt_edit.insert(END, x + " {:.02f} ".format(os.path.getsize(x)) + ' bytes \n')


def sizeChange():
    txt_edit.delete('1.0', END)
    global current_dir
    os.chdir(current_dir)
    dirlist = os.listdir(os.getcwd())
    # dirlist.sort(key=lambda f: os.stat(f).st_size, reverse=True)
    for x in dirlist:
        txt_edit.insert(END, x + " {:.02f} ".format(os.path.getsize(x) / 2 ** 20) + ' MB \n')


def upList():
    txt_edit.delete('1.0', END)
    global current_dir
    os.chdir(current_dir)
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


def dwnList():
    txt_edit.delete('1.0', END)
    global current_dir
    os.chdir(current_dir)
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


def enterDir():
    global current_dir
    direc = dir_var.get()
    txt_edit.delete('1.0', END)

    try:  # Incase wrong input for directory
        temp_dir = current_dir + "\\" + direc
        os.chdir(temp_dir)
        listdir = os.listdir(os.getcwd())
        for x in listdir:
            txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')

        input_box.delete(0, 'end')
        print(current_dir)
    except FileNotFoundError:
        print("Directory not found")
        os.chdir(current_dir)
        listdir = os.listdir(os.getcwd())
        for x in listdir:
            txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')
        input_box.delete(0, 'end')
        tk.messagebox.showwarning(title=None, message="Doesn't exist")

        return
    current_dir = temp_dir


def backDir():
    txt_edit.delete('1.0', END)
    global current_dir
    beg_dir = answer + ":\\"
    if len(current_dir) <= 4:
        os.chdir(current_dir)
        listdir = os.listdir(os.getcwd())
        for x in listdir:
            txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')
        return
    else:
        try:
            temp_dir = current_dir[:current_dir.rfind('\\')]
            print(temp_dir)
            os.chdir(temp_dir)
            listdir = os.listdir(os.getcwd())
            for x in listdir:
                txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')
        except FileNotFoundError:
            print("Directory not found")
            os.chdir(current_dir)
            listdir = os.listdir(os.getcwd())
            for x in listdir:
                txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')
    current_dir = temp_dir

# Stores every drive connected on PC in a list by going thru alphabet looking at each letter
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

answer = startup_dialog("Which drive do you want to enter? \n" + str(drives))

# Setup window
window = tk.Tk()
window.title("File Manager")
window.resizable(width=True, height=True)

dir_var = tk.StringVar()
current_dir = answer + ":\\"

w = 800  # width for the Tk root
h = 650  # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.columnconfigure(1, weight=1)
window.columnconfigure(3, pad=7)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, pad=7)

lbl = Label(window, text="Looking at " + answer + ": Drive")
lbl.grid(sticky=W, pady=4, padx=5)

scrollbar = Scrollbar(window)
scrollbar.grid(row=1, column=2, rowspan=5, sticky='ns')

txt_edit = Text(window, yscrollcommand=scrollbar.set)
txt_edit.grid(row=1, column=0, columnspan=2, rowspan=5, padx=5, sticky=E + W + S + N)

ref_but = Button(window, text="Refresh", width=10, command=listDir)
ref_but.grid(row=1, column=3)

sort_but = Button(window, text="Sort", width=10, command=sortList)
sort_but.grid(row=2, column=3, pady=4, padx=10)

size_but = Button(window, text="Size to MB", width=10, command=sizeChange)
size_but.grid(row=3, column=3, pady=4, padx=10)

dir_but = Button(window, text="Back", width=10, command=backDir)
dir_but.grid(row=4, column=3, pady=4, padx=10)

input_box = Entry(window, textvariable=dir_var)
input_box.grid(row=6, column=0, columnspan=2, sticky=E + W, padx=5)
input_box.focus_set()

ok_but = Button(window, text="OK", command=enterDir, width=10)
ok_but.grid(row=6, column=3)

window.bind('<Return>', lambda event=None: ok_but.invoke())
window.bind('<Escape>', lambda event=None: dir_but.invoke())

scrollbar.config(command=txt_edit.yview)

listDir()

window.focus_force()

tk.mainloop()
