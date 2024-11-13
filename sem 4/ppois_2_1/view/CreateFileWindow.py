import os
import tkinter as tk
from tkinter import ttk, filedialog

class CreateFileWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Create File")
        self.geometry('200x170')

        # Create widgets
        ttk.Label(self, text="File Type:").pack()
        self.file_type_var = tk.StringVar()
        self.file_type_combobox = ttk.Combobox(self, textvariable=self.file_type_var)
        self.file_type_combobox['values'] = ('.db', '.xml')
        self.file_type_combobox.pack()

        ttk.Label(self, text="File Name:").pack()
        self.file_name_entry = ttk.Entry(self)
        self.file_name_entry.pack()

        ttk.Button(self, text="Create", command=self.create_file).pack()

    def create_file(self):
        file_type = self.file_type_var.get()
        file_name = self.file_name_entry.get()

        if file_type and file_name:
            filename = filedialog.asksaveasfilename(defaultextension=file_type, initialfile=file_name)
            if filename:
                # Create an empty file
                with open(filename, 'w') as f:
                    pass
                print(f"File '{filename}' created.")
                self.destroy()
