#from tkinter import *
#root = Tk()
#root.title("Test1")
#root.geometry('1000x500')
#root.resizable(width=False, height=False)
#root.mainloop()

def update_page_label_patients(self, parent):
    total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Patients").fetchone()[0]
    total_pages = (total_records + self.patients_per_page.get() - 1) // self.patients_per_page.get()
    page_label_text = f"Page {self.patients_page + 1} of {total_pages}"
    page_label = ttk.Label(parent, text=page_label_text)
    page_label.pack()


def update_page_label_doctors(self, parent):
    total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Doctors").fetchone()[0]
    total_pages = (total_records + self.doctors_per_page.get() - 1) // self.doctors_per_page.get()
    page_label_text = f"Page {self.doctors_page + 1} of {total_pages}"
    page_label = ttk.Label(parent, text=page_label_text)
    page_label.pack()
    метка
    должна
    оставаться
    на
    месте
    и
    изменяться, а
    не
    писаться
    заново