from tkinter import *
from tkinter import ttk
from model.Patient import Patient


class FormSearchResultWindow(Toplevel):
    def __init__(self, patient_list: list[Patient]):
        super().__init__()
        self.__patient_list: list[Patient] = patient_list

        # window settings

        self.title('Search Result')
        self.geometry('900x400')  # Increase the height of the window
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=10)
        self.columnconfigure(index=0, weight=1)
        self.resizable(False,False)

        # result label

        self.__result_label: ttk.Label = ttk.Label(self, text='Search Result:')
        self.__result_label.grid(row=0, column=0)

        # count label

        self.__count_label: ttk.Label = ttk.Label(self, text=f'Total find records: {len(self.__patient_list)}')
        self.__count_label.grid(row=0, column=1)  # Place the label in the same row as the result label

        # result text panel

        self.__result_panel: ttk.Frame = ttk.Frame(self)
        self.__result_panel.rowconfigure(index=0, weight=1)
        self.__result_panel.columnconfigure(index=0, weight=1)
        self.__result_text: Listbox = Listbox(self.__result_panel,
                                              listvariable=Variable(value=self.list_to_text_convert()))
        self.__result_text.grid(row=0, column=0, sticky=NSEW)
        self.__result_panel.grid(row=1, column=0, sticky=NSEW, columnspan=2)  # Let the panel span both columns

    def list_to_text_convert(self):
        text: list = []
        for i in self.__patient_list:
            text.append(i.__str__())
        return text
