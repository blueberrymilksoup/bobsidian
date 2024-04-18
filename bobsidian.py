import tkinter as tk
from tkinter.filedialog import askopenfilename , asksaveasfilename
# might change the above later to not have the finder window open

main = tk.Tk() # makes the window
main.title("BOBSIDIAN")
main.rowconfigure(0, minsize=800)
main.columnconfigure(1, minsize=800)

text_edit = tk.Text(main)
frame_button = tk.Frame(main, relief = tk.RAISED, bd = 3)

main.mainloop()

