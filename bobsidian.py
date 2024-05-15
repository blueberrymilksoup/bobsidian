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

def window(type):
     popup = Toplevel(main) # popup window
     popup.geometry("500x600")
     popup.title("BOBSIDIAN Select Note")

     if type == "open":
          option = tk.Button(popup, text="option1")
     elif type == "save":
          popup.title("BOBSIDIAN Enter Information")
          note_name = tk.Entry(popup)
          save_button = tk.Button(popup, text="option1")
     elif type == "delete":
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

popup = Toplevel(main) # popup window
popup.geometry("500x600")
popup.title("BOBSIDIAN Open")


text_edit = tk.Text(main, height=100, width=100)
text_edit.pack(side=RIGHT, expand=TRUE, fill="both")

# make another frame to put the sidebar buttons in and maybe put a settings button? who knows lmao
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
button_save = tk.Button(frames_button, text="Save", command=lambda: window("save"))
button_save.grid(row=2, column = 0, padx=5, pady=5)
button_delete = tk.Button(frames_button, text="Delete", command=lambda: window("delete"))
button_delete.grid(row=3, column = 0, padx=5, pady=5)

main.mainloop()

