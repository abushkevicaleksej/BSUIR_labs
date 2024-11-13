
import uuid

class Doctor:
    def __init__(self, id:uuid.UUID ,docname: str, specialization: str):
        self.__id = id
        self.__docname = docname
        self.__specialization = specialization

    def get_id(self):
        return self.__id

    def get_docname(self):
        return self.__docname

    def get_specialization(self):
        return self.__specialization

    def tuple(self):
        values_tuple: tuple = (
            self.__id.__str__(),
            self.__docname,
            self.__specialization,
        )
        return values_tuple

    def __str__(self):
        return f"{self.__id}, Doctor Name: {self.__docname}, Specialization: {self.__specialization}"
