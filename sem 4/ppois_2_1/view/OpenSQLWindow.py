from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from controller.DbController import DbController


class OpenMsSqlWindow(tk.Toplevel):
    def __init__(self, master, application):
        super().__init__(master=master)
        self.title("Open MS SQL connection")
        self.application = application

        self.connection_string = tk.StringVar()

        name_frame = ttk.LabelFrame(self, text="Connection string")
        self.name_entry = ttk.Entry(name_frame, textvariable=self.connection_string, width=300)
        self.name_entry.pack()
        name_frame.pack(pady=10)

        add_button = ttk.Button(self, text="Open connection", command=self.open_connection)
        add_button.pack(pady=10)

        self.connection_string.set(
            'DRIVER={SQL Server};SERVER=localhost,1433;DATABASE=Patients;UID=SA;PWD=PatientsDb123$')

    def open_connection(self):
        if len(self.connection_string.get()) == 0:
            return
        try:
            db_repo = DbController(self.connection_string.get())
            self.application.repo = db_repo
            self.destroy()
        except:
            tk.messagebox.showinfo(title='Error', message="Can't open connection")