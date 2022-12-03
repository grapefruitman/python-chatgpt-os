# Import the necessary libraries
import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create a new tkinter window
window = tk.Tk()

# Set the window title and size
window.title("My Python Browser")
window.geometry("800x600")

# Create a text field for the user to enter a URL
url_field = tk.Entry(window)
url_field.pack()

# Create a global variable to store the current page
current_page = ""

# Create a function to handle the "Go" button click
def go_clicked():
  # Get the URL from the text field
  url = url_field.get()

  # Use the urllib library to fetch the contents of the URL
  response = urlopen(url)
  html = response.read()

  # Use the BeautifulSoup library to parse the HTML
  soup = BeautifulSoup(html, "html.parser")

  # Extract the title of the page
  title = soup.title.string

  # Create a new tkinter label to display the title
  title_label = tk.Label(window, text=title)
  title_label.pack()

  # Update the current page global variable
  global current_page
  current_page = soup

# Create a "Go" button to fetch the URL contents
go_button = tk.Button(window, text="Go", command=go_clicked)
go_button.pack()

# Create a function to handle the "Back" button click
def back_clicked():
  # Get the previous page from the current page's "previous" attribute
  global current_page
  previous_page = current_page.previous

  # If there is no previous page, do nothing
  if previous_page is None:
    return

  # Extract the title of the previous page
  title = previous_page.title.string

  # Create a new tkinter label to display the title
  title_label = tk.Label(window, text=title)
  title_label.pack()

  # Update the current page global variable
  current_page = previous_page

# Create a "Back" button to go to the previous page
back_button = tk.Button(window, text="Back", command=back_clicked)
back_button.pack()

# Start the GUI event loop
window.mainloop()

