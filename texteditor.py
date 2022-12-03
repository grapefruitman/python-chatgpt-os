import tkinter as tk
from tkinter import filedialog


class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Editor")
        self.root.geometry("400x400")

        self.text = tk.Text(self.root)
        self.text.pack(fill="both", expand=True)

        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

    def open_file(self):
        filename = tk.filedialog.askopenfilename(title="Open File")
        with open(filename, "r") as file:
            self.text.insert("end", file.read())

    def save_file(self):
        filename = tk.filedialog.asksaveasfilename(title="Save File")
        with open(filename, "w") as file:
            file.write(self.text.get("1.0", "end"))

if __name__ == "__main__":
    editor = TextEditor()
    editor.root.mainloop()
