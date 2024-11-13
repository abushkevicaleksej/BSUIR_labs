from model.ProgrammingLanguage import ProgrammingLanguage
from model.ProgrammingLevel import ProgrammerLevel
from model.Employee import Employee
from model.Project import Project
from model.Position import Position
from ProjectMenu import ProjectMenu
from view.Printer import Printer
from model.CompanyRepository import CompanyRepository


class CompanyMenu:
    @staticmethod
    def company_menu(company):
        while True:
            Printer.print_company_menu()
            choice = input("\nВыберите действие: ")

            if choice == '1':
                name = input("Введите новое имя компании: ")
                company.set_name(name)

            elif choice == '2':

                while True:
                    name = input("Введите имя сотрудника: ")
                    if not name.isalpha():
                        Printer.print_name_error()
                        continue
                    age = int(input("Введите возраст сотрудника: "))
                    if not isinstance(age, int):
                        Printer.print_invalid_number()
                        continue
                    if age < 18:
                        Printer.print_low_age_error()
                        continue
                    elif age > 60:
                        Printer.print_high_age_error()
                        continue

                    else:
                        break
                chosen_position = None
                chosen_language = None

                while chosen_position is None:
                    Printer.print_choose_job()
                    for idx, position in enumerate(Position, start=1):
                        print(f"{idx}. {position.value}")
                    position_choice = int(input("Введите номер должности: "))
                    if 1 <= position_choice <= len(Position):
                        chosen_position = list(Position)[position_choice - 1]
                    else:
                        Printer.print_incorrect_position_input()

                while chosen_language is None:
                    Printer.print_programming_lang()
                    for idx, language in enumerate(ProgrammingLanguage, start=1):
                        print(f"{idx}. {language.value}")
                    language_choice = int(input("Введите номер языка программирования: "))
                    if 1 <= language_choice <= len(ProgrammingLanguage):
                        chosen_language = list(ProgrammingLanguage)[language_choice - 1]
                    else:
                        Printer.print_incorrect_lang_input()
                while True:
                    try:
                        work_experience = int(input("Введите трудовой стаж сотрудника: "))
                        if work_experience <= 0:
                            raise ValueError("Трудовой стаж должен быть положительным числом.")
                        age_minus_experience = age - work_experience
                        if age_minus_experience < 18:
                            raise ValueError("Разница между возрастом и трудовым стажем должна быть не менее 18 лет.")
                        break
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                try:
                    salary = int(input("Введите зарплату сотрудника: "))
                except ValueError:
                    Printer.print_incorrect_royalty_input()
                    continue

                if salary <= 0:
                    Printer.print_incorrect_royalty_input()
                    continue

                if salary > company.get_budget():
                    Printer.print_error_salary()
                    continue

                if work_experience >= 7:
                    programmer_level = ProgrammerLevel.SENIOR
                elif work_experience >= 3:
                    programmer_level = ProgrammerLevel.MIDDLE
                else:
                    programmer_level = ProgrammerLevel.JUNIOR
                try:
                    company.add_employee(
                        Employee(name, age, work_experience, language, position, programmer_level, salary))
                except ValueError as e:
                    Printer.print_add_emp_error()

            elif choice == '3':
                name = input("Введите имя проекта: ")
                existing_projects = [project.get_proj_name() for project in company.get_projects()]

                if name in existing_projects:
                    Printer.print_the_same_proj()
                else:
                    try:
                        budget = float(input("Введите бюджет проекта: "))
                        if budget <= 0:
                            raise ValueError("Бюджет должен быть положительным числом.")
                    except ValueError as e:
                        Printer.print_error_input()
                        continue
                    company.add_project(Project(name, budget))

            elif choice == '4':
                projects = company.get_projects()

                if projects:
                    for idx, project in enumerate(projects, start=1):
                        print(f"{idx}. {project.get_proj_name()}")
                    project_choice = input("Выберите проект для управления: ")

                    try:
                        project_choice = int(project_choice)
                        if 1 <= project_choice <= len(projects):
                            ProjectMenu.project_menu(company, projects[project_choice - 1])
                        else:
                            Printer.print_error_choose_proj()
                    except ValueError:
                        Printer.print_error_choose_proj_number()
                else:
                    Printer.print_no_proj_error()

            elif choice == '5':
                print(company.get_info())

            elif choice == '6':
                projects = company.get_projects()

                if projects:
                    for project in projects:
                        print(project.get_info())
                else:
                    Printer.print_no_proj_error()

            elif choice == '7':
                employees = company.get_employees()

                if employees:
                    for employee in employees:
                        print(employee.get_info())
                else:
                    Printer.print_no_emps()

            elif choice == '8':
                clients = company.get_client_manager().get_clients()
                if clients:
                    for client in clients:
                        print(f"Имя: {client.getname()}, Тип: {type(client).__name__}")
                else:
                    Printer.print_no_clients()

            elif choice == '9':
                while True:
                    Printer.show_orders()
                    order_choice = input("\nВыберите действие: ")

                    if order_choice == '1':
                        orders = company.get_orders()
                        if orders:
                            for idx, order in enumerate(orders, start=1):
                                print(f"{idx}. {order.get_info()}")
                        else:
                            Printer.print_no_order()

                    elif order_choice == '2':
                        if not company.get_employees():
                            Printer.print_no_emps_for_order()
                            continue
                        orders = company.get_orders()
                        if orders:
                            order_index = int(input(
                                "Введите номер заказа, который хотите отметить как выполненный: ")) - 1
                            if 0 <= order_index < len(orders):
                                order = orders[order_index]
                                if not order.get_assigned_employees():
                                    Printer.print_no_emps_on_order()
                                    continue
                                order.mark_as_completed()
                            else:
                                Printer.print_invalid_input()
                        else:
                            Printer.print_no_order()

                    elif order_choice == '3':
                        if not company.get_employees():
                            Printer.print_no_free_emps()
                            continue
                        order_name = input("Введите название заказа, на который хотите назначить сотрудников: ")
                        order = company.get_order_by_name(order_name)
                        if order:
                            employee_names_input = input(
                                "Введите имена сотрудников, которых хотите назначить на заказ (через запятую): ")
                            employee_names = employee_names_input.split(',')
                            employees = []
                            for name in employee_names:
                                name = name.strip()
                                try:
                                    employee = company.get_employee_by_name(name)
                                    if employee:
                                        employees.append(employee)
                                    else:
                                        raise ValueError(f"Сотрудник {name} не найден в базе компании.")
                                except ValueError as e:
                                    print(e)
                                    continue
                            if employees:
                                order.assign_employee(employees)
                            else:
                                Printer.print_no_free_emps()
                        else:
                            Printer.print_no_order()

                    elif order_choice == '4':
                        break
            elif choice == '10':
                break
            elif choice == '11':
                CompanyRepository.save_state(company)
                break
            elif choice == '12':
                loaded_company = CompanyRepository.load_state()
                if loaded_company:
                    Printer.print_success_saving_file()
                    company = loaded_company
                else:
                    Printer.print_file_not_found()
            elif choice == '13':
                name_to_remove = input("Введите имя сотрудника для увольнения: ")
                try:
                    company.remove_employee_by_name(name_to_remove)
                    Printer.print_successfull_del(name_to_remove)
                except ValueError as e:
                    print(e)
            else:
                Printer.print_invalid_choose()
