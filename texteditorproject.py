from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

stimulator_window = Tk()
stimulator_window.geometry('600x600')
stimulator_window.title('Pysanj')

heading = Label(
    stimulator_window,
    text='Welcome to the Text Editor',
    font=('bold', 20),
    bg='light grey'
)
heading.pack()

scrollbar = tk.Scrollbar(stimulator_window)
scrollbar.pack(side=RIGHT, fill=Y)

Editor = tk.Text(
    stimulator_window,
    width=400,
    height=450,
    yscrollcommand=scrollbar.set  # Corrected attribute name to 'yscrollcommand=scrollbar.set'
)
Editor.pack(fill=BOTH)
scrollbar.config(command=Editor.yview)

def save():
    filepath = asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = Editor.get(1.0, tk.END)
        output_file.write(text)
    stimulator_window.title(f'Entitled – {filepath}')

button = Button(
    stimulator_window,
    text='Save',
    font=('normal', 10),
    command=save,
    bg='yellow'
)
button.place(x=270, y=520)

stimulator_window.mainloop()
