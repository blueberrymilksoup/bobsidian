import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
# might change the above later to not have the finder window open

def saving():
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
    main.title(f"BOBSIDIAN - {file_location}")

def deleting():
    return

def window(type):
     popup = Toplevel(main) # popup window
     popup.geometry("500x600")
     popup.title("BOBSIDIAN Select Note")

     if type == "open":
          option = tk.button(popup, text="option1")
     elif type == "save":
          note_name = tk.entry(popup)
          save_button = tk.button(popup, text="option1")



def open_window():
     popup = Toplevel(main) # popup window
     popup.geometry("500x600")
     popup.title("BOBSIDIAN Select Note")

def save_window():
     popup = Toplevel(main) # popup window
     popup.geometry("500x600")
     popup.title("BOBSIDIAN Save")

def hide_sidebar():
        frames_button.pack_forget()
        button_sidebar.pack_forget()
        button_sidebar_s.pack(side=TOP)

def show_sidebar():
     button_sidebar.pack(side=TOP)
     frames_button.pack(side=TOP, expand=TRUE, fill="y")
     button_sidebar_s.pack_forget()
     

main = tk.Tk() # makes the window
main.title("BOBSIDIAN")
main.rowconfigure(0, minsize=800)
main.columnconfigure(1, minsize=800)

popup = Toplevel(main) # popup window
popup.geometry("500x600")
popup.title("BOBSIDIAN New Note")



text_edit = tk.Text(main, height=100, width=100)
# text_edit.grid(row=0,column=1, sticky="nsew")
text_edit.pack(side=RIGHT, expand=TRUE, fill="both")

button_sidebar = tk.Button(main, text="|||", command=hide_sidebar)
button_sidebar.pack(side=TOP)
#button_sidebar.grid(row=0, column = 0, padx=5, pady=5)

button_sidebar_s = tk.Button(main, text="|||", command=show_sidebar)
button_sidebar_s.pack_forget()

# make another frame to put the sidebar buttons in and maybe put a settings button? who knows lmao


frames_button = tk.Frame(main, relief = tk.RAISED, bd = 3)
frames_button.pack(side=TOP, expand=TRUE, fill="y")

#button_sidebar = tk.Button(frames_button, text="|||", command=sidebar)
#button_sidebar.grid(row=0, column = 0, padx=5, pady=5)

button_open = tk.Button(frames_button, text="Open", command=open_window)
button_open.grid(row=1, column = 0, padx=5, pady=5)

button_save = tk.Button(frames_button, text="Save", command=save_window)
button_save.grid(row=2, column = 0, padx=5, pady=5)

button_delete = tk.Button(frames_button, text="Delete", command=delete_window)
button_delete.grid(row=3, column = 0, padx=5, pady=5)

main.mainloop()

