import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os
import sys
# might change the above later to not have the finder window open

main_list = "list_of_notes.txt"
print("Current directory :", os.getcwd())
os.chdir("files")
print("Current directory :", os.getcwd())
selections = tk.Listbox()

""" def saving():
    file_location = asksaveasfilename(
        defaultextension="txt", 
        filetypes=[("Text files", "*.txt"), ("All files","*.*"), ]) # ("Markdown files", "*.md"),
        #will default to save as a txt but you can do other 
    if not file_location:
        return
    with open(file_location,"w") as file_output:
        txt = text_edit.get(1.0, tk.END)
        file_output.write(txt)
    main.title(f"BOBSIDIAN - {file_location}")

def opening():
    file_location = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files","*.*")])
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location,"r") as file_input:
        txt = file_input.read()
        text_edit.insert(tk.END, txt)
    main.title(f"BOBSIDIAN - {file_location}") """

def saves(name):
    note_name = name+".txt"
    with open(main_list, "a") as new_note:
        new_note.write(f"{note_name}\n")
    with open(note_name, "w") as file_output: # should be able to create a new file 
        contents = text_edit.get(1.0, tk.END)
        file_output.write(contents)
    main.title(f"BOBSIDIAN - {name}")

def saver():
    with open(main_list, "r") as reader:
        length = int(len(reader.readlines())) - 1
        line_read = reader.readlines()
        i = 0
        while i < length:
            i +=1
        note_name = line_read[i]
    with open(note_name, "w") as file_output:
        contents = text_edit.get(1.0, tk.END)
        file_output.write(contents)
    main.title(f"BOBSIDIAN - {note_name}")

def opens():
    ftuple = selections.curselection()
    for i in ftuple:
        if i < 0:
            messagebox.showinfo(title="Error",message="Please choose only 1 file")
            window("open")
        else:
            note_name = selections.get(i) # FIX TO REMOVE THE \N
            with open(note_name, "r") as file_output:
                contents = file_output.read()
            text_edit.insert(tk.END, contents)
    main.title(f"BOBSIDIAN - {note_name}")

def checker(name):
    with open(main_list, "r") as reader:
        notes = reader.read()
        if name not in notes:
            saves(name)
        else:
            popup = Toplevel(main) # popup window
            popup.geometry("300x300")
            popup.title("BOBSIDIAN Error")
            new_file = tk.Button(text="Choose a new name", command=lambda: window("new"))
            new_file.pack()
            open_existing = tk.Button(text="Open existing file", command=opens(name))
            open_existing.pack()
            # MAKE THE BUTTONS VISIBLE


def window(type): # will only build the windows and buttons etc
     popup = Toplevel(main) # popup window
     popup.geometry("300x300")
     popup.title("BOBSIDIAN Select Note")

     if type == "open":
          # use a loop to list the items as listbox items
          popup.geometry("700x700")
          i = 0
          with open(main_list, "r") as reader:
            notes = reader.readlines()
            for file in notes:
                selections.insert(i , file)
                i = i + 1
          selections.pack()
          real_open = tk.Button(text="Open file", command=opens)
          real_open.pack()

     elif type == "save":
          """ popup.title("BOBSIDIAN Enter Information")
          name_entry = tk.Entry(popup)
          name_entry.pack(side = LEFT) 
          button_name = tk.Button(popup, text="Save File", command = lambda: checker(name_entry.get()))
          button_name.pack(side = LEFT)
          popup.destroy() """
          # enter name and get it as a variable then runs saves
          # for now..
          saver()

     elif type == "delete":
        return
     elif type == "new":
         popup.title("BOBSIDIAN Enter Information")
         name_entry = tk.Entry(popup)
         name_entry.pack(side = LEFT) 
         button_name = tk.Button(popup, text="Start File", command = lambda: checker(name_entry.get()))
         button_name.pack(side = LEFT)

def destroy(item):
    item.destroy()

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
button_new = tk.Button(window_open, command=lambda:window("new"))
button_new.pack()
button_open_start = tk.Button(window_open, command=lambda:window("open"))
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

main.mainloop()

