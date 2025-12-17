

# Step 1: Import tkinter
from tkinter import *

# Step 2: GUI interaction
window = Tk()
window.title("Simple Menu Example")  # Optional: Set window title

# Step 3: Adding inputs
menu = Menu(window)

# Create File menu
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Add File menu to the menu bar
menu.add_cascade(label="File", menu=file_menu)

# Configure the window to use the menu
window.config(menu=menu)

# Step 4: Main loop
window.mainloop()