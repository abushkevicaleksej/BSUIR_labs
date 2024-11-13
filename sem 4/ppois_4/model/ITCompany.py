from model.ClientManager import ClientManager
from model.Customer import Customer


class ITCompany:
    def __init__(self, name, initial_budget, location):
        self.__name = name
        self.__budget = initial_budget
        self.__employees = []
        self.__projects = []
        self.__client_manager = ClientManager()
        self.__location = location
        self.__orders = []
        self.__investments = 0

    def receive_an_investment(self, amount):
        self.__investments += amount

    def get_investments(self):
        return self.__investments

    def get_client_manager(self):
        return self.__client_manager

    def get_employee(self, employee_name):
        for employee in self.__employees:
            if employee.get_name() == employee_name:
                return employee
        return None

    def get_order_by_name(self, order_name):
            for order in self.__orders:
                if order.get_name() == order_name:
                    return order
            return None

    def get_order_by_number(self, order_number):
        for order in self.__orders:
            if order.number == order_number:
                return order
        return None

    def get_customer_by_name(self, name):
        for client in self.__client_manager.get_clients():
            if isinstance(client, Customer) and client.get_name() == name:
                return client
        return None

    def add_order(self, order):
        self.__orders.append(order)

    def get_all_orders(self):
        return self.__orders

    def get_orders(self):
        return self.__orders

    def mark_order_as_completed(self, order_name):
        order = self.get_order_by_name(order_name)
        if order:
            order.mark_as_completed()
            self.__budget += order.get_budget()
           # Printer.print_order_success_with_name(order.get_name())
      #  else:
      #      Printer.print_no_order_by_name()

    def get_project_by_name(self, project_name):
        for project in self.__projects:
            if project.get_proj_name() == project_name:
                return project
        return None

    def remove_project(self, project):
        if project in self.__projects:
            self.__projects.remove(project)
            return True
        return False

    def get_employee_by_name(self, employee_name):
        for employee in self.__employees:
            if employee.get_name() == employee_name:
                return employee
        return None

    def get_num_of_emps(self):
        return len(self.__employees)

    def increase_budget(self, amount):
        self.__budget += amount

    def remove_employee_by_name(self, name):
        for employee in self.__employees:
            if employee.get_name() == name:
                self.__employees.remove(employee)
                return
        raise ValueError(f"Сотрудник с именем '{name}' не найден.")

    def add_project(self, project):
        if project.get_budget() <= self.__budget:
            self.__projects.append(project)
            self.__budget -= project.get_budget()
         #   Printer.print_project_was_successfully_added(project.get_proj_name(), self.__budget)
  #      else:
     #       Printer.print_no_money_for_proj(project.get_proj_name())

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self, employee):
        self.__employees.remove(employee)

    def get_employees(self):
        return self.__employees

    def get_projects(self):
        return self.__projects

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_budget(self, budget):
        self.__budget = budget

    def get_budget(self):
        return self.__budget

    def get_location(self):
        return self.__location

    def get_info(self):
        return f"Компания: {self.__name}, \nБюджет: {self.__budget},\nМестоположение: {self.__location}, \nСотрудники: {[employee.get_name() for employee in self.__employees]}, \nПроекты: {[project.get_proj_name() for project in self.__projects]}"
