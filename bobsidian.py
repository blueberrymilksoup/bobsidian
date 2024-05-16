import tkinter as tk
from tkinter import *
import os
import sys

main_list = "list_of_notes.txt"
os.chdir("files")

def saves(name): # create new
    with open(main_list, "a") as new_note:
        new_note.write(name)
    name = name.strip("\n")
    with open(name, "w") as file_input: # should be able to create a new file 
        file_input.write("")
    text_edit.delete(1.0,tk.END)
    main.title(f"BOBSIDIAN - {name}")

def saver(): # press save button after writing
    with open("current.txt", "r") as reader: # read current and get the name of the new file
        line_read = reader.readlines()
        note_name = line_read[0]
        new_name = note_name.strip('\n')
    with open(new_name, "w") as file_input: # create the new 
        contents = text_edit.get(1.0, tk.END)
        file_input.write(contents)
    main.title(f"BOBSIDIAN - {new_name}")

def open_delete(selections,type):
        ftuple = get_ftuple(selections)
        index = ftuple[0]
        note_name = selections.get(index).strip("\n") # REMOVE THE \N

        if type == "open":
            save_current(note_name)
            text_edit.delete("1.0",tk.END)
            with open(note_name, "r") as file_output:
                contents = file_output.read()
                text_edit.insert(tk.END, contents)
            main.title(f"BOBSIDIAN - {note_name}")

        else: # delete function
            items = ""
            with open(main_list, "r") as reader:
                lines = reader.readlines()
            with open(main_list, "w") as writer:
                for item in lines:
                    if item.strip("\n") != note_name:
                        items = items + item
                writer.write(items)
                os.remove(note_name)
            return

def open_existing_file(name): # opens existing note
    name = name.strip("\n")
    save_current(name)
    with open(name, "r") as file_input:
        contents = file_input.read()
        text_edit.insert(tk.END, contents)
        main.title(f"BOBSIDIAN - {name}")
    return

def checker(name): # checks if the note name exists
    name = name+f".txt\n"
    save_current(name)
    with open(main_list, "r") as reader:
        notes = reader.read()
        if name not in notes:
            saves(name)
        else:
            popup = tk.Toplevel(main) # popup window
            popup.geometry("300x300")
            popup.title("BOBSIDIAN Error")
            new_file = tk.Button(popup, text="Choose a new name", command=lambda: [window("new"),destroy(popup)])
            new_file.pack()
            open_existing = tk.Button(popup, text="Open existing file", command=lambda:[open_existing_file(name), destroy(popup)])
            open_existing.pack()
    return

def save_current(name):
    with open("current.txt", "w") as writer: # save the name of the current file
        writer.write(name)
    return

def get_selections(popup): # returns the listbox of notes
    selections = tk.Listbox(popup)
    i = 0
    with open(main_list, "r") as reader:
        notes = reader.readlines()
        for file in notes:
            selections.insert(i,file)
            i += 1
    selections.pack()
    return selections

def get_ftuple(selections): # gets the tuple from the listbox
    ftuple=selections.curselection()
    return ftuple

def window(type): # will only build the windows and buttons etc
     popup = Toplevel(main) # popup window
     popup.geometry("300x300")
     popup.title("BOBSIDIAN Select Note")

     if type == "open": # open note
          popup.geometry("700x700")
          selections = get_selections(popup)
          real_open = tk.Button(popup, text="Open file", command=lambda:[open_delete(selections, "open"), destroy(popup)])
          real_open.pack()

     elif type == "delete":
        selections = get_selections(popup)
        ftuple = get_ftuple(selections)
        real_delete = tk.Button(popup, text="Delete file", command=lambda:[open_delete(selections,"del"), destroy(popup), destroy(selections)])
        real_delete.pack()

     elif type == "new":
         popup.title("BOBSIDIAN Enter Information")
         name_entry = tk.Entry(popup)
         name_entry.pack() 
         button_name = tk.Button(popup, text="Start File", command = lambda: [checker(name_entry.get()),destroy(popup)])
         button_name.pack()

def destroy(item):
    item.destroy()
    return

def hide_sidebar():
     frames_button.pack_forget()
     frames_settings.pack_forget()
     frames_settings_s.pack(side=TOP)
     button_sidebar_s.pack()
def show_sidebar():
     frames_settings_s.pack_forget()
     button_sidebar_s.pack_forget()
     frames_settings.pack(side=TOP)
     frames_button.pack(side=TOP, expand=TRUE, fill="y")

main = tk.Tk() # makes the window
main.title("BOBSIDIAN")
main.rowconfigure(0, minsize=800)
main.columnconfigure(1, minsize=800)

window_open = Toplevel(main) # popup window to check if you want to open a file or do a new one
window_open.geometry("500x600")
window_open.title("BOBSIDIAN Start")
button_new = tk.Button(window_open, text="Create New Note",command=lambda:[window("new"),destroy(window_open)])
button_new.pack()
button_open_start = tk.Button(window_open, text="Open Existing",command=lambda:[window("open"),destroy(window_open)])
button_open_start.pack()

text_edit = tk.Text(main, height=100, width=100)
text_edit.pack(side=RIGHT, expand=TRUE, fill="both")
# make another frame to put the sidebar buttons in and maybe put a settings button? DONE
frames_settings = tk.Frame(main,relief = tk.RAISED, bd = 3)
frames_settings.pack(side=TOP)
button_sidebar = tk.Button(frames_settings, text="|||", command=hide_sidebar)
button_sidebar.grid(row=0, column = 0, padx=5, pady=5)
frames_settings_s = tk.Frame(main,relief = tk.RAISED, bd = 3)
frames_settings_s.pack(side=TOP)
frames_settings_s.pack_forget()

button_sidebar_s = tk.Button(frames_settings_s, text="|||", command=show_sidebar)
button_sidebar.grid(row=0, column = 0, padx=5, pady=5)
frames_button = tk.Frame(main, relief = tk.RAISED, bd = 3)
frames_button.pack(side=TOP, expand=TRUE, fill="y")
button_open = tk.Button(frames_button, text="Open", command=lambda: window("open"))
button_open.grid(row=1, column = 0, padx=5, pady=5)
button_save = tk.Button(frames_button, text="Save", command=saver)
button_save.grid(row=2, column = 0, padx=5, pady=5)
button_delete = tk.Button(frames_button, text="Delete", command=lambda: window("delete"))
button_delete.grid(row=3, column = 0, padx=5, pady=5)
button_neww = tk.Button(frames_button, text="New", command=lambda: window("new"))
button_neww.grid(row=4, column = 0, padx=5, pady=5)

main.mainloop()