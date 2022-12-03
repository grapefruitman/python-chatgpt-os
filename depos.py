import os
import subprocess

from tkinter import Tk, Button

# Set up the root window
root = Tk()
root.title("Python OS")

# Function to run a Python program
def run_program(program_name):
  subprocess.run(["python", program_name])

# Create a button for each program we want to run
programs = ["texteditor.py", "program2.py", "program3.py", "os.py"]
print(programs)
for program in programs:
  btn = Button(root, text=program, command=lambda p=program: run_program(p))
  btn.pack()

# Start the GUI event loop
root.mainloop()
