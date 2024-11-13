from model.Investor import Investor
from model.Customer import Customer
from model.ITCompany import ITCompany
from CompanyMenu import CompanyMenu
from model.CompanyCreator import CompanyCreator
from CustomerMenu import CustomerMenu
from view.Printer import Printer
import pickle


class MainMenu:
    SAVE_FILE = "company_state.pickle"

    @staticmethod
    def main_menu():
        company = MainMenu.load_company_state()

        if company is None:
            Printer.print_welcome()
            company = MainMenu.create_company()

        while True:
            Printer.print_main_menu()
            choice = input("\nВыберите действие: ")

            if choice == '1':
                CompanyMenu.company_menu(company)

            elif choice == '2':
                client_type = input("Введите тип клиента (заказчик, инвестор): ")
                if client_type.lower() == 'заказчик':
                    name = input("Введите ваше имя: ")
                    if not name.isalpha():
                        Printer.print_valid_name()
                        continue
                    company.get_client_manager().add_client(Customer(name))
                elif client_type.lower() == 'инвестор':
                    available_projects = company.get_projects()
                    if available_projects:
                        name = input("Введите имя инвестора: ")
                        invested_amount = input("Введите сумму инвестиций: ")
                        try:
                            invested_amount = float(invested_amount)
                            if invested_amount <= 0:
                                raise ValueError("Сумма инвестиций должна быть положительным числом.")
                        except ValueError as e:
                            Printer.print_valid_sum()
                            continue
                        investor = Investor(name, invested_amount)
                        Printer.print_all_proj_for_invest()
                        for idx, project in enumerate(available_projects, start=1):
                            print(f"{idx}. {project.get_proj_name()} (Бюджет: {project.get_budget()})")
                        project_choice = input("Введите номер проекта для инвестирования: ")
                        try:
                            project_choice = int(project_choice)
                            if 1 <= project_choice <= len(available_projects):
                                selected_project = available_projects[project_choice - 1]
                                investor.invest_in_project(selected_project, invested_amount)
                                selected_project.add_investor(investor, invested_amount)
                                company.get_client_manager().add_client(investor)
                            else:
                                Printer.print_invalid_proj()
                        except ValueError:
                            Printer.print_invalid_number_proj()
                    else:
                        Printer.print_no_proj_invest()

            elif choice == '3':
                customer_name = input("Введите ваше имя: ")
                if not customer_name.isalpha():
                    Printer.print_name_error()
                    continue
                customer = company.get_customer_by_name(customer_name)
                if customer:
                    CustomerMenu.customer_menu(company, customer)
                else:
                    Printer.print_no_client()

            elif choice == '4':
                MainMenu.save_company_state(company)
                break

            elif choice == '5':
                CompanyCreator.delete_company(MainMenu.SAVE_FILE)
                break
            else:
                Printer.print_invalid_choose()

    @staticmethod
    def create_company():
        while True:
            name = input("Введите название новой IT-компании: ")
            if not all(char.isalpha() or char.isspace() for char in name):
                Printer.print_error_company()
                continue

            try:
                initial_budget = float(input("Введите начальный бюджет компании: "))
                if initial_budget < 0:
                    Printer.print_invalid_budget()
                    continue
            except ValueError:
                Printer.print_invalid_format()
                continue

            location = input("Введите место дислокации IT-компании: ")
            if not location.isalpha():
                Printer.print_invalid_location()
                continue
            return ITCompany(name, initial_budget, location)

    @staticmethod
    def save_company_state(company):
        with open(MainMenu.SAVE_FILE, 'wb') as f:
            pickle.dump(company, f)
        Printer.print_success_saving_file()

    @staticmethod
    def load_company_state():
        try:
            with open(MainMenu.SAVE_FILE, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
