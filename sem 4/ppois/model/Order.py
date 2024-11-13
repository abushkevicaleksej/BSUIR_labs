class Order:
    def __init__(self, name, preferred_languages, deadline, budget):
        self.__name = name
        self.__preferred_languages = preferred_languages
        self.__deadline = deadline
        self.__budget = budget
        self.__completed = False
        self.__assigned_employees = []

    def mark_as_completed(self):
        self.__completed = True

    def get_name(self):
        return self.__name

    def get_budget(self):
        return self.__budget

    def get_pref_langs(self):
        return self.__preferred_languages

    def get_deadline(self):
        return self.__deadline

    def is_completed(self):
        if self.__completed:
            return True
        else:
            return False

    def cancel(self):
        self.__completed = False

    def get_info(self):
        status = "Выполнен" if self.__completed else "Не выполнен"
        assigned_employees_info = [employee for employee_list in self.__assigned_employees for employee in employee_list]
        assigned_employees_names = [employee.get_name() for employee in assigned_employees_info]
        info = f"Название: {self.__name}\nПредпочтительные языки: {', '.join(self.__preferred_languages)}\nДедлайн: {self.__deadline}\nБюджет: {self.__budget}\nСтатус: {status}\nНазначенные сотрудники: {', '.join(assigned_employees_names)}"
        return info

    def assign_employee(self, employee):
        self.__assigned_employees.append(employee)

    def get_assigned_employees(self):
        return self.__assigned_employees
