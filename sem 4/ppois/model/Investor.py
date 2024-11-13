from model.Client import Client
from view.Printer import Printer


class Investor(Client):
    def __init__(self, name, invested_amount=0):
        super().__init__(name)
        self.__invested_amount = invested_amount
        self.__budget = 0

    def increase_budget(self, amount):
        self.__budget += amount

    def get_budget(self):
        return self.__budget

    def get_invested_amount(self):
        return self.__invested_amount

    def invest_in_company(self, company, amount):
        if amount > 0:
            company.receive_an_investment(amount)
            self.__invested_amount += amount
            print(f"{self.getname()} инвестировал {amount} в компанию {company.get_name()}.")
        else:
            Printer.print_incorrect_invest()

    def invest_in_project(self, project, amount):
        if amount > 0:
            project.receive_investment(self, amount)
            self.__invested_amount += amount

            print(f"{self.get_name()} инвестировал {amount} в проект {project.get_proj_name()}.")
        else:
            Printer.print_incorrect_invest()
