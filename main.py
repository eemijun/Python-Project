import sys
import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import simpledialog


# Lists each folder and file present in the current working directory
from tkinter.filedialog import askopenfilename


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x + '  ' + str(os.path.getsize(x)) + ' bytes')


def listDir():
    txt_edit.delete('1.0', END)
    os.chdir(answer + ":\\")
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


def sortList():
    txt_edit.delete('1.0', END)
    os.chdir(answer + ":\\")
    dirlist = os.listdir(os.getcwd())
    dirlist.sort(key=lambda f: os.stat(f).st_size, reverse=True)
    for x in dirlist:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


def upList():
    txt_edit.delete('1.0', END)
    os.chdir(answer + ":\\")
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


def dwnList():
    txt_edit.delete('1.0', END)
    os.chdir(answer + ":\\")
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        txt_edit.insert(END, x + '  ' + str(os.path.getsize(x)) + ' bytes \n')


print('Welcome to the Python File Viewer\n')

# Stores every drive connected on PC in a list.
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

# for x in range(len(drives)):
 #   print(str(5 + x) + '. ' + drives[x])

# Setup window
window = tk.Tk()
window.title("File Manager")
window.resizable(width=True, height=True)

w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

answer = "C"  # Set default
#answer = simpledialog.askstring("Input", "Which drive do you want to enter? \n" + str(drives))


window.columnconfigure(1, weight=1)
window.columnconfigure(3, pad=7)
window.rowconfigure(3, weight=1)
window.rowconfigure(5, pad=7)

lbl = Label(window, text="Windows")

lbl.grid(sticky=W, pady=4, padx=5)
txt_edit = Text(window)
txt_edit.grid(row=1, column=0, columnspan=2, rowspan=4,padx=5, sticky=E+W+S+N)

ref_but = Button(window, text="Refresh", width=10, command=listDir)
ref_but.grid(row=1, column=3)

sort_but = Button(window, text="Sort", width=10, command=sortList)
sort_but.grid(row=2, column=3, pady=4, padx=10)

help_but = Button(window, text="Help")
help_but.grid(row=5, column=0, padx=5)

ok_but = Button(window, text="OK")
ok_but.grid(row=5, column=3)

listDir()

tk.mainloop()


# while True:
#     showDir = True
#     print("1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n")
#     result = input("Choose one of the following: ")
#
#     if result == '1':
#         # Home Screen
#         print('\nQuick Access:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')
#
#         print('Drives: ')
#         for x in range(len(drives)):
#             print(str(5 + x) + '. ' + drives[x])
#
#         while True:
#             inp = input("\nEnter your Choice: ")
#
#             if inp == '1':
#                 path = 'C:\\Users\\$USERNAME\\Documents'
#                 os.chdir(os.path.expandvars(path))
#                 break
#
#             elif inp == '2':
#                 path = 'C:\\Users\\$USERNAME\\Videos'
#                 os.chdir(os.path.expandvars(path))
#                 break
#
#             elif inp == '3':
#                 path = 'C:\\Users\\$USERNAME\\Pictures'
#                 os.chdir(os.path.expandvars(path))
#                 break
#
#             elif inp == '4':
#                 path = 'C:\\Users\\$USERNAME\\Downloads'
#                 os.chdir(os.path.expandvars(path))
#                 break
#
#             elif int(inp) > 4:
#                 os.chdir(str(drives[int(inp) - 5]) + '\\')
#                 break
#
#             # elif inp in drives:
#             #    os.chdir(inp + '\\')
#             #    break
#
#             else:
#                 print('Error\nEnter a correct input / drive name.\n')
#
#         while True:
#
#             if showDir is True:
#                 listDirectories()
#
#             print('\n\nType "sort" to sort list by largest file.')
#             print('Type "exit" to exit from file manager.')
#             print('Type "back" to go up one directory.')
#
#             res = input('\nChoose a file/folder: ')
#             print('\n')
#
#             if res in os.listdir(os.getcwd()):
#                 if os.path.isfile(res):
#                     os.system('"' + res + '"')
#                 else:
#                     os.chdir(res)
#
#             elif res == 'exit':  # Exit command to exit from loop
#                 sys.exit(0)
#
#             elif res == 'back':  # Back command to go up one directory
#                 os.chdir('..')
#                 showDir = True
#
#             elif res == 'sort':
#                 dirlist = os.listdir(os.getcwd())
#                 dirlist.sort(key=lambda f: os.stat(f).st_size, reverse=True)
#                 for x in dirlist:
#                     print(x + '  ' + str(os.path.getsize(x)) + ' bytes')
#                 showDir = False
#
#             else:
#                 print('No file/folder exist of this name.')

    # if result == '2':
    #     print("You chose to rename")
    #     print('Drives: ')
    #     for x in range(len(drives)):
    #         print(str(1 + x) + '. ' + drives[x])
    #
    #     while True:
    #         inp = input("\nEnter your Choice: ")
    #
    #         if inp in drives:
    #             os.chdir(inp + '\\')
    #             break
    #         else:
    #             print('Error\nEnter a correct drive name.\n')
    #
    #     while True:
    #
    #         listDirectories()
    #
    #         print('\n\nType "exit" to exit from file manager.')
    #         print('Type "back" to go up one directory.')
    #         print('Type "rename" to rename this directory')
    #
    #         res = input('\nChoose a file to rename: ')
    #         print('\n')
    #
    #         if res in os.listdir(os.getcwd()):
    #             if os.path.isfile(res):
    #
    #                 new_name = input("Enter a new name: ")
    #                 ogDir = res
    #                 newDir = os.getcwd() + '\\' + new_name
    #                 shutil.move(ogDir, newDir)
    #             else:
    #                 os.chdir(res)
    #
    #         elif res == 'exit':  # Exit command to exit from loop
    #             sys.exit(0)
    #
    #         elif res == 'back':  # Back command to go up one directory
    #             os.chdir('..')
    #
    #         elif res == 'rename':  # Rename command to delete one directory
    #
    #             new_name = input("Enter a new name: ")
    #             ogDir = os.getcwd()
    #             os.chdir('..')
    #             newDir = os.getcwd() + '\\' + new_name
    #             shutil.move(ogDir, newDir)
    #
    #         else:
    #             print('No file/folder exist of this name.')

    # if result == '3':
    #     print("You chose to move")
    #     print('Drives: ')
    #     for x in range(len(drives)):
    #         print(str(1 + x) + '. ' + drives[x])
    #
    #     while True:
    #         inp = input("\nEnter your Choice: ")
    #
    #         if inp in drives:
    #             os.chdir(inp + '\\')
    #             break
    #         else:
    #             print('Error\nEnter a correct drive name.\n')
    #
    #     while True:
    #
    #         listDirectories()
    #
    #         print('\n\nType "exit" to exit from file manager.')
    #         print('Type "back" to go up one directory.')
    #         print('Type "cut" to move this directory')
    #
    #         res = input('\nChoose a file to move: ')
    #         print('\n')
    #
    #         if res in os.listdir(os.getcwd()):
    #
    #             if os.path.isfile(res):
    #                 og_path = os.getcwd() + "\\" + res
    #                 print("\nMove " + res + " to a desired location.")
    #
    #                 while True:
    #                     for x in range(len(drives)):
    #                         print(str(1 + x) + '. ' + drives[x])
    #
    #                     inp2 = input("\nEnter your Choice: ")
    #
    #                     if inp2 in drives:
    #                         os.chdir(inp2 + '\\')
    #                         break
    #                     else:
    #                         print('Error\nEnter a correct drive name.\n')
    #
    #                 while True:
    #                     listDirectories()
    #
    #                     print('Type "pasteManager" to paste this file in current directory')
    #
    #                     res2 = input('\nChoose a file to move: ')
    #                     print('\n')
    #
    #                     if res2 in os.listdir(os.getcwd()):
    #                         if os.path.isfile(res):
    #                             print("You can't choose a file.\nPlease choose a folder.")
    #                         else:
    #                             os.chdir(res2)
    #
    #                     elif res2 == 'pasteManager':
    #                         shutil.move(og_path, os.getcwd())
    #                         break
    #
    #             else:
    #                 os.chdir(res)
    #
    #
    #         elif res == 'exit':  # Exit command to exit from loop
    #             sys.exit(0)
    #
    #         elif res == 'back':  # Back command to go up one directory
    #             os.chdir('..')
    #
    #         elif res == 'cut':
    #             og_path = os.getcwd()
    #
    #             print("Moving the current directory")
    #             while True:
    #                 for x in range(len(drives)):
    #                     print(str(1 + x) + '. ' + drives[x])
    #
    #                 inp2 = input("\nEnter your Choice: ")
    #
    #                 if inp2 in drives:
    #                     os.chdir(inp2 + '\\')
    #                     break
    #                 else:
    #                     print('Error\nEnter a correct drive name.\n')
    #
    #             while True:
    #                 listDirectories()
    #
    #                 print('\nType "paste" to paste this folder in current directory')
    #
    #                 res2 = input('\nChoose a folder to open: ')
    #                 print('\n')
    #
    #                 if res2 in os.listdir(os.getcwd()):
    #                     if os.path.isfile(res):
    #                         print("You can't choose a file.\nPlease choose a folder.")
    #                     else:
    #                         os.chdir(res2)
    #
    #                 elif res2 == 'paste':
    #                     shutil.move(og_path, os.getcwd())
    #                     break
    #
    #         else:
    #             print('No file/folder exist of this name.')

    # if result == '4':
    #     print("You chose to copy")
    #     print('Drives: ')
    #     for x in range(len(drives)):
    #         print(str(1 + x) + '. ' + drives[x])
    #
    #     while True:
    #         inp = input("\nEnter your Choice: ")
    #
    #         if inp in drives:
    #             os.chdir(inp + '\\')
    #             break
    #         else:
    #             print('Error\nEnter a correct drive name.\n')
    #
    #     while True:
    #
    #         listDirectories()
    #
    #         print('\n\nType "exit" to exit from file manager.')
    #         print('Type "back" to go up one directory.')
    #         print('Type "copy" to copy this directory')
    #
    #         res = input('\nChoose a file to copy: ')
    #         print('\n')
    #
    #         if res in os.listdir(os.getcwd()):
    #
    #             if os.path.isfile(res):
    #                 og_path = os.getcwd() + "\\" + res
    #                 print("Move " + res + " to a desired location.")
    #
    #                 while True:
    #                     for x in range(len(drives)):
    #                         print(str(1 + x) + '. ' + drives[x])
    #
    #                     inp2 = input("\nEnter your Choice: ")
    #
    #                     if inp2 in drives:
    #                         os.chdir(inp2 + '\\')
    #                         break
    #                     else:
    #                         print('Error\nEnter a correct drive name.\n')
    #
    #                 while True:
    #                     listDirectories()
    #
    #                     print('Type "paste" to copy this file in current directory')
    #
    #                     res2 = input('\nChoose a file to move: ')
    #                     print('\n')
    #
    #                     if res2 in os.listdir(os.getcwd()):
    #                         if os.path.isfile(res):
    #                             print("You can't choose a file.\nPlease choose a folder.")
    #                         else:
    #                             os.chdir(res2)
    #
    #                     elif res2 == 'paste':
    #                         shutil.copy(og_path, os.getcwd())
    #                         break
    #
    #             else:
    #                 os.chdir(res)
    #
    #
    #         elif res == 'exit':  # Exit command to exit from loop
    #             sys.exit(0)
    #
    #         elif res == 'back':  # Back command to go up one directory
    #             os.chdir('..')
    #
    #         elif res == 'copy':
    #             og_path = os.getcwd()
    #
    #             print("Copying the current directory")
    #             while True:
    #                 for x in range(len(drives)):
    #                     print(str(1 + x) + '. ' + drives[x])
    #
    #                 inp2 = input("\nEnter your Choice: ")
    #
    #                 if inp2 in drives:
    #                     os.chdir(inp2 + '\\')
    #                     break
    #                 else:
    #                     print('Error\nEnter a correct drive name.\n')
    #
    #             while True:
    #                 listDirectories()
    #
    #                 print('\nType "paste" to copy this file in current directory')
    #
    #                 res2 = input('\nChoose a folder to open: ')
    #                 print('\n')
    #
    #                 if res2 in os.listdir(os.getcwd()):
    #                     if os.path.isfile(res):
    #                         print("You can't choose a file.\nPlease choose a folder.")
    #                     else:
    #                         os.chdir(res2)
    #
    #                 elif res2 == 'paste':
    #                     print(og_path)
    #                     folder_name = og_path.split('\\')[-1]
    #                     folder_directory = os.getcwd() + '\\' + folder_name
    #                     shutil.copytree(og_path, folder_directory)
    #                     break
    #
    #         else:
    #             print('No file/folder exist of this name.')

