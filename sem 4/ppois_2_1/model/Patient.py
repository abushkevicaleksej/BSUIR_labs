from datetime import datetime
import uuid


class Patient:
    def __init__(self, id: uuid.UUID, name: str, address: str, birthdate: datetime, appdate: datetime, docname: str, concl: str):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__birthdate = birthdate
        self.__appdate = appdate
        self.__docname = docname
        self.__concl = concl

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_birthdate(self):
        return self.__birthdate

    def get_appdate(self):
        return self.__appdate

    def get_docname(self):
        return self.__docname

    def get_concl(self):
        return self.__concl

    def tuple(self):
        values_tuple: tuple = (
            self.__id.__str__(),
            self.__name,
            self.__address,
            self.__birthdate,
            self.__appdate,
            self.__docname,
            self.__concl
        )
        return values_tuple

    def __str__(self):
        return (f"{self.__id}, Name: {self.__name}, Address: {self.__address}, Birth Date: {self.__birthdate}, "
                f"Appointment Date: {self.__appdate}, Doctor Name: {self.__docname}, Conclusion: {self.__concl}")


