import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def select_directory():
    global path
    path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, path)


def delete_file():
    file_to_delete = entry.get() + "/" + file_entry.get()
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        messagebox.showinfo("Success", "File deleted successfully.")
    else:
        messagebox.showerror("Error", "File does not exist.")


root = tk.Tk()
root.title("File Manager")

label = tk.Label(root, text="Directory Path:")
label.pack()

entry = tk.Entry(root)
entry.pack()

browse_button = tk.Button(root, text="Browse", command=select_directory)
browse_button.pack()

file_label = tk.Label(root, text="File to delete:")
file_label.pack()

file_entry = tk.Entry(root)
file_entry.pack()

delete_button = tk.Button(root, text="Delete", command=delete_file)
delete_button.pack()

root.mainloop()