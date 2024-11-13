from view.Printer import Printer

class Project:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__employees = []
        self.__support_employee = []
        self.__is_tested = False
        self.__investments = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def get_support_employee(self):
        return self.__support_employee

    def remove_employee(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)

    def get_tested(self):
        return self.__is_tested

    def get_budget(self):
        return self.__budget

    def get_employees(self):
        return self.__employees

    def get_proj_name(self):
        return self.__name

    def receive_investment(self, company, amount):
        if amount > 0:
            self.__budget += amount
            Printer.print_invest_about_project(self.__name, amount, self.__budget)
            company.increase_budget(amount)
        else:
            Printer.print_incorrect_invest()

    def add_investor(self, investor, amount):
        self.__investments.append((investor, amount))

    def remove_support_employee(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
        elif employee == self.__support_employee:
            self.__support_employee = None
            return True
        else:
            return False

    def get_info(self):
        support_employee_name = self.__support_employee if self.__support_employee else "Ответственный за поддержку не назначен"
        is_tested = "Да" if self.__is_tested else "Нет"
        investors_info = "\n".join([f"{investor.get_name()} ({investment})" for investor, investment in self.__investments])
        return f"Проект: {self.__name},\nБюджет: {self.__budget},\nСотрудники: {[employee.get_name() for employee in self.__employees]},\nОтветственный за поддержку: {support_employee_name},\nПротестирован: {is_tested},\nИнвесторы:\n{investors_info},\nСумма инвестиций: {sum(investment for _, investment in self.__investments)}"

    def has_required_specialists(self, required_specialists):
        assigned_specialists = {employee.position for employee in self.__employees}
        return set(required_specialists).issubset(assigned_specialists)

    def assign_support_employee(self, employee):
        if employee in self.__employees:
            self.__support_employee = employee
            Printer.print_emp_on_proj(employee.get_name(), self.__name)
        else:
            Printer.print_emp_arent_on_proj(employee.get_name(), self.__name)

    def test(self):
        self.__is_tested = True
        Printer.print_proj_has_tested(self.__name)

    def get_investments(self):
        return self.__investments
