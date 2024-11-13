from model.FileRepository import FileRepository
from model.ITCompany import ITCompany


class CompanyManager:
    def __init__(self, repository: FileRepository):
        self.__companies: list[ITCompany] = []
        self.__repo: FileRepository = repository