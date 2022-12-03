import os
import subprocess

from tkinter import Tk, Button

# Set up the root window
root = Tk()
root.title("Python OS")

# Function to run a Python program
def run_program(program_name):
  subprocess.run(["python", program_name])

# Read the programs list from the text file
with open("programs.txt", "r") as f:
  programs = f.readlines()

# Strip the newline from each program name
programs = [p.strip() for p in programs]

# Create a button for each program we want to run
for program in programs:
  btn = Button(root, text=program, command=lambda p=program: run_program(p))
  btn.pack()

# Start the GUI event loop
root.mainloop()
