from model.ITCompany import ITCompany
from view.Printer import Printer
import os


class CompanyCreator:
    @staticmethod
    def create_company():
        name = input("Введите название новой IT-компании: ")
        initial_budget = float(input("Введите начальный бюджет компании: "))
        location = input("Введите место дислокации IT-компании: ")
        return ITCompany(name, initial_budget, location)

