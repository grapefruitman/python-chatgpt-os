import os
import tkinter as tk
from tkinter import filedialog, Text

# Create the main window
root = tk.Tk()

# Define a function for opening a file
def open_file():
    # Ask the user to select a file to open
    filepath = filedialog.askopenfilename()
    
    # Check if a file was selected
    if filepath:
        # Open the selected file
        with open(filepath, 'r') as file:
            # Read the file's contents and display them in the Text widget
            contents = file.read()
            text_widget.insert('1.0', contents)

# Define a function for saving a file
def save_file():
    # Ask the user to select a file to save to
    filepath = filedialog.asksaveasfilename()
    
    # Check if a file was selected
    if filepath:
        # Get the contents of the Text widget
        contents = text_widget.get('1.0', tk.END)
        
        # Write the contents to the selected file
        with open(filepath, 'w') as file:
            file.write(contents)

# Create a Text widget
text_widget = Text(root)
text_widget.pack()

# Create a menu with two commands: "Open" and "Save"
menu = tk.Menu(root)
menu.add_command(label='Open', command=open_file)
menu.add_command(label='Save', command=save_file)
root.config(menu=menu)

# Start the event loop
root.mainloop()
