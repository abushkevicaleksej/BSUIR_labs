class Employee:
    def __init__(self, name, age, work_experience, programming_languages=None, positions=None, programmer_level=None, salary=0, role=None):
        if age < 18:
            raise ValueError("Возраст должен быть не меньше 18.")
        if age > 60:
            raise ValueError("Возраст должен быть не больше 60.")
        if age - work_experience < 18:
            raise ValueError("Разница между возрастом и трудовым стажем не должна быть больше 18.")
        self.__name = name
        self.__age = age
        self.__work_experience = work_experience
        self.__programming_languages = programming_languages
        self.__positions = positions
        self.__programmer_level = programmer_level
        self.__salary = salary
        self.__project = None

    def assign_project(self, project):
        self.__project = project

    def get_project(self):
        return self.__project

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return self.__name

    def get_info(self):
        project_name = self.__project.name if self.__project else "Сотрудник не занят"
        if self.__programming_languages:
            languages = self.__programming_languages.value
        else:
            languages = 'Не указан'
        if self.__positions:
            positions = self.__positions.value
        else:
            positions = 'Не указана'
        level = self.__programmer_level.value if self.__programmer_level else 'Не указан'
        return (f"Имя: {self.__name}, \n"
                f"Возраст: {self.__age}, \n"
                f"Трудовой стаж: {self.__work_experience}, \n"
                f"Язык программирования: {languages}, \n"
                f"Должность: {positions}, \n"
                f"Уровень программиста: {level}, \n"
                f"Зарплата: {self.__salary}, \n"
                f"Проект: {project_name}")
